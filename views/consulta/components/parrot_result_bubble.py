import flet as ft

from core.theme.colors import AppColors


# ---------------------------------------------------------
# ESTUDIO BUBBLE
# ---------------------------------------------------------

def build_estudio_bubble(
    estudio_info,
    salas,
    username,
    on_open_detail=None
):
    """
    Bubble mostrado después de seleccionar estudio.
    """

    estudio_name = estudio_info.get(
        "nombre",
        "N/A"
    )

    codigo_cups = estudio_info.get(
        "codigo_cups",
        ""
    )

    content_controls = []

    if salas:

        header = f"{username}, el estudio {estudio_name}"

        if codigo_cups:
            header += f" ({codigo_cups})"

        header += " tiene estas salas disponibles:"

        content_controls.append(
            (header, False)
        )

        for sala in salas:

            sala_text = (
                f"{sala.get('codigo', sala.get('codigo_sala', ''))} "
                f"{sala.get('nombre', '')}"
            )

            content_controls.append(
                (
                    sala_text,
                    True,
                    sala
                )
            )

    else:

        content_controls.append(
            (
                f"{username}, este estudio no está registrado",
                False
            )
        )

    return _build_parrot_bubble_controls(
        content_controls,
        on_open_detail
    )


# ---------------------------------------------------------
# RESULTADO COMPLETO BUBBLE
# ---------------------------------------------------------

def build_resultado_bubble(
    resultado_data,
    username,
    on_open_detail=None
):
    """
    Bubble final completo.
    Todo el resultado debe renderizarse aquí.
    """

    content_controls = []

    # ---------------------------------------------------------
    # ESTUDIO
    # ---------------------------------------------------------

    estudio = resultado_data.get(
        "estudio",
        {}
    )

    estudio_name = estudio.get(
        "nombre",
        "N/A"
    )

    codigo_cups = estudio.get(
        "codigo_cups",
        ""
    )

    intro = f"{username}, el estudio {estudio_name}"

    if codigo_cups:
        intro += f" ({codigo_cups})"

    content_controls.append(
        (
            intro,
            False
        )
    )

    # ---------------------------------------------------------
    # SALAS
    # ---------------------------------------------------------

    salas = resultado_data.get(
        "salas",
        []
    )

    if salas:

        content_controls.append(
            (
                "Salas disponibles:",
                False
            )
        )

        for sala in salas:

            sala_text = (
                f"{sala.get('codigo', sala.get('codigo_sala', ''))} "
                f"{sala.get('nombre', '')}"
            )

            content_controls.append(
                (
                    sala_text,
                    True,
                    sala
                )
            )

    # ---------------------------------------------------------
    # CONTRATO
    # ---------------------------------------------------------

    contrato = resultado_data.get(
        "contrato",
        {}
    )

    if contrato:

        contrato_text = (
            f"{contrato.get('nombre_contrato', '')}"
        )

        if contrato.get("nombre_entidad"):

            contrato_text += (
                f" - {contrato.get('nombre_entidad')}"
            )

        content_controls.append(
            (
                "Contrato y entidad:",
                False
            )
        )

        content_controls.append(
            (
                contrato_text,
                True,
                contrato
            )
        )

    # ---------------------------------------------------------
    # PREPARACIÓN
    # ---------------------------------------------------------

    preparacion = resultado_data.get(
        "preparacion",
        {}
    )

    if preparacion:

        prep_text = (
            f"{preparacion.get('codigo_preparacion', '')} "
            f"{preparacion.get('nombre', '')}"
        )

        content_controls.append(
            (
                "Preparación:",
                False
            )
        )

        content_controls.append(
            (
                prep_text,
                True,
                preparacion
            )
        )

    # ---------------------------------------------------------
    # LISTA PREPARACIONES
    # ---------------------------------------------------------

    listas = resultado_data.get(
        "lista_preparaciones",
        []
    )

    if listas:

        content_controls.append(
            (
                "Lista de preparaciones:",
                False
            )
        )

        for lista in listas:

            content_controls.append(
                (
                    f"• {lista.get('nombre', '')}",
                    False
                )
            )

    # ---------------------------------------------------------
    # RECOMENDACIONES ESTUDIO
    # ---------------------------------------------------------

    recomendaciones_estudio = resultado_data.get(
        "recomendaciones_estudio",
        []
    )

    if recomendaciones_estudio:

        content_controls.append(
            (
                "Recomendaciones del estudio:",
                False
            )
        )

        for recomendacion in recomendaciones_estudio:

            texto = (
                recomendacion.get("descripcion")
                or recomendacion.get("texto")
                or "Sin descripción"
            )

            content_controls.append(
                (
                    f"• {texto}",
                    False
                )
            )

    # ---------------------------------------------------------
    # RECOMENDACIONES ENTIDAD
    # ---------------------------------------------------------

    recomendaciones_entidad = resultado_data.get(
        "recomendaciones_entidad",
        []
    )

    if recomendaciones_entidad:

        content_controls.append(
            (
                "Recomendaciones de la entidad:",
                False
            )
        )

        for recomendacion in recomendaciones_entidad:

            texto = (
                recomendacion.get("descripcion")
                or recomendacion.get("texto")
                or "Sin descripción"
            )

            content_controls.append(
                (
                    f"• {texto}",
                    False
                )
            )

    return _build_parrot_bubble_controls(
        content_controls,
        on_open_detail
    )


