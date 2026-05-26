import flet as ft


def build():
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ProgressRing()
        ]
    )
