import flet as ft


class EmptyState:

    @staticmethod
    def build(message="No hay registros"):

        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.icons.INBOX, size=60),
                ft.Text(message)
            ]
        )