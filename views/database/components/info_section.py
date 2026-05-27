import flet as ft

from core.theme.colors import AppColors


def build_info_section():

    items = [

        "Realiza backups regularmente.",

        "Importar reemplaza la base actual.",

        "Se crea respaldo automático.",

        "Solo administradores."
    ]

    return ft.Container(

        bgcolor=AppColors.LIGHT_GRAY,

        border_radius=16,

        padding=20,

        content=ft.Column(

            spacing=10,

            controls=[

                ft.Text(
                    "Información importante",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=AppColors.PRIMARY
                ),

                *[
                    ft.Text(
                        f"• {item}",
                        size=12
                    )
                    for item in items
                ]
            ]
        )
    )