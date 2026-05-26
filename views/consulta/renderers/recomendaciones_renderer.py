from ..components.cards.recomendacion_card import build as build_recomendacion_card
import flet as ft
from core.theme.colors import AppColors


def build_recomendation_list(recomendaciones, title):
    controls = [
        ft.Text(
            title,
            size=12,
            weight=ft.FontWeight.BOLD,
            color=AppColors.PRIMARY
        )
    ]

    if recomendaciones:
        controls.extend([
            build_recomendacion_card(recomendacion)
            for recomendacion in recomendaciones
        ])
    else:
        controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Text(
                        "No hay recomendaciones registradas."
                    )
                )
            )
        )

    return controls
