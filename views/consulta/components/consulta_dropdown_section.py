import flet as ft

from core.theme.colors import AppColors


def build(title, dropdown_control):
    return ft.Column(
        spacing=8,
        controls=[
            ft.Text(
                title,
                size=14,
                weight=ft.FontWeight.BOLD,
                color=AppColors.TEXT_PRIMARY
            ),
            dropdown_control
        ]
    )
