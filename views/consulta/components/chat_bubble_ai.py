import flet as ft

from core.theme.colors import AppColors


def build(message, controls=None):

    # =====================================================
    # NORMALIZAR CONTROLS
    # =====================================================

    normalized_controls = []

    if controls:

        # Si ya viene lista
        if isinstance(controls, list):

            normalized_controls.extend(controls)

        # Si viene un control único
        else:

            normalized_controls.append(controls)

    # =====================================================
    # BUBBLE
    # =====================================================

    bubble = ft.Container(

        expand=True,

        padding=15,

        bgcolor=AppColors.LIGHT_GRAY,

        border_radius=20,

        border=ft.border.all(
            1,
            AppColors.BORDER
        ),

        content=ft.Column(

            spacing=10,

            tight=True,

            controls=[

                ft.Text(
                    message,
                    size=13,
                    color=AppColors.TEXT_PRIMARY
                ),

                *normalized_controls
            ]
        )
    )

    # =====================================================
    # ROW
    # =====================================================

    return ft.Row(

        alignment=ft.MainAxisAlignment.START,

        vertical_alignment=ft.CrossAxisAlignment.START,

        controls=[

            ft.Container(

                margin=ft.margin.only(top=5),

                content=ft.Image(
                    src="assets/parrot.png",
                    width=42,
                    height=42,
                    fit=ft.ImageFit.CONTAIN
                )
            ),

            bubble
        ]
    )
