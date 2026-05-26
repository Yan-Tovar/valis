import flet as ft

from database.init import (
    init_database,
    create_admin
)

from core.router.app_router import AppRouter
from core.router.navigation_service import NavigationService
from core.theme.theme import app_theme
from core.router.routes import Routes


def main(page: ft.Page):

    # -------------------------------------------------
    # INIT DB (SIEMPRE SE VERIFICA BIEN)
    # -------------------------------------------------

    init_database()
    create_admin()

    # -------------------------------------------------
    # APP
    # -------------------------------------------------

    page.title = "Valis"
    page.theme = app_theme()
    page.padding = 0
    page.spacing = 0
    page.window.maximized = True

    NavigationService.initialize(page)

    router = AppRouter(page)
    page.on_route_change = router.route_change

    page.go(Routes.SPLASH)


ft.app(target=main)