import flet as ft

from core.theme.colors import AppColors


def build(left_panel):
    return ft.Container(
        content=left_panel,
        padding=20,
        bgcolor=AppColors.WHITE,
        border_radius=15,
        border=ft.border.all(1, AppColors.BORDER)
    )
