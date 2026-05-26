from database.models import Sala

from core.repositories.base_repository import (
    BaseRepository
)


class SalaRepository(BaseRepository):


    def __init__(
        self,
        session
    ):

        super().__init__(
            Sala,
            session
        )