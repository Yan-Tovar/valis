class NavigationService:

    _page = None

    @classmethod
    def initialize(
        cls,
        page
    ):

        cls._page = page

    @classmethod
    def navigate(
        cls,
        route
    ):

        cls._page.go(route)

    @classmethod
    def logout(cls):

        from auth.session_manager import (
            SessionManager
        )

        SessionManager.logout()

        cls._page.go("/login")