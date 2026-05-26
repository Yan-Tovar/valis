import flet as ft

from .info_card import build as build_info_card


def build(sala):
    rows = [
        f"Código: {sala.get('codigo_sala', '')}",
        f"Sede: {sala.get('sede', '')}",
        f"Localización: {sala.get('localizacion', '')}"
    ]
    return build_info_card(
        sala.get('nombre', 'Sala'),
        rows
    )
