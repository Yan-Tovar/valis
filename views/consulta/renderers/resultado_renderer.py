import flet as ft

from core.theme.colors import AppColors


# =========================================================
# SAFE VALUE
# =========================================================

def safe(
    value,
    default="-"
):

    if value is None:
        return default

    value = str(value).strip()

    if value == "":
        return default

    return value


# =========================================================
# COPY FIELD
# =========================================================

def copy_field(
    label,
    value,
    page,
    color=AppColors.PRIMARY,
    icon=None
):

    value = safe(value)

    return ft.Container(

        padding=ft.padding.symmetric(
            horizontal=7,
            vertical=5
        ),

        border_radius=9,

        bgcolor="#F8FAFC",

        content=ft.Row(

            spacing=6,

            vertical_alignment=ft.CrossAxisAlignment.START,

            controls=[

                (
                    ft.Icon(
                        icon,
                        size=12,
                        color=AppColors.TEXT_SECONDARY
                    )

                    if icon
                    else ft.Container(width=0)
                ),

                ft.Column(

                    spacing=1,

                    expand=True,

                    controls=[

                        ft.Text(
                            label,
                            size=8,
                            color=AppColors.TEXT_SECONDARY,
                            weight=ft.FontWeight.W_500
                        ),

                        ft.TextButton(

                            content=ft.Text(
                                value,
                                size=10,
                                weight=ft.FontWeight.BOLD,
                                color=color,
                                selectable=True,
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS
                            ),

                            style=ft.ButtonStyle(
                                padding=0
                            ),

                            on_click=lambda e:
                                page.set_clipboard(value)
                                if page
                                else None
                        )
                    ]
                )
            ]
        )
    )


# =========================================================
# MINI CARD
# =========================================================

def mini_card(
    title,
    controls,
    icon=None,
    action=None
):

    return ft.Container(

        padding=8,

        border_radius=14,

        bgcolor=AppColors.WHITE,

        border=ft.border.all(
            1,
            "#E5E7EB"
        ),

        content=ft.Column(

            spacing=6,

            controls=[

                ft.Row(

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                    vertical_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Row(

                            spacing=5,

                            controls=[

                                (
                                    ft.Icon(
                                        icon,
                                        size=14,
                                        color=AppColors.PRIMARY
                                    )

                                    if icon
                                    else ft.Container(width=0)
                                ),

                                ft.Text(
                                    title,
                                    size=10,
                                    weight=ft.FontWeight.BOLD,
                                    color=AppColors.PRIMARY
                                )
                            ]
                        ),

                        (
                            ft.IconButton(
                                icon=ft.icons.OPEN_IN_NEW,
                                icon_size=15,
                                height=28,
                                width=28,
                                tooltip="Ver detalle",
                                style=ft.ButtonStyle(
                                    padding=2
                                ),
                                on_click=action
                            )

                            if action
                            else ft.Container(width=1)
                        )
                    ]
                ),

                ft.Column(
                    spacing=5,
                    controls=controls
                )
            ]
        )
    )


# =========================================================
# RECOMMENDATION ITEM
# =========================================================

def recommendation_item(
    title,
    description,
    bgcolor
):

    return ft.Container(

        padding=7,

        border_radius=10,

        bgcolor=bgcolor,

        content=ft.Column(

            spacing=2,

            controls=[

                ft.Text(
                    safe(title),
                    size=9,
                    weight=ft.FontWeight.BOLD,
                    color=AppColors.WHITE,
                    max_lines=1,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),

                ft.Text(
                    safe(description),
                    size=9,
                    color=AppColors.WHITE,
                    max_lines=4,
                    overflow=ft.TextOverflow.ELLIPSIS
                )
            ]
        )
    )


# =========================================================
# RESULTADO
# =========================================================

