from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)

from core.database.exceptions import (
    ValidationError
)


class StateValidator:


    VALID_STATES = [

        SoftDeleteMixin.ACTIVE_STATE,

        SoftDeleteMixin.INACTIVE_STATE
    ]


    @classmethod
    def validate(
        cls,
        data
    ):

        estado = data.get("estado")

        if estado is None:
            return

        if estado not in cls.VALID_STATES:

            raise ValidationError(
                "Estado inválido"
            )