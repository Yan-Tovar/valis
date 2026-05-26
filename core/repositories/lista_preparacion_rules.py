class ListaPreparacionRules:


    @staticmethod
    def validate_nombre(nombre):

        if not nombre:

            raise ValueError(
                "El nombre es obligatorio"
            )