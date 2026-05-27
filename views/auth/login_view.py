import flet as ft

from views.auth.login_controller import (
    LoginController
)

from views.auth.components.login_left_panel import (
    LoginLeftPanel
)

from views.auth.components.login_right_panel import (
    LoginRightPanel
)


class LoginView:

    def __init__(
        self,
        page: ft.Page
    ):

        self.page = page

        self.controller = (
            LoginController(page)
        )

    # =================================================
    # BUILD
    # =================================================

    def build(self):

        is_mobile = self.page.width < 900
        page_width = self.page.width

        # =============================================
        # MOBILE
        # =============================================

        if is_mobile:

            return ft.Container(

                expand=True,

                bgcolor="white",

                content=ft.Column(

                    expand=True,

                    scroll=ft.ScrollMode.AUTO,

                    spacing=0,

                    controls=[

                        LoginLeftPanel(
                            mobile=True,
                            width=page_width
                        ),

                        LoginRightPanel(
                            on_login=(
                                self.controller.login
                            ),
                            mobile=True
                        )
                    ]
                )
            )

        # =============================================
        # DESKTOP
        # =============================================

        return ft.Container(

            expand=True,

            bgcolor="white",

            content=ft.Row(

                expand=True,

                spacing=0,

                controls=[

                    LoginLeftPanel(
                        width=page_width
                    ),

                    LoginRightPanel(
                        on_login=(
                            self.controller.login
                        )
                    )
                ]
            )
        )