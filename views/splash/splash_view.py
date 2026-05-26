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

        self.controller = SplashController(
            page
        )


    # --------------------------------------------------
    # BUILD
    # --------------------------------------------------

    def build(self):

        # START FLOW

        self.controller.start()

        return ft.Container(

            expand=True,

            bgcolor=AppColors.WHITE,

            alignment=ft.alignment.center,

            content=ft.Stack(

                expand=True,

                controls=[

                    # -------------------------------------
                    # BACKGROUND
                    # -------------------------------------

                    SplashBackground(),

                    # -------------------------------------
                    # LOGO
                    # -------------------------------------

                    ft.Container(

                        alignment=ft.alignment.center,

                        margin=ft.margin.only(top=500),

                        content=AnimatedLogo(
                            self.page
                        )
                    )
                ]
            )
        )