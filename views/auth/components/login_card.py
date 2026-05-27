import flet as ft

from core.theme.colors import (
    AppColors
)

from views.auth.login_form import (
    LoginForm
)


class LoginCard(ft.Container):

    def __init__(
        self,
        on_login,
        mobile=False
    ):

        super().__init__()

        self.width = 360 if mobile else 420

        self.padding = 25 if mobile else 35

        self.bgcolor = AppColors.WHITE

        self.border_radius = 24

        self.border = ft.border.all(
            1,
            AppColors.PRIMARY
        )

        self.shadow = ft.BoxShadow(
            blur_radius=20,
            spread_radius=1,
            color="black12"
        )

        self.content = ft.Column(

            tight=True,

            spacing=25,

            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

            controls=[

                # =====================================
                # TITLE
                # =====================================

                ft.Column(

                    spacing=5,

                    horizontal_alignment=(
                        ft.CrossAxisAlignment.CENTER
                    ),

                    controls=[

                        ft.Text(

                            "Bienvenido",

                            size=24 if mobile else 28,

                            weight=ft.FontWeight.BOLD,

                            color=AppColors.BLACK
                        ),

                        ft.Text(

                            "Ingresa tus credenciales",

                            size=13 if mobile else 14,

                            color=AppColors.DARK_GRAY
                        )
                    ]
                ),

                # =====================================
                # FORM
                # =====================================

                LoginForm(
                    on_login
                )
            ]
        )