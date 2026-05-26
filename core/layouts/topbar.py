import flet as ft

from core.theme.colors import AppColors


class TopBar(ft.Container):

    def __init__(self, title):

        super().__init__()

        self.title_text = ft.Text(
            title,
            size=22,
            weight=ft.FontWeight.BOLD,
            color=AppColors.TEXT_PRIMARY
        )

        self.height = 70

        self.padding = ft.padding.symmetric(
            horizontal=24
        )

        self.bgcolor = AppColors.WHITE

        self.border = ft.border.only(
            bottom=ft.BorderSide(
                1,
                AppColors.BORDER
            )
        )

        self.content = ft.Row(

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

            controls=[

                self.title_text,

                ft.Row(
                    controls=[
                        ft.CircleAvatar(
                            content=ft.Text("A")
                        )
                    ]
                )
            ]
        )

    # =================================================
    # SET TITLE
    # =================================================

    def set_title(
        self,
        title
    ):

        self.title_text.value = title
