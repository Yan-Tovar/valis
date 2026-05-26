from core.database.exceptions import (
    ValidationError
)


class EstudioRules:


    @staticmethod
    def validate_sigla(sigla):

        if sigla is None:
            return

        if len(sigla) > 10:

            raise ValidationError(
                "La sigla no puede superar 10 caracteres"
            )