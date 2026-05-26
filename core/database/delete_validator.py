from sqlalchemy.inspection import inspect

from core.database.exceptions import (
    RelatedRecordsError
)


class DeleteValidator:


    EXCLUDED_RELATIONS = [
        "created_by",
        "updated_by"
    ]


    @classmethod
    def validate(
        cls,
        instance
    ):

        mapper = inspect(instance.__class__)

        for relation in mapper.relationships:

            if relation.key in cls.EXCLUDED_RELATIONS:
                continue

            # -------------------------------------------------
            # SOLO VALIDAR RELACIONES HIJAS
            # -------------------------------------------------

            if not relation.uselist:
                continue

            related = getattr(
                instance,
                relation.key
            )

            if related and len(related) > 0:

                raise RelatedRecordsError(

                    f"No se puede eliminar porque "
                    f"tiene relación '{relation.key}'"
                )