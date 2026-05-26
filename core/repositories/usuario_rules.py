from core.database.exceptions import (
    ValidationError
)


class UsuarioRules:


    @staticmethod
    def validate_password(password):

        if len(password) < 6:

            raise ValidationError(
                "La contraseña debe tener mínimo 6 caracteres"
            )


    @staticmethod
    def validate_username(username):

        if " " in username:

            raise ValidationError(
                "El usuario no puede contener espacios"
            )