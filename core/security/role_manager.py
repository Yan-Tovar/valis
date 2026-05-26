from core.database.exceptions import (
    ValidationError
)

from core.security.permissions import (
    Permissions
)


class RoleManager:


    VALID_ROLES = [
        Permissions.ADMIN,
        Permissions.LECTOR
    ]


    @classmethod
    def validate_role(
        cls,
        role
    ):

        if role not in cls.VALID_ROLES:

            raise ValidationError(
                "Rol inválido"
            )