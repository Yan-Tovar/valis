from core.crud_engine.generic_crud_view import (
    GenericCrudView
)


class ListaPreparacionesPreparacionesView:

    title = "Listas - Preparaciones"

    def __init__(
        self,
        page
    ):

        self.page = page

    def build(self):

        return GenericCrudView(

            page=self.page,

            module="lista_preparaciones_preparaciones"

        ).build()