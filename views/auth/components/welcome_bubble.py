import flet as ft

from core.theme.colors import (
    AppColors
)


class WelcomeBubble(ft.Container):

    def __init__(
        self,
        mobile=False,
        width=0
    ):

        super().__init__()

        # Calcular posición dinámica basada en ancho de pantalla
        if mobile:
            # En mobile, calcular left dinámico (30% del ancho)
            bubble_left = (width * 0.25) if width > 0 else 170
            bubble_bottom = 170
        else:
            # En desktop, usar valores fijos
            bubble_left = 355
            bubble_bottom = 405

        self.left = bubble_left

        self.bottom = bubble_bottom

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

                    size=12 if mobile else 14,

                    weight=ft.FontWeight.W_600,

                    color=AppColors.PRIMARY
                ),

                ft.Text(

                    "¿Quién eres tú?",

                    size=12 if mobile else 14,

                    weight=ft.FontWeight.W_600,

                    color=AppColors.PRIMARY
                )
            ]
        )