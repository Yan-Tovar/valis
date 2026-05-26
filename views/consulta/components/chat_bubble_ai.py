import flet as ft

from core.theme.colors import AppColors


def build(message, controls=None):

    controls = controls or []

    bubble = ft.Container(

        content=ft.Column(

            controls=[

                ft.Text(
                    message,
                    size=13,
                    color=AppColors.TEXT_PRIMARY
                ),

                *controls
            ],

            spacing=10,
            tight=True
        ),

        padding=15,

        bgcolor=AppColors.LIGHT_GRAY,

        border_radius=20,

        border=ft.border.all(
            1,
            AppColors.BORDER
        ),

        expand=True
    )

    return ft.Row(

        alignment=ft.MainAxisAlignment.START,

        vertical_alignment=ft.CrossAxisAlignment.START,

        controls=[

            ft.Container(

                content=ft.Image(
                    src="assets/parrot.png",
                    width=42,
                    height=42,
                    fit=ft.ImageFit.CONTAIN
                ),

                margin=ft.margin.only(
                    top=5
                )
            ),

            bubble
        ]
    )