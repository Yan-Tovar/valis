from database.models import Usuario

from core.repositories.base_repository import (
    BaseRepository
)


class UsuarioRepository(BaseRepository):


    def __init__(
        self,
        session
    ):

        super().__init__(
            Usuario,
            session
        )


    def get_by_username(
        self,
        username
    ):

        return self.session.query(
            Usuario
        ).filter(
            Usuario.nombre_usuario == username
        ).first()