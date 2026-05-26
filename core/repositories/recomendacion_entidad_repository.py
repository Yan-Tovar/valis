from database.models import RecomendacionEntidad

from core.repositories.base_repository import (
    BaseRepository
)


class RecomendacionEntidadRepository(
    BaseRepository
):


    def __init__(self, session):

        super().__init__(
            RecomendacionEntidad,
            session
        )