def build(
    data,
    on_open_detail=None
):

    estudio = data.get("estudio", {}) or {}
    salas = data.get("salas", []) or []
    contrato = data.get("contrato", {}) or {}
    entidad = data.get("entidad", {}) or {}
    preparacion = data.get("preparacion", {}) or {}
    listas = data.get("lista_preparaciones", []) or []

    recomendaciones_estudio = (
        data.get("recomendaciones_estudio", [])
        or []
    )

    recomendaciones_entidad = (
        data.get("recomendaciones_entidad", [])
        or []
    )

    # =====================================================
    # PAGE
    # =====================================================

    page = None

    if on_open_detail:

        try:
            page = on_open_detail.__self__.page
        except:
            pass

    # =====================================================
    # HEADER
    # =====================================================

    header = ft.Container(

        padding=10,

        border_radius=16,

        bgcolor=AppColors.PRIMARY,

        content=ft.ResponsiveRow(

            spacing=8,

            run_spacing=6,

            vertical_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[

                ft.Column(

                    col={"xs": 12, "md": 8},

                    spacing=2,

                    controls=[

                        ft.Text(
                            safe(
                                estudio.get("nombre")
                            ),
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color=AppColors.WHITE,
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS
                        ),

                        ft.Text(
                            f"CUPS: {safe(estudio.get('codigo_cups'))}",
                            size=9,
                            color=AppColors.WHITE70
                        ),

                        ft.Text(
                            safe(estudio.get("sigla")),
                            size=9,
                            color=AppColors.WHITE70
                        )
                    ]
                ),

                ft.Column(

                    col={"xs": 12, "md": 4},

                    horizontal_alignment=ft.CrossAxisAlignment.END,

                    spacing=2,

                    controls=[

                        ft.Text(
                            "VALOR ESTUDIO",
                            size=8,
                            color=AppColors.WHITE70
                        ),

                        ft.Text(
                            f"${safe(contrato.get('valor_estudio'), '0')}",
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color="#8CFFB2"
                        ),

                        ft.IconButton(
                            icon=ft.icons.OPEN_IN_NEW,
                            icon_size=16,
                            tooltip="Ver estudio",
                            style=ft.ButtonStyle(
                                bgcolor="#0F5C8E",
                                color=AppColors.WHITE
                            ),
                            on_click=lambda e:
                                on_open_detail({
                                    "type": "estudio",
                                    "data": estudio
                                })
                                if on_open_detail
                                else None
                        )
                    ]
                )
            ]
        )
    )

    # =====================================================
    # SALAS
    # =====================================================

    salas_controls = []

    for sala in salas:

        salas_controls.append(

            ft.Container(

                padding=7,

                border_radius=9,

                bgcolor="#F8FAFC",

                content=ft.Row(

                    spacing=6,

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                    vertical_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Column(

                            spacing=1,

                            expand=True,

                            controls=[

                                ft.Text(
                                    safe(
                                        sala.get("nombre")
                                    ),
                                    size=10,
                                    weight=ft.FontWeight.BOLD,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                ),

                                ft.Text(
                                    (
                                        f"{safe(sala.get('codigo_sala'))} • "
                                        f"{safe(sala.get('sede'))}"
                                    ),
                                    size=8,
                                    color=AppColors.TEXT_SECONDARY,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                )
                            ]
                        ),

                        ft.IconButton(
                            icon=ft.icons.OPEN_IN_NEW,
                            icon_size=15,
                            width=28,
                            height=28,
                            tooltip="Ver sala",
                            on_click=lambda e, p=sala:
                                on_open_detail({
                                    "type": "sala",
                                    "data": p
                                })
                                if on_open_detail
                                else None
                        )
                    ]
                )
            )
        )

    salas_card = mini_card(

        title="SALAS",

        icon=ft.icons.LOCATION_CITY,

        controls=salas_controls
        if salas_controls
        else [
            ft.Text(
                "No hay salas disponibles",
                size=9
            )
        ]
    )

    # =====================================================
    # ENTIDAD
    # =====================================================

    entidad_card = mini_card(

        title="ENTIDAD",

        icon=ft.icons.BUSINESS,

        action=lambda e:
            on_open_detail({
                "type": "entidad",
                "data": entidad
            })
            if on_open_detail
            else None,

        controls=[

            copy_field(
                "Código",
                entidad.get("codigo_entidad"),
                page,
                icon=ft.icons.QR_CODE
            ),

            copy_field(
                "Entidad",
                entidad.get("nombre_entidad")
                or entidad.get("nombre"),
                page,
                icon=ft.icons.BUSINESS
            ),

            copy_field(
                "Ubicación",
                entidad.get("ubicacion"),
                page,
                icon=ft.icons.PLACE
            )
        ]
    )

    # =====================================================
    # CONTRATO
    # =====================================================

    contrato_card = mini_card(

        title="CONTRATO",

        icon=ft.icons.DESCRIPTION,

        action=lambda e:
            on_open_detail({
                "type": "contrato",
                "data": contrato
            })
            if on_open_detail
            else None,

        controls=[

            copy_field(
                "Contrato",
                contrato.get("nombre_contrato")
                or contrato.get("nombre"),
                page,
                icon=ft.icons.DESCRIPTION
            ),

            copy_field(
                "Inicio",
                contrato.get("fecha_inicio"),
                page,
                icon=ft.icons.CALENDAR_MONTH
            ),

            copy_field(
                "Fin",
                contrato.get("fecha_fin"),
                page,
                icon=ft.icons.EVENT_BUSY
            )
        ]
    )
    # =====================================================
    # PREPARACION
    # =====================================================

    prep_controls = []

    # -----------------------------------------------------
    # PREPARACION PRINCIPAL
    # -----------------------------------------------------

    if preparacion:

        prep_controls.append(

            ft.Container(

                padding=7,

                border_radius=9,

                bgcolor="#EFF6FF",

                content=ft.Row(

                    spacing=6,

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                    vertical_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Column(

                            spacing=1,

                            expand=True,

                            controls=[

                                ft.Text(
                                    safe(
                                        preparacion.get("nombre")
                                    ),
                                    size=10,
                                    weight=ft.FontWeight.BOLD,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                ),

                                ft.Text(
                                    safe(
                                        preparacion.get(
                                            "codigo_preparacion"
                                        )
                                    ),
                                    size=8,
                                    color=AppColors.TEXT_SECONDARY
                                )
                            ]
                        ),

                        ft.IconButton(
                            icon=ft.icons.OPEN_IN_NEW,
                            icon_size=15,
                            width=28,
                            height=28,
                            tooltip="Ver preparación",
                            on_click=lambda e:
                                on_open_detail({
                                    "type": "preparacion",
                                    "data": preparacion
                                })
                                if on_open_detail
                                else None
                        )
                    ]
                )
            )
        )

    # -----------------------------------------------------
    # LISTA PREPARACIONES EN 2 COLUMNAS
    # -----------------------------------------------------

    lista_controls = []

    for item in listas:

        lista_controls.append(

            ft.Column(

                col={"xs": 12, "sm": 6, "md": 6},

                controls=[

                    ft.Container(

                        padding=7,

                        border_radius=9,

                        bgcolor="#F8FAFC",

                        height=92,

                        content=ft.Column(

                            spacing=2,

                            controls=[

                                ft.Text(
                                    safe(item.get("nombre")),
                                    size=9,
                                    weight=ft.FontWeight.BOLD,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                ),

                                ft.Text(
                                    safe(item.get("detalle")),
                                    size=8,
                                    max_lines=3,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                ),

                                ft.Text(
                                    safe(item.get("observacion")),
                                    size=8,
                                    color=AppColors.TEXT_SECONDARY,
                                    max_lines=2,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                )
                            ]
                        )
                    )
                ]
            )
        )

    # -----------------------------------------------------
    # AGREGAR GRID RESPONSIVE
    # -----------------------------------------------------

    if lista_controls:

        prep_controls.append(

            ft.ResponsiveRow(

                spacing=6,

                run_spacing=6,

                controls=lista_controls
            )
        )

    # -----------------------------------------------------
    # CARD FINAL
    # -----------------------------------------------------

    preparacion_card = mini_card(

        title="PREPARACIÓN",

        icon=ft.icons.FACT_CHECK,

        controls=prep_controls
    )

    # =====================================================
    # RECOMENDACIONES
    # =====================================================

    recomendaciones_controls = []

    for rec in recomendaciones_estudio:

        recomendaciones_controls.append(

            ft.Column(

                col={"xs": 12, "md": 6},

                controls=[

                    recommendation_item(
                        rec.get("titulo"),
                        rec.get("descripcion"),
                        "#EAB308"
                    )
                ]
            )
        )

    for rec in recomendaciones_entidad:

        recomendaciones_controls.append(

            ft.Column(

                col={"xs": 12, "md": 6},

                controls=[

                    recommendation_item(
                        rec.get("titulo"),
                        rec.get("descripcion"),
                        "#F97316"
                    )
                ]
            )
        )

    recomendaciones_card = None

    if recomendaciones_controls:

        recomendaciones_card = mini_card(

            title="RECOMENDACIONES",

            icon=ft.icons.WARNING_AMBER,

            controls=[

                ft.ResponsiveRow(
                    spacing=6,
                    run_spacing=6,
                    controls=recomendaciones_controls
                )
            ]
        )

    # =====================================================
    # MAIN
    # =====================================================

    controls = [

        # HEADER
        header,

        # FILA 2
        ft.ResponsiveRow(

            spacing=8,
            run_spacing=8,

            controls=[

                # SALAS
                ft.Column(
                    col={"xs": 12, "md": 4},
                    controls=[salas_card]
                ),

                # ENTIDAD
                ft.Column(
                    col={"xs": 12, "md": 4},
                    controls=[entidad_card]
                ),

                # CONTRATO
                ft.Column(
                    col={"xs": 12, "md": 4},
                    controls=[contrato_card]
                )
            ]
        ),

        # FILA 3
        ft.ResponsiveRow(

            spacing=8,
            run_spacing=8,

            controls=[

                ft.Column(
                    col={"xs": 12},
                    controls=[preparacion_card]
                )
            ]
        )
    ]

    # RECOMENDACIONES
    if recomendaciones_card:

        controls.append(

            ft.ResponsiveRow(

                spacing=8,
                run_spacing=8,

                controls=[

                    ft.Column(
                        col={"xs": 12},
                        controls=[recomendaciones_card]
                    )
                ]
            )
        )

    return ft.Container(

        padding=8,

        border_radius=18,

        bgcolor="#FAFAFA",

        border=ft.border.all(
            1,
            "#E5E7EB"
        ),

        content=ft.Column(

            spacing=8,

            controls=controls
        )
    )