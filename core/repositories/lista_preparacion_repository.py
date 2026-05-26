from database.models import ListaPreparacion

from core.repositories.base_repository import (
    BaseRepository
)


class ListaPreparacionRepository(
    BaseRepository
):

    def __init__(
        self,
        session
    ):

        super().__init__(
            ListaPreparacion,
            session
        )