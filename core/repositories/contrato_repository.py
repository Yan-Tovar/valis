from database.models import Contrato

from core.repositories.base_repository import (
    BaseRepository
)


class ContratoRepository(BaseRepository):


    def __init__(
        self,
        session
    ):

        super().__init__(
            Contrato,
            session
        )