import flet as ft

from core.theme.colors import AppColors


class PrimaryButton(ft.Container):


    def __init__(
        self,
        text,
        on_click=None,
        color=AppColors.PRIMARY,
        icon=None,
        width=160
    ):

        super().__init__()

        self.content = ft.ElevatedButton(

            text=text,

            icon=icon,

            width=width,

            height=45,

            bgcolor=color,

            color=AppColors.WHITE,

            style=ft.ButtonStyle(

                shape=ft.RoundedRectangleBorder(
                    radius=8
                )
            ),

            on_click=on_click
        )