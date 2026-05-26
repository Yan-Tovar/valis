from database.models import EstudioSala

from core.repositories.base_repository import (
    BaseRepository
)

class EstudioSalaRepository(
    BaseRepository
):


    def __init__(
        self,
        session
    ):

        super().__init__(
            EstudioSala,
            session
        )