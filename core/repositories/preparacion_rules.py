class PreparacionRules:


    @staticmethod
    def validate_codigo(codigo):

        if not codigo:

            raise ValueError(
                "El código de preparación es obligatorio"
            )