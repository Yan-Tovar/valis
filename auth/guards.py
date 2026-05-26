from auth.session_manager import (
    SessionManager
)

from auth.auth_exceptions import (
    Unauthorized
)

from core.security.permissions import (
    Permissions
)


class Guards:


    @staticmethod
    def auth_required():

        if not SessionManager.is_authenticated():

            raise Unauthorized(
                "Debe iniciar sesión"
            )


    @staticmethod
    def admin_required():

        Guards.auth_required()

        user = SessionManager.current_user()

        if not Permissions.is_admin(user):

            raise Unauthorized(
                "Permisos insuficientes"
            )