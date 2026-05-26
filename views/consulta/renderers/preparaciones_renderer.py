from core.theme.colors import AppColors
from ..components.cards.preparacion_card import build as build_preparacion_card
from ..components.cards.lista_preparacion_card import build as build_lista_preparacion_card
import flet as ft


def build_preparacion_section(preparacion):
    if not preparacion:
        return []

    return [build_preparacion_card(preparacion)]


def build_lista_preparaciones_section(listas):
    if not listas:
        return []

    controls = [
        ft.Text(
            "LISTA DE PREPARACIONES",
            size=12,
            weight=ft.FontWeight.BOLD,
            color=AppColors.PRIMARY
        )
    ]
    controls.extend([build_lista_preparacion_card(lista) for lista in listas])
    return controls
