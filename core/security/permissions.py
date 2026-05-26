from core.database.exceptions import (
    ValidationError
)


class Permissions:


    ADMIN = "ADMIN"

    LECTOR = "LECTOR"


    @classmethod
    def _normalize_role(
        cls,
        user
    ):

        if not user or "rol" not in user or not user["rol"]:
            return None

        return user["rol"].strip().upper()


    # ---------------------------------------------------------
    # ROLE CHECKS
    # ---------------------------------------------------------

    @classmethod
    def is_admin(
        cls,
        user
    ):

        return cls._normalize_role(user) == cls.ADMIN


    @classmethod
    def is_lector(
        cls,
        user
    ):

        return cls._normalize_role(user) == cls.LECTOR


    # ---------------------------------------------------------
    # ACCESS CONTROL
    # ---------------------------------------------------------

    @classmethod
    def can_edit(
        cls,
        user
    ):

        return cls.is_admin(user)


    @classmethod
    def can_delete(
        cls,
        user
    ):

        return cls.is_admin(user)


    @classmethod
    def can_view_inactive(
        cls,
        user
    ):

        return cls.is_admin(user)


    # ---------------------------------------------------------
    # VALIDATORS
    # ---------------------------------------------------------

    @classmethod
    def validate_admin(
        cls,
        user
    ):

        if not cls.is_admin(user):

            raise ValidationError(
                "No tiene permisos suficientes"
            )