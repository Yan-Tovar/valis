import flet as ft

from core.theme.colors import AppColors
from .info_card import build as build_info_card


def build(estudio):
    title = "ESTUDIO"
    rows = [
        f"Código: {estudio.get('codigo_cups', 'N/A')}",
        f"Nombre: {estudio.get('nombre', 'N/A')}",
        f"Sigla: {estudio.get('sigla', 'N/A')}"
    ]
    return build_info_card(
        title,
        rows,
        bgcolor=AppColors.SUCCESS,
        title_color=AppColors.WHITE,
        text_color=AppColors.WHITE
    )
