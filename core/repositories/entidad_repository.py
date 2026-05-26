from database.models import Entidad

from core.repositories.base_repository import (
    BaseRepository
)


class EntidadRepository(BaseRepository):


    def __init__(
        self,
        session
    ):

        super().__init__(
            Entidad,
            session
        )