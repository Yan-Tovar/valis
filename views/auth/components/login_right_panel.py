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
        on_login,
        mobile=False
    ):

        super().__init__()

        self.expand = not mobile

        self.bgcolor = AppColors.PRIMARY_LIGHT

        self.padding = 20

        self.alignment = ft.alignment.center

        self.content = ft.Container(

            alignment=ft.alignment.center,

            content=LoginCard(
                on_login,
                mobile=mobile
            )
        )