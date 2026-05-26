import flet as ft

from core.theme.colors import (
    AppColors
)


class CrudStateBadge(ft.Container):


    def __init__(
        self,
        estado
    ):

        super().__init__()

        active = (
            estado == "ACTIVO"
        )

        self.padding = ft.padding.symmetric(

            horizontal=12,

            vertical=5
        )

        self.border_radius = 30

        self.bgcolor = (

            AppColors.SUCCESS
            if active
            else AppColors.ERROR
        )

        self.content = ft.Text(

            estado,

            color=AppColors.WHITE,

            size=12,

            weight=ft.FontWeight.BOLD
        )