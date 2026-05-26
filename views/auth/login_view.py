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


    # -------------------------------------------------
    # BUILD
    # -------------------------------------------------

    def build(self):

        return ft.Container(

            expand=True,

            content=ft.Row(

                expand=True,

                spacing=0,

                controls=[

                    # LEFT

                    LoginLeftPanel(),

                    # RIGHT

                    LoginRightPanel(

                        on_login=(
                            self.controller.login
                        )
                    )
                ]
            )
        )