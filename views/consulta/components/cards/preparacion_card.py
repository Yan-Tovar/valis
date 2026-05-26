from .info_card import build as build_info_card


def build(preparacion):
    rows = [
        f"Código: {preparacion.get('codigo_preparacion', '')}",
        f"Nombre: {preparacion.get('nombre', 'N/A')}"
    ]
    return build_info_card(
        "PREPARACIÓN",
        rows
    )
