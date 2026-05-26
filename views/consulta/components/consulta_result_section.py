import flet as ft

from core.theme.colors import AppColors


def build(container):
    # Return a full height container that will host result bubbles and details.
    return ft.Container(
        content=container,
        expand=True,
        padding=ft.padding.all(8)
    )
