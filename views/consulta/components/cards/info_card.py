import flet as ft

from core.theme.colors import AppColors


def build(title, rows, bgcolor=None, title_color=AppColors.TEXT_PRIMARY, text_color=AppColors.TEXT_PRIMARY):
    controls = [
        ft.Text(
            title,
            size=14,
            weight=ft.FontWeight.BOLD,
            color=title_color
        )
    ]

    for row in rows:
        controls.append(ft.Text(row, color=text_color))

    return ft.Card(
        content=ft.Container(
            padding=15,
            bgcolor=bgcolor,
            content=ft.Column(
                spacing=8,
                controls=controls
            )
        )
    )
