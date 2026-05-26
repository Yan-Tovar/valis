from auth.session_manager import (
    SessionManager
)

from core.navigation.menu_registry import (
    MENU_REGISTRY
)

from core.security.permissions import (
    Permissions
)


class RouteGuard:


    @staticmethod
    def can_access(route):

        user = SessionManager.current_user()

        # -----------------------------------------
        # PUBLIC ROUTES
        # -----------------------------------------

        public_routes = [
            "/",
            "/login"
        ]

        if route in public_routes:

            return True

        # -----------------------------------------
        # REQUIRE LOGIN
        # -----------------------------------------

        if not user:

            return False

        # -----------------------------------------
        # ADMIN-ONLY ROUTES
        # -----------------------------------------

        admin_routes = [
            item["route"]
            for item in MENU_REGISTRY
            if item["roles"] == [Permissions.ADMIN]
        ]

        if route in admin_routes:

            return Permissions.is_admin(user)

        return True