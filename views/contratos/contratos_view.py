from core.crud_engine.generic_crud_view import (
    GenericCrudView
)


class ContratosView:

    title = "Contratos"

    def __init__(
        self,
        page
    ):

        self.page = page

    def build(self):

        return GenericCrudView(

            page=self.page,

            module="contratos"

        ).build()