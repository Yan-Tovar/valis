from database.models import (
    ListaPreparacionPreparacion
)

from core.repositories.base_repository import (
    BaseRepository
)


class ListaPreparacionPreparacionRepository(
    BaseRepository
):


    def __init__(
        self,
        session
    ):

        super().__init__(
            ListaPreparacionPreparacion,
            session
        )