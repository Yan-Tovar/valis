import flet as ft


class CustomTextField:

    @staticmethod
    def build(label, password=False):

        return ft.TextField(

            label=label,

            password=password,

            can_reveal_password=password,

            border=ft.InputBorder.NONE,

            text_size=14,

            dense=True,

            cursor_color="#2E7D32",

            focused_border_color="transparent",

            border_color="transparent",

            bgcolor="transparent",

            content_padding=ft.padding.symmetric(
                horizontal=0,
                vertical=12
            )
        )