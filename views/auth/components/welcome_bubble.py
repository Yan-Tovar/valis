import flet as ft

from core.theme.colors import (
    AppColors
)


class WelcomeBubble(ft.Container):


    def __init__(self):

        super().__init__()

        self.left = 355

        self.bottom = 405

        self.padding = ft.padding.symmetric(
            horizontal=14,
            vertical=10
        )

        self.bgcolor = AppColors.WHITE

        self.border = ft.border.all(
            2,
            AppColors.PRIMARY_LIGHT
        )

        self.border_radius = 18

        self.shadow = ft.BoxShadow(
            blur_radius=10,
            spread_radius=1,
            color="black12"
        )

        self.content = ft.Column(

            tight=True,

            spacing=0,

            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

            controls=[

                ft.Text(

                    "Soy Valis,",

                    size=14,

                    weight=ft.FontWeight.W_600,

                    color=AppColors.PRIMARY
                ),

                ft.Text(

                    "¿Quién eres tú?",

                    size=14,

                    weight=ft.FontWeight.W_600,

                    color=AppColors.PRIMARY
                )
            ]
        )