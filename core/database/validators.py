from sqlalchemy.inspection import inspect

from core.database.exceptions import (
    DuplicateRecordError,
    ValidationError
)


class Validators:


    @staticmethod
    def validate_required_fields(model, data):

        mapper = inspect(model)

        for column in mapper.columns:

            if (
                not column.nullable
                and
                not column.primary_key
                and
                column.default is None
            ):

                if column.name not in data:

                    raise ValidationError(
                        f"El campo '{column.name}' es obligatorio"
                    )


    @staticmethod
    def validate_unique(
        session,
        model,
        data,
        instance_id=None
    ):

        mapper = inspect(model)

        for column in mapper.columns:

            if column.unique:

                value = data.get(column.name)

                if value is None:
                    continue

                query = session.query(model).filter(
                    getattr(model, column.name) == value
                )

                if instance_id:

                    query = query.filter(
                        model.id != instance_id
                    )

                exists = query.first()

                if exists:

                    raise DuplicateRecordError(
                        f"El valor '{value}' ya existe"
                    )