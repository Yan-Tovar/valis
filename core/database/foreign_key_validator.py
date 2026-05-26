from sqlalchemy.inspection import inspect

from core.database.exceptions import ValidationError


class ForeignKeyValidator:


    @staticmethod
    def validate(
        session,
        model,
        data
    ):

        mapper = inspect(model)

        for column in mapper.columns:

            foreign_keys = list(column.foreign_keys)

            if not foreign_keys:
                continue

            value = data.get(column.name)

            if value is None:
                continue

            foreign_key = foreign_keys[0]

            target_table = foreign_key.column.table.name

            target_column = foreign_key.column.name

            target_model = None

            for mapper_model in model.registry.mappers:

                cls = mapper_model.class_

                if cls.__tablename__ == target_table:

                    target_model = cls
                    break

            if not target_model:
                continue

            exists = session.query(target_model).filter(
                getattr(
                    target_model,
                    target_column
                ) == value
            ).first()

            if not exists:

                raise ValidationError(
                    f"No existe relación válida para '{column.name}'"
                )