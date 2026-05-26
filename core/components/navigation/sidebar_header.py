import flet as ft

from core.theme.colors import (
    AppColors
)


class SidebarHeader(ft.Container):


    def __init__(self):

        super().__init__()

        self.padding = ft.padding.only(
            bottom=30
        )

        self.content = ft.Column(

            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

            controls=[

                ft.Text(

                    "VALIS",

                    size=28,

                    weight=ft.FontWeight.BOLD,

                    color=AppColors.WHITE
                ),

                ft.Text(

                    "Sistema de Gestión",

                    size=12,

                    color=AppColors.WHITE70
                )
            ]
        )