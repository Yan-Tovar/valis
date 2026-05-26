import flet as ft

from core.theme.colors import AppColors


def build(message):

    bubble = ft.Container(

        content=ft.Text(
            message,
            size=13,
            color=AppColors.WHITE
        ),

        padding=15,

        bgcolor=AppColors.PRIMARY,

        border_radius=20,

        width=420
    )

    return ft.Row(

        alignment=ft.MainAxisAlignment.END,

        controls=[

            bubble,

            ft.CircleAvatar(
                content=ft.Icon(
                    ft.icons.PERSON,
                    color=AppColors.WHITE
                ),
                radius=18,
                bgcolor=AppColors.PRIMARY
            )
        ]
    )