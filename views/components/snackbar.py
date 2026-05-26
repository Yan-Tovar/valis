import flet as ft


class Snackbar:

    @staticmethod
    def show(page, message, color="green"):

        page.snack_bar = ft.SnackBar(
            content=ft.Text(message),
            bgcolor=color
        )

        page.snack_bar.open = True

        page.update()