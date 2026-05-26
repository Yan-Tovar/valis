from database.models import EntidadContrato

from core.repositories.base_repository import (
    BaseRepository
)


class EntidadContratoRepository(
    BaseRepository
):


    def __init__(
        self,
        session
    ):

        super().__init__(
            EntidadContrato,
            session
        )