from database.models import Preparacion

from core.repositories.base_repository import (
    BaseRepository
)


class PreparacionRepository(
    BaseRepository
):


    def __init__(
        self,
        session
    ):

        super().__init__(
            Preparacion,
            session
        )