class SalaRules:


    @staticmethod
    def validate_codigo(codigo):

        if not codigo:

            raise ValueError(
                "El código de sala es obligatorio"
            )