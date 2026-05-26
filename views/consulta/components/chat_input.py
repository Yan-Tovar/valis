import flet as ft

from core.theme.colors import AppColors


def build(
    hint_text,
    on_change,
    visible=True,
    autofocus=False
):

    return ft.TextField(

        hint_text=hint_text,

        border_radius=20,

        filled=True,

        expand=True,

        autofocus=autofocus,

        visible=visible,

        dense=True,

        cursor_color=AppColors.PRIMARY,

        focused_border_color=AppColors.PRIMARY,

        border_color=AppColors.BORDER,

        fill_color=AppColors.WHITE,

        content_padding=ft.padding.symmetric(
            horizontal=20,
            vertical=14
        ),

        on_change=on_change
    )