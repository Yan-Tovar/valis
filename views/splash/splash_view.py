import flet as ft

from core.theme.colors import AppColors

from views.splash.splash_controller import (
    SplashController
)

from views.splash.components.animated_logo import (
    AnimatedLogo
)

from views.splash.components.splash_background import (
    SplashBackground
)


class SplashView:


    def __init__(
        self,
        page: ft.Page
    ):

        self.page = page

        self.started = False

        self.controller = SplashController(
            page
        )

    # ==================================================
    # BUILD
    # ==================================================

    def build(self):

        if not self.started:

            self.started = True

            self.controller.start()

        return ft.Container(

            expand=True,

            bgcolor=AppColors.WHITE,

            alignment=ft.alignment.center,

            content=ft.Stack(

                expand=True,

                controls=[

                    # ======================================
                    # BACKGROUND
                    # ======================================

                    SplashBackground(),

                    # ======================================
                    # LOGO CONTENT
                    # ======================================

                    ft.Container(

                        expand=True,

                        alignment=ft.alignment.center,

                        content=AnimatedLogo(
                            self.page
                        )
                    )
                ]
            )
        )