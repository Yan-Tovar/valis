import flet as ft


def build(left_panel, right_panel):
    return ft.Row(
        spacing=20,
        expand=True,
        controls=[
            left_panel,
            right_panel
        ]
    )
