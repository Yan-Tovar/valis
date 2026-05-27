import flet as ft

from core.router.app_router import AppRouter
from core.router.navigation_service import NavigationService
from core.router.routes import Routes
from core.theme.theme import app_theme


def main(page: ft.Page):

    # =================================================
    # WINDOW CONFIGURATION
    # =================================================

    page.window.visible = False
    page.window.resizable = True
    page.window.maximizable = True
    page.window.minimizable = True
    page.window.maximized = True

    # =================================================
    # PAGE SETUP
    # =================================================

    page.title = "Valis"
    page.theme = app_theme()
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "white"

    # =================================================
    # CLEAN UPDATE
    # =================================================

    page.update()

    # =================================================
    # NAVIGATION SETUP
    # =================================================

    NavigationService.initialize(page)
    router = AppRouter(page)
    page.on_route_change = router.route_change

    # =================================================
    # SHOW WINDOW WITH CONTENT
    # =================================================

    page.go(Routes.SPLASH)
    page.window.visible = True
    page.update()


ft.app(target=main)