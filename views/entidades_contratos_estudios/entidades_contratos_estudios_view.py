from core.crud_engine.generic_crud_view import (
    GenericCrudView
)


class EntidadesContratosEstudiosView:

    title = "Contratos - Estudios"

    def __init__(
        self,
        page
    ):

        self.page = page

    def build(self):

        return GenericCrudView(

            page=self.page,

            module="entidades_contratos_estudios"

        ).build()