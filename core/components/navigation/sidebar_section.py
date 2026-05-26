import flet as ft

from core.theme.colors import (
    AppColors
)


class SidebarSection(ft.Container):

    def __init__(
        self,
        title,
        controls
    ):

        super().__init__(

            content=ft.Column(

                spacing=10,

                controls=[

                    ft.Text(

                        title.upper(),

                        size=11,

                        weight=ft.FontWeight.BOLD,

                        color=AppColors.WHITE70
                    ),

                    *controls
                ]
            )
        )