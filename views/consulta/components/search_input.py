import flet as ft

from core.theme.colors import AppColors


def build(label, hint_text, width, value, on_submit, on_change, autofocus=True, visible=True):
    return ft.TextField(
        label=label,
        hint_text=hint_text,
        width=width,
        value=value,
        autofocus=autofocus,
        visible=visible,
        on_submit=on_submit,
        on_change=on_change,
        dense=True,
        border_radius=10,
        filled=True,
        fill_color=AppColors.WHITE,
        focused_border_color=AppColors.PRIMARY,
        border_color=AppColors.BORDER,
        cursor_color=AppColors.PRIMARY,
        content_padding=ft.padding.symmetric(horizontal=12, vertical=12)
    )
