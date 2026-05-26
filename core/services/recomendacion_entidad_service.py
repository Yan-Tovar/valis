from auth.session_manager import SessionManager

from core.security.permissions import (
    Permissions
)

from core.services.base_service import (
    BaseService
)

from core.repositories.recomendacion_entidad_repository import (
    RecomendacionEntidadRepository
)


class RecomendacionEntidadService(
    BaseService
):


    def __init__(self):

        super().__init__()

        self.repository = (
            RecomendacionEntidadRepository(
                self.session
            )
        )

    # -------------------------------------------------
    # GET ALL
    # -------------------------------------------------

    def get_all(self):

        user = SessionManager.current_user()

        include_inactive = (
            Permissions.can_view_inactive(user)
        )

        return self.repository.get_all(
            include_inactive=include_inactive
        )

    # -------------------------------------------------
    # CREATE
    # -------------------------------------------------

    def create(
        self,
        data
    ):

        if data.get("entidad_id"):

            data["entidad_id"] = int(
                data["entidad_id"]
            )

        return self.repository.create(
            data
        )

    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    def update(
        self,
        entity_id,
        data
    ):

        if data.get("entidad_id"):

            data["entidad_id"] = int(
                data["entidad_id"]
            )

        return self.repository.update(
            entity_id,
            data
        )

    # -------------------------------------------------
    # DELETE
    # -------------------------------------------------

    def soft_delete(
        self,
        entity_id
    ):

        return self.repository.soft_delete(
            entity_id
        )

    # -------------------------------------------------
    # RESTORE
    # -------------------------------------------------

    def restore(
        self,
        entity_id
    ):

        return self.repository.restore(
            entity_id
        )

    # -------------------------------------------------
    # HARD DELETE
    # -------------------------------------------------

    def hard_delete(
        self,
        entity_id
    ):

        return self.repository.hard_delete(
            entity_id
        )