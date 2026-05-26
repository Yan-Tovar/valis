from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.inspection import inspect
from sqlalchemy import or_

from database.connection import SessionLocal

from core.database.validators import Validators
from core.database.relationship_inspector import RelationshipInspector
from core.database.query_builder import QueryBuilder
from core.database.response import Response
from core.database.exceptions import (
    RecordNotFound,
    RelatedRecordsError
)
from core.database.serializer import Serializer

from core.database.foreign_key_validator import (
    ForeignKeyValidator
)

from core.database.type_validator import (
    TypeValidator
)

from core.database.state_validator import (
    StateValidator
)

from core.database.delete_validator import (
    DeleteValidator
)

from core.database.logger import Logger

from auth.guards import Guards

from auth.session_manager import (
    SessionManager
)

from core.security.permissions import (
    Permissions
)

from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)

class BaseCRUD:


    def __init__(self, session):

        self.session = session


    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(
        self,
        model,
        data
    ):
        Guards.admin_required()

        try:

            Validators.validate_required_fields(
                model,
                data
            )

            Validators.validate_unique(
                self.session,
                model,
                data
            )

            TypeValidator.validate(
                model,
                data
            )

            StateValidator.validate(data)

            ForeignKeyValidator.validate(
                self.session,
                model,
                data
            )

            instance = model(**data)

            self.session.add(instance)

            self.session.commit()

            self.session.refresh(instance)

            Logger.info(
                f"Registro creado en {model.__tablename__}"
            )

            return Response.success(
                "Registro creado correctamente",
                Serializer.to_dict(instance)
            )

        except Exception as e:

            self.session.rollback()

            Logger.error(str(e))

            return Response.error(str(e))


    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        model,
        instance_id,
        data
    ):
        Guards.admin_required()

        try:

            instance = self.session.get(
                model,
                instance_id
            )

            if not instance:

                raise RecordNotFound(
                    "Registro no encontrado"
                )

            Validators.validate_unique(
                self.session,
                model,
                data,
                instance_id
            )

            TypeValidator.validate(
                model,
                data
            )

            StateValidator.validate(data)

            ForeignKeyValidator.validate(
                self.session,
                model,
                data
            )

            for key, value in data.items():

                if hasattr(instance, key):

                    setattr(
                        instance,
                        key,
                        value
                    )

            self.session.commit()

            self.session.refresh(instance)

            Logger.info(
                f"Registro actualizado en {model.__tablename__}"
            )

            return Response.success(
                "Registro actualizado correctamente",
                Serializer.to_dict(instance)
            )

        except Exception as e:

            self.session.rollback()

            Logger.error(str(e))

            return Response.error(str(e))


    # ---------------------------------------------------------
    # GET ALL
    # ---------------------------------------------------------

    def get_all(
        self,
        model,
        include_inactive=False,
        filters=None,
        search=None
    ):
        Guards.auth_required()

        try:

            query = self.session.query(model)

            user = SessionManager.current_user()

            can_view_inactive = (
                Permissions.can_view_inactive(user)
            )

            if (
                issubclass(model, SoftDeleteMixin)
                and
                (
                    not include_inactive
                    or
                    not can_view_inactive
                )
            ):

                query = query.filter(
                    model.estado == "ACTIVO"
                )

            query = QueryBuilder.apply_filters(
                query,
                model,
                filters
            )

            query = QueryBuilder.apply_search(
                query,
                model,
                search
            )

            data = query.all()

            return Response.success(
                data=Serializer.to_dict_list(
                    data,
                    relationships=True,
                    depth=3
                )
            )

        except Exception as e:

            return Response.error(str(e))


    # ---------------------------------------------------------
    # GET BY ID
    # ---------------------------------------------------------

    def get_by_id(
        self,
        model,
        instance_id
    ):

        try:

            instance = self.session.get(
                model,
                instance_id
            )

            if not instance:

                raise RecordNotFound(
                    "Registro no encontrado"
                )

            return Response.success(
                data=Serializer.to_dict(
                    instance,
                    relationships=True
                )
            )

        except Exception as e:

            return Response.error(str(e))


    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------

    def search(
        self,
        model,
        search
    ):

        return self.get_all(
            model,
            search=search
        )


    # ---------------------------------------------------------
    # SEARCH BY COLUMNS
    # ---------------------------------------------------------

    def search_columns(
        self,
        model,
        query_text,
        columns=None,
        include_inactive=False,
        filters=None
    ):

        Guards.auth_required()

        try:

            query = self.session.query(model)

            user = SessionManager.current_user()

            can_view_inactive = (
                Permissions.can_view_inactive(user)
            )

            if (
                issubclass(model, SoftDeleteMixin)
                and
                (
                    not include_inactive
                    or
                    not can_view_inactive
                )
            ):

                query = query.filter(
                    model.estado == "ACTIVO"
                )

            query = QueryBuilder.apply_filters(
                query,
                model,
                filters
            )

            # If specific columns provided, build OR conditions
            if columns:

                conditions = []

                for col_name in columns:

                    if hasattr(model, col_name):

                        col_attr = getattr(model, col_name)

                        try:
                            conditions.append(
                                col_attr.ilike(f"%{query_text}%")
                            )
                        except Exception:
                            # skip columns that don't support ilike
                            pass

                if conditions:

                    query = query.filter(
                        or_(*conditions)
                    )

            else:

                # fallback to generic search across varchar columns
                query = QueryBuilder.apply_search(
                    query,
                    model,
                    query_text
                )

            data = query.all()

            return Response.success(
                data=Serializer.to_dict_list(
                    data,
                    relationships=True,
                    depth=3
                )
            )

        except Exception as e:

            return Response.error(str(e))


    # ---------------------------------------------------------
    # PAGINATE
    # ---------------------------------------------------------

    def paginate(
        self,
        model,
        page=1,
        per_page=10,
        include_inactive=False
    ):

        try:

            query = self.session.query(model)

            if (
                issubclass(model, SoftDeleteMixin)
                and
                not include_inactive
            ):

                query = query.filter(
                    model.estado == "ACTIVO"
                )

            total = query.count()

            data = query.offset(
                (page - 1) * per_page
            ).limit(
                per_page
            ).all()

            return Response.success(
                data={
                    "items": data,
                    "total": total,
                    "page": page,
                    "per_page": per_page
                }
            )

        except Exception as e:

            return Response.error(str(e))


    # ---------------------------------------------------------
    # SOFT DELETE
    # ---------------------------------------------------------

    def soft_delete(
        self,
        model,
        instance_id
    ):
        Guards.admin_required()

        try:

            instance = self.session.get(
                model,
                instance_id
            )

            if not instance:

                raise RecordNotFound(
                    "Registro no encontrado"
                )

            if not isinstance(instance, SoftDeleteMixin):

                return Response.error(
                    "El modelo no soporta soft delete"
                )

            instance.estado = (
                SoftDeleteMixin.INACTIVE_STATE
            )

            self.session.commit()

            return Response.success(
                "Registro desactivado correctamente"
            )

        except Exception as e:

            self.session.rollback()

            return Response.error(str(e))


    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        model,
        instance_id
    ):

        try:

            instance = self.session.get(
                model,
                instance_id
            )

            if not instance:

                raise RecordNotFound(
                    "Registro no encontrado"
                )

            if not isinstance(instance, SoftDeleteMixin):

                return Response.error(
                    "El modelo no soporta restore"
                )

            instance.estado = (
                SoftDeleteMixin.ACTIVE_STATE
            )

            self.session.commit()

            return Response.success(
                "Registro restaurado correctamente"
            )

        except Exception as e:

            self.session.rollback()

            return Response.error(str(e))


    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        model,
        instance_id
    ):
        Guards.admin_required()

        try:

            instance = self.session.get(
                model,
                instance_id
            )

            if not instance:

                raise RecordNotFound(
                    "Registro no encontrado"
                )

            DeleteValidator.validate(instance)

            self.session.delete(instance)

            self.session.commit()

            Logger.info(
                f"Registro eliminado de {model.__tablename__}"
            )

            return Response.success(
                "Registro eliminado correctamente"
            )

        except Exception as e:

            self.session.rollback()

            Logger.error(str(e))

            return Response.error(str(e))


    # ---------------------------------------------------------
    # CLOSE
    # ---------------------------------------------------------

    def close(self):

        self.session.close()