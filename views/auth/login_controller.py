from auth.session_manager import (
    SessionManager
)

from core.router.navigation_service import (
    NavigationService
)

from core.router.routes import (
    Routes
)

from core.components.alerts.snackbar import (
    Snackbar
)

from auth.auth_service import (
    AuthService
)

from auth.auth_exceptions import (

    InvalidCredentials,

    InactiveUser
)


class LoginController:

    # =================================================
    # INIT
    # =================================================

    def __init__(
        self,
        page
    ):

        self.page = page

        self.auth_service = (
            AuthService()
        )

    # =================================================
    # LOGIN
    # =================================================

    def login(

        self,

        nombre_usuario,

        password
    ):

        try:

            # =========================================
            # LOGIN
            # =========================================

            self.auth_service.login(

                nombre_usuario=nombre_usuario,

                password=password
            )

            # =========================================
            # CURRENT USER
            # =========================================

            user = SessionManager.current_user()

            user_role = (
                user["rol"]
            )

            # =========================================
            # SUCCESS
            # =========================================

            Snackbar.show(

                self.page,

                "Bienvenido al sistema",

                success=True
            )

            # =========================================
            # REDIRECT
            # =========================================

            if user_role == "ADMIN":

                NavigationService.navigate(
                    Routes.DASHBOARD
                )

            else:

                NavigationService.navigate(
                    Routes.CONSULTA
                )

        # =============================================
        # INVALID CREDENTIALS
        # =============================================

        except InvalidCredentials as e:

            Snackbar.show(

                self.page,

                str(e),

                success=False
            )

        # =============================================
        # INACTIVE USER
        # =============================================

        except InactiveUser as e:

            Snackbar.show(

                self.page,

                str(e),

                success=False
            )

        # =============================================
        # UNKNOWN ERROR
        # =============================================

        except Exception as e:

            Snackbar.show(

                self.page,

                f"Error inesperado: {str(e)}",

                success=False
            )