from core.crud_engine.generic_crud_view import (
    GenericCrudView
)


class EstudiosSalasView:

    title = "Estudios - Salas"

    def __init__(
        self,
        page
    ):

        self.page = page

    def build(self):

        return GenericCrudView(

            page=self.page,

            module="estudios_salas"

        ).build()