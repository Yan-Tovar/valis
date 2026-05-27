import flet as ft

from core.theme.colors import AppColors


def build_unauthorized_view():

    return ft.Container(

        expand=True,

        alignment=ft.alignment.center,

        content=ft.Column(

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            alignment=ft.MainAxisAlignment.CENTER,

            controls=[

                ft.Icon(
                    ft.icons.LOCK,
                    size=80,
                    color=AppColors.PRIMARY
                ),

                ft.Text(
                    "Acceso Denegado",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    "Solo administradores",
                    size=13
                )
            ]
        )
    )