import flet as ft

from core.theme.colors import (
    AppColors
)


class SidebarHeader(ft.Container):

    def __init__(self):

        super().__init__()

        self.content = ft.Column(

            spacing=2,

            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

            controls=[

                ft.Text(

                    "VALIS",

                    size=24,

                    weight=ft.FontWeight.BOLD,

                    color=AppColors.WHITE
                ),

                ft.Text(

                    "Sistema de Gestión",

                    size=11,

                    color=AppColors.WHITE70
                )
            ]
        )