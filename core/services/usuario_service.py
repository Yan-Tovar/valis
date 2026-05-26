from auth.session_manager import SessionManager

from core.security.permissions import (
    Permissions
)

from core.services.base_service import (
    BaseService
)

from core.repositories.usuario_repository import (
    UsuarioRepository
)

from core.repositories.usuario_rules import (
    UsuarioRules
)

from core.security.password_hasher import (
    PasswordHasher
)

from core.security.role_manager import (
    RoleManager
)


class UsuarioService(BaseService):


    def __init__(self):

        super().__init__()

        self.repository = (
            UsuarioRepository(
                self.session
            )
        )

    # ---------------------------------------------------------
    # GET ALL
    # ---------------------------------------------------------

    def get_all(self):

        user = SessionManager.current_user()

        include_inactive = (
            Permissions.can_view_inactive(user)
        )

        return self.repository.get_all(
            include_inactive=include_inactive
        )

    # ---------------------------------------------------------
    # GET BY ID
    # ---------------------------------------------------------

    def get_by_id(
        self,
        user_id
    ):

        return self.repository.get_by_id(
            user_id
        )

    # ---------------------------------------------------------
    # CREATE USER
    # ---------------------------------------------------------

    def create(
        self,
        data
    ):

        UsuarioRules.validate_username(
            data["nombre_usuario"]
        )

        UsuarioRules.validate_password(
            data["password"]
        )

        RoleManager.validate_role(
            data["rol"]
        )

        data["password"] = (
            PasswordHasher.hash_password(
                data["password"]
            )
        )

        return self.repository.create(
            data
        )

    # ---------------------------------------------------------
    # UPDATE USER
    # ---------------------------------------------------------

    def update(
        self,
        user_id,
        data
    ):

        if "rol" in data:

            RoleManager.validate_role(
                data["rol"]
            )

        if "password" in data:

            UsuarioRules.validate_password(
                data["password"]
            )

            data["password"] = (
                PasswordHasher.hash_password(
                    data["password"]
                )
            )

        return self.repository.update(
            user_id,
            data
        )

    # ---------------------------------------------------------
    # SOFT DELETE
    # ---------------------------------------------------------

    def soft_delete(
        self,
        user_id
    ):

        return self.repository.soft_delete(
            user_id
        )

    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        user_id
    ):

        return self.repository.restore(
            user_id
        )

    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        user_id
    ):

        return self.repository.hard_delete(
            user_id
        )