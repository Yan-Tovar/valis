import flet as ft

from core.layouts.app_shell import AppShell

from core.router.routes import (
    Routes
)

from core.router.route_manager import (
    RouteManager
)


class AppRouter:

    # =================================================
    # INIT
    # =================================================

    def __init__(
        self,
        page: ft.Page
    ):

        self.page = page

        # =============================================
        # SHELL PERSISTENTE
        # =============================================

        self.shell = AppShell(page)

        # =============================================
        # ERP VIEW ÚNICA
        # =============================================

        self.erp_view = ft.View(

            route="/app",

            padding=0,

            spacing=0,

            controls=[
                self.shell
            ]
        )

        # =============================================
        # PUBLIC ROUTES
        # =============================================

        self.public_routes = [

            Routes.SPLASH,

            Routes.LOGIN
        ]

    # =================================================
    # ROUTE CHANGE
    # =================================================

    def route_change(
        self,
        route
    ):

        current_route = self.page.route

        # =============================================
        # GET VIEW
        # =============================================

        view = RouteManager.get_view(

            self.page,

            current_route
        )

        # =============================================
        # ROUTE NOT FOUND
        # =============================================

        if not view:
            return

        # =================================================
        # PUBLIC VIEWS
        # =================================================

        if current_route in self.public_routes:

            self.load_public_view(

                route=current_route,

                content=view.build()
            )

        # =================================================
        # PRIVATE ERP VIEWS
        # =================================================

        else:

            self.load_private_view(view)

        # =================================================
        # UPDATE
        # =================================================

        self.page.update()

    # =================================================
    # LOAD PUBLIC VIEW
    # =================================================

    def load_public_view(
        self,
        route,
        content
    ):

        self.page.views.clear()

        self.page.views.append(

            ft.View(

                route=route,

                padding=0,

                spacing=0,

                controls=[
                    content
                ]
            )
        )

    # =================================================
    # LOAD PRIVATE VIEW
    # =================================================

    def load_private_view(
        self,
        view
    ):

        # =============================================
        # UPDATE SHELL
        # =============================================

        self.shell.set_view(

            title=view.title,

            content=view.build()
        )

        # =============================================
        # LOAD ERP VIEW ONCE
        # =============================================

        if self.erp_view not in self.page.views:

            self.page.views.clear()

            self.page.views.append(
                self.erp_view
            )