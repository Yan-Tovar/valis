from database.connection import SessionLocal
from database.models import Usuario

from auth.session_manager import (
    SessionManager
)

from auth.auth_exceptions import (
    InvalidCredentials,
    InactiveUser
)

from core.security.password_hasher import (
    PasswordHasher
)


class AuthService:


    def __init__(self):

        self.session = SessionLocal()


    # ---------------------------------------------------------
    # LOGIN
    # ---------------------------------------------------------

    def login(
        self,
        nombre_usuario,
        password
    ):

        user = self.session.query(
            Usuario
        ).filter(
            Usuario.nombre_usuario == nombre_usuario
        ).first()

        if not user:

            raise InvalidCredentials(
                "Usuario o contraseña incorrectos"
            )

        if user.estado != "ACTIVO":

            raise InactiveUser(
                "Usuario inactivo"
            )

        valid_password = (
            PasswordHasher.verify_password(
                password,
                user.password
            )
        )

        if not valid_password:

            raise InvalidCredentials(
                "Usuario o contraseña incorrectos"
            )

        SessionManager.login(user)

        return user


    # ---------------------------------------------------------
    # LOGOUT
    # ---------------------------------------------------------

    def logout(self):

        SessionManager.logout()


    # ---------------------------------------------------------
    # CURRENT USER
    # ---------------------------------------------------------

    def current_user(self):

        return SessionManager.current_user()