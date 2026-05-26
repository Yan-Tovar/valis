import flet as ft

from core.theme.colors import AppColors
from ..components.cards.sala_card import build as build_sala_card


def build_estudio_info(query):
    return ft.Card(
        content=ft.Container(
            padding=15,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text(
                        "Información del Estudio",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=AppColors.PRIMARY
                    ),
                    ft.Text(f"Código: {query}"),
                    ft.Text("Salas disponibles:")
                ]
            )
        )
    )


def build_salas_section(salas):
    controls = []

    for sala in salas:
        controls.append(build_sala_card(sala))

    return controls
