from database.models import RecomendacionEstudio

from core.repositories.base_repository import (
    BaseRepository
)


class RecomendacionEstudioRepository(
    BaseRepository
):


    def __init__(self, session):

        super().__init__(
            RecomendacionEstudio,
            session
        )