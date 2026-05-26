import flet as ft

from core.theme.colors import AppColors


def app_theme():

    return ft.Theme(

        color_scheme=ft.ColorScheme(

            primary=AppColors.PRIMARY,

            secondary=AppColors.RED,

            surface=AppColors.WHITE
        )
    )