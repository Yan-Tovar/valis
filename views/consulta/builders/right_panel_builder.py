import flet as ft

from core.theme.colors import AppColors


def build(right_panel):
    return ft.Container(
        content=right_panel,
        padding=20,
        expand=True,
        bgcolor=AppColors.WHITE,
        border_radius=15,
        border=ft.border.all(1, AppColors.BORDER)
    )
