import flet as ft

from core.theme.colors import AppColors


# =========================================================
# COPY FIELD
# =========================================================

def copy_field(
    page,
    label,
    value,
    color=AppColors.PRIMARY
):

    value = str(value or "N/A")

    return ft.Column(

        spacing=2,

        controls=[

            ft.Text(
                label,
                size=10,
                color=AppColors.TEXT_SECONDARY,
                weight=ft.FontWeight.W_500
            ),

            ft.TextButton(

                content=ft.Text(
                    value,
                    size=12,
                    weight=ft.FontWeight.BOLD,
                    color=color
                ),

                style=ft.ButtonStyle(
                    padding=0
                ),

                on_click=lambda e: page.set_clipboard(
                    value
                )
            )
        ]
    )


# =========================================================
# SECTION CARD
# =========================================================

def section_card(
    title,
    content,
    bgcolor=AppColors.WHITE
):

    return ft.Container(

        bgcolor=bgcolor,

        border_radius=18,

        padding=15,

        border=ft.border.all(
            1,
            AppColors.BORDER
        ),

        content=ft.Column(

            spacing=12,

            controls=[

                ft.Text(
                    title,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color=AppColors.PRIMARY
                ),

                content
            ]
        )
    )


# =========================================================
# RECOMMENDATION CHIP
# =========================================================

def recommendation_chip(
    title,
    description,
    bgcolor
):

    return ft.Container(

        padding=12,

        border_radius=14,

        bgcolor=bgcolor,

        content=ft.Column(

            spacing=4,

            controls=[

                ft.Text(
                    title,
                    size=12,
                    weight=ft.FontWeight.BOLD,
                    color=AppColors.WHITE
                ),

                ft.Text(
                    description,
                    size=11,
                    color=AppColors.WHITE
                )
            ]
        )
    )


# =========================================================
# SHOW MODAL
# =========================================================

