import flet as ft


class CustomButton:

    @staticmethod
    def primary(text, on_click=None):

        return ft.ElevatedButton(
            text=text,
            on_click=on_click,
            height=45,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10)
            )
        )