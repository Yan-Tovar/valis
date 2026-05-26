from core.crud_engine.generic_crud_view import (
    GenericCrudView
)


class EstudiosView:

    title = "Estudios"

    def __init__(
        self,
        page
    ):

        self.page = page

    # ---------------------------------------------------------
    # BUILD
    # ---------------------------------------------------------

    def build(self):

        return GenericCrudView(

            page=self.page,

            module="estudios"

        ).build()