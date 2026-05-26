from core.crud_engine.generic_crud_view import (
    GenericCrudView
)


class RecomendacionesEstudioView:

    title = "Recomendaciones - Estudios"

    def __init__(
        self,
        page
    ):

        self.page = page

    def build(self):

        return GenericCrudView(

            page=self.page,

            module="recomendaciones_estudio"

        ).build()