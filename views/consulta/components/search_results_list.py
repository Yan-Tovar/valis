import flet as ft

from .search_result_item import build as build_result_item
from .consulta_empty_state import build as build_empty_state
from core.theme.colors import AppColors


def build(title, items, selected_index, on_select):
    if not items:
        return [
            ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color=AppColors.PRIMARY),
            ft.Divider(),
            build_empty_state("No se encontraron resultados")
        ]

    controls = [
        ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color=AppColors.PRIMARY),
        ft.Divider()
    ]

    for index, item in enumerate(items):
        controls.append(
            build_result_item(
                item,
                selected_index == index,
                on_select,
                index
            )
        )

    return controls