# ---------------------------------------------------------
# INTERNAL BUILDER
# ---------------------------------------------------------

def _build_parrot_bubble_controls(
    controls_list,
    on_open_detail=None
):
    """
    controls_list:
    [
        (text, is_link),
        (text, is_link, payload)
    ]
    """

    parrot_image = ft.Image(
        src="assets/parrot.png",
        width=70,
        height=70,
        fit=ft.ImageFit.CONTAIN
    )

    bubble_children = []

    for item in controls_list:

        text = item[0]
        is_link = item[1]

        payload = (
            item[2]
            if len(item) > 2
            else None
        )

        # ---------------------------------------------------------
        # LINK ITEM
        # ---------------------------------------------------------

        if is_link:

            row = ft.Row(
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "•",
                        size=12,
                        color=AppColors.TEXT_SECONDARY
                    ),

                    ft.Text(
                        text,
                        size=11,
                        color=AppColors.TEXT_PRIMARY,
                        expand=True
                    ),

                    ft.TextButton(
                        text="Ver",
                        on_click=lambda e, p=payload:
                            on_open_detail(p)
                            if on_open_detail
                            else None,
                        style=ft.ButtonStyle(
                            padding=ft.padding.symmetric(
                                6,
                                2
                            )
                        )
                    )
                ]
            )

        # ---------------------------------------------------------
        # NORMAL ITEM
        # ---------------------------------------------------------

        else:

            row = ft.Row(
                spacing=8,
                controls=[
                    ft.Text(
                        text,
                        size=11,
                        color=AppColors.TEXT_PRIMARY,
                        expand=True
                    )
                ]
            )

        bubble_children.append(row)

    # ---------------------------------------------------------
    # THOUGHT BUBBLE
    # ---------------------------------------------------------

    thought_bubble = ft.Container(
        content=ft.Column(
            controls=bubble_children,
            tight=True,
            spacing=6
        ),
        padding=ft.padding.all(10),
        border_radius=12,
        bgcolor=AppColors.LIGHT_GRAY,
        border=ft.border.all(
            1,
            AppColors.BORDER
        ),
        expand=True,
        margin=ft.margin.only(left=10)
    )

    # ---------------------------------------------------------
    # FINAL ROW
    # ---------------------------------------------------------

    result_row = ft.Row(
        controls=[
            parrot_image,
            thought_bubble
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=False
    )

    return ft.Container(
        content=result_row,
        padding=ft.padding.all(10),
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(
            1,
            AppColors.BORDER
        ),
        margin=ft.margin.only(bottom=12)
    )