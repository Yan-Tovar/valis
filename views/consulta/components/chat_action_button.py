import flet as ft

from core.theme.colors import AppColors


def build(
    text,
    on_click
):

    return ft.ElevatedButton(

        text=text,

        icon=ft.icons.CHECK_CIRCLE,

        on_click=on_click,

        style=ft.ButtonStyle(

            bgcolor=AppColors.PRIMARY,

            color=AppColors.WHITE,

            padding=20,

            shape=ft.RoundedRectangleBorder(
                radius=14
            )
        )
    )