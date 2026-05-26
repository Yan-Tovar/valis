import flet as ft

from core.theme.colors import (
    AppColors
)

from views.auth.components.login_card import (
    LoginCard
)


class LoginRightPanel(ft.Container):


    def __init__(
        self,
        on_login
    ):

        super().__init__()

        self.expand = True

        self.bgcolor = AppColors.PRIMARY_LIGHT

        self.content = ft.Column(

            expand=True,

            alignment=ft.MainAxisAlignment.CENTER,

            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

            controls=[

                LoginCard(
                    on_login
                )
            ]
        )