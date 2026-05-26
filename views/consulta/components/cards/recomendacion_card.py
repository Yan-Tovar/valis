from .info_card import build as build_info_card


def build(recomendacion):
    rows = [
        recomendacion.get('descripcion', '')
    ]
    return build_info_card(
        recomendacion.get('titulo', 'Sin título'),
        rows
    )
