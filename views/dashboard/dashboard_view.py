import flet as ft


class DashboardView:

    # =================================================
    # TITLE
    # =================================================

    title = "Dashboard"

    # =================================================
    # INIT
    # =================================================

    def __init__(
        self,
        page: ft.Page
    ):

        self.page = page

    # =================================================
    # BUILD
    # =================================================

    def build(self):

        return ft.Container(

            expand=True,

            padding=30,

            content=ft.Column(

                expand=True,

                alignment=ft.MainAxisAlignment.CENTER,

                horizontal_alignment=(
                    ft.CrossAxisAlignment.CENTER
                ),

                controls=[

                    ft.Text(

                        "Hola",

                        size=40,

                        weight=ft.FontWeight.BOLD
                    )
                ]
            )
        )