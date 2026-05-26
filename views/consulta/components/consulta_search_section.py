import flet as ft

from core.theme.colors import AppColors


def build(title, input_control, button_control):
    return ft.Column(
        spacing=8,
        controls=[
            ft.Text(
                title,
                size=14,
                weight=ft.FontWeight.BOLD,
                color=AppColors.TEXT_PRIMARY
            ),
            ft.Row(
                spacing=10,
                controls=[
                    input_control,
                    button_control
                ]
            )
        ]
    )
