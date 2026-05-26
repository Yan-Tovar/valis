from .info_card import build as build_info_card


def build(lista):
    rows = [
        f"Detalle: {lista.get('detalle', '')}",
        f"Observación: {lista.get('observacion', '')}"
    ]
    return build_info_card(
        lista.get('nombre', 'Lista de Preparación'),
        rows
    )
