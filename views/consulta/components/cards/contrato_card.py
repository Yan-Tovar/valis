from .info_card import build as build_info_card


def build(contrato):
    rows = [
        f"Entidad: {contrato.get('nombre_entidad', '')}",
        f"Código: {contrato.get('codigo_entidad', '')}",
        f"Ubicación: {contrato.get('ubicacion', '')}",
        f"Contrato: {contrato.get('nombre_contrato', '')}",
        f"Fecha Inicio: {contrato.get('fecha_inicio', 'N/A')}",
        f"Fecha Fin: {contrato.get('fecha_fin', 'N/A')}",
        f"Valor del Estudio: ${contrato.get('valor_estudio', 'N/A')}"
    ]
    return build_info_card(
        "CONTRATO Y ENTIDAD",
        rows,
        bgcolor="#2196F3",
        title_color="#FFFFFF",
        text_color="#FFFFFF"
    )
