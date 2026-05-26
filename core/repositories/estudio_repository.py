from database.models import Estudio

from core.repositories.base_repository import (
    BaseRepository
)


class EstudioRepository(BaseRepository):


    def __init__(
        self,
        session
    ):

        super().__init__(
            Estudio,
            session
        )


    # ---------------------------------------------------------
    # CUSTOM QUERIES
    # ---------------------------------------------------------

    def get_by_codigo(
        self,
        codigo
    ):

        return self.session.query(
            Estudio
        ).filter(
            Estudio.codigo_cups == codigo
        ).first()