def show_detail_modal(
    page,
    title,
    data
):

    estudio = data.get("estudio", {})
    salas = data.get("salas", [])
    contrato = data.get("contrato", {})
    entidad = data.get("entidad", {})
    preparacion = data.get("preparacion", {})
    listas = data.get("lista_preparaciones", [])

    recomendaciones_estudio = data.get(
        "recomendaciones_estudio",
        []
    )

    recomendaciones_entidad = data.get(
        "recomendaciones_entidad",
        []
    )

    # =====================================================
    # HEADER ESTUDIO
    # =====================================================

    estudio_header = ft.Container(

        padding=20,

        border_radius=20,

        bgcolor=AppColors.PRIMARY,

        content=ft.ResponsiveRow(

            vertical_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[

                ft.Column(

                    col={"xs": 12, "md": 8},

                    spacing=5,

                    controls=[

                        ft.Text(
                            estudio.get(
                                "nombre",
                                "Sin estudio"
                            ),
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=AppColors.WHITE
                        ),

                        copy_field(
                            page,
                            "Código CUPS",
                            estudio.get("codigo_cups"),
                            AppColors.WHITE
                        )
                    ]
                ),

                ft.Column(

                    col={"xs": 12, "md": 4},

                    horizontal_alignment=ft.CrossAxisAlignment.END,

                    controls=[

                        ft.Container(

                            padding=12,

                            border_radius=14,

                            bgcolor="#0E5A8A",

                            content=ft.Column(

                                spacing=2,

                                controls=[

                                    ft.Text(
                                        "VALOR",
                                        size=10,
                                        color=AppColors.WHITE
                                    ),

                                    ft.Text(
                                        f"${contrato.get('valor_estudio', '0')}",
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color="#8CFFB2"
                                    )
                                ]
                            )
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

                padding=10,

                border_radius=12,

                bgcolor="#F7F9FC",

                content=ft.Row(

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                    controls=[

                        ft.Column(

                            spacing=2,

                            controls=[

                                copy_field(
                                    page,
                                    "Código",
                                    sala.get("codigo_sala")
                                ),

                                ft.Text(
                                    sala.get("nombre", ""),
                                    size=12,
                                    weight=ft.FontWeight.BOLD
                                )
                            ]
                        ),

                        ft.IconButton(
                            icon=ft.icons.OPEN_IN_NEW
                        )
                    ]
                )
            )
        )

    # =====================================================
    # CONTRATO
    # =====================================================

    contrato_content = ft.Column(

        spacing=10,

        controls=[

            copy_field(
                page,
                "Contrato",
                contrato.get("nombre_contrato")
            ),

            copy_field(
                page,
                "Fecha inicio",
                contrato.get("fecha_inicio")
            ),

            copy_field(
                page,
                "Fecha fin",
                contrato.get("fecha_fin")
            )
        ]
    )

    # =====================================================
    # ENTIDAD
    # =====================================================

    entidad_content = ft.Column(

        spacing=10,

        controls=[

            copy_field(
                page,
                "Código",
                entidad.get("codigo_entidad")
            ),

            copy_field(
                page,
                "Entidad",
                entidad.get("nombre_entidad")
            )
        ]
    )

    # =====================================================
    # PREPARACION
    # =====================================================

    prep_controls = [

        copy_field(
            page,
            "Preparación",
            preparacion.get("nombre")
        )
    ]

    for item in listas:

        prep_controls.append(

            ft.Container(

                padding=10,

                border_radius=12,

                bgcolor="#F9FAFB",

                content=ft.Column(

                    spacing=5,

                    controls=[

                        ft.Text(
                            item.get("nombre", ""),
                            size=12,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            item.get("detalle", ""),
                            size=11
                        ),

                        ft.Text(
                            item.get("observacion", ""),
                            size=10,
                            color=AppColors.TEXT_SECONDARY
                        )
                    ]
                )
            )
        )

    # =====================================================
    # RECOMENDACIONES
    # =====================================================

    recomendaciones_controls = []

    for rec in recomendaciones_estudio:

        recomendaciones_controls.append(

            recommendation_chip(
                rec.get("titulo", "Recomendación"),
                rec.get("descripcion", ""),
                "#EAB308"
            )
        )

    for rec in recomendaciones_entidad:

        recomendaciones_controls.append(

            recommendation_chip(
                rec.get("titulo", "Recomendación"),
                rec.get("descripcion", ""),
                "#F97316"
            )
        )

    # =====================================================
    # CONTENT
    # =====================================================

    dialog = ft.AlertDialog(

        inset_padding=20,

        content=ft.Container(

            width=1100,

            height=750,

            padding=10,

            content=ft.Column(

                scroll=ft.ScrollMode.AUTO,

                spacing=18,

                controls=[

                    estudio_header,

                    ft.ResponsiveRow(

                        controls=[

                            ft.Column(

                                col={"xs": 12, "md": 3},

                                controls=[

                                    section_card(
                                        "SALAS",
                                        ft.Column(
                                            controls=salas_controls,
                                            spacing=10
                                        )
                                    )
                                ]
                            ),

                            ft.Column(

                                col={"xs": 12, "md": 4},

                                controls=[

                                    section_card(
                                        "CONTRATO",
                                        contrato_content
                                    )
                                ]
                            ),

                            ft.Column(

                                col={"xs": 12, "md": 5},

                                controls=[

                                    section_card(
                                        "ENTIDAD",
                                        entidad_content
                                    )
                                ]
                            )
                        ]
                    ),

                    section_card(
                        "PREPARACIÓN",
                        ft.Column(
                            controls=prep_controls,
                            spacing=10
                        )
                    ),

                    section_card(
                        "RECOMENDACIONES",
                        ft.ResponsiveRow(

                            controls=[

                                ft.Column(
                                    col={"xs": 12, "md": 6},
                                    controls=[
                                        chip
                                    ]
                                )

                                for chip in recomendaciones_controls
                            ]
                        )
                    )
                ]
            )
        ),

        actions=[

            ft.TextButton(
                "Cerrar",
                on_click=lambda e: close_modal(page)
            )
        ]
    )

    page.dialog = dialog

    dialog.open = True

    page.update()


# =========================================================
# CLOSE
# =========================================================

def close_modal(page):

    page.dialog.open = False

    page.update()