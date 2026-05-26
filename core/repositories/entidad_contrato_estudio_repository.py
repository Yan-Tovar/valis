from database.models import (
    EntidadContratoEstudio
)

from core.repositories.base_repository import (
    BaseRepository
)


class EntidadContratoEstudioRepository(
    BaseRepository
):


    def __init__(
        self,
        session
    ):

        super().__init__(
            EntidadContratoEstudio,
            session
        )