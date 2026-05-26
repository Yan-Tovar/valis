import flet as ft

from core.theme.colors import (
    AppColors
)


class CustomTextField:


    @staticmethod
    def build(

        label="",

        value="",

        password=False,

        multiline=False,

        read_only=False,

        autofocus=False,

        expand=True
    ):

        return ft.TextField(

            label=label,

            value=value,

            password=password,

            can_reveal_password=password,

            multiline=multiline,

            min_lines=3 if multiline else 1,

            max_lines=5 if multiline else 1,

            read_only=read_only,

            autofocus=autofocus,

            expand=expand,

            dense=True,

            filled=True,

            border_radius=14,

            bgcolor=AppColors.WHITE,

            border_color=AppColors.BORDER,

            focused_border_color=AppColors.PRIMARY,

            text_size=14,

            label_style=ft.TextStyle(
                size=13,
                color=AppColors.TEXT_SECONDARY
            ),

            cursor_color=AppColors.PRIMARY,

            content_padding=ft.padding.symmetric(
                horizontal=15,
                vertical=16
            )
        )