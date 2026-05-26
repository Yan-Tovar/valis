import flet as ft

from core.theme.colors import (
    AppColors
)


class DataTableComponent(ft.Container):


    def __init__(
        self,
        columns,
        rows
    ):

        super().__init__()

        self.expand = True

        self.bgcolor = AppColors.WHITE

        self.border_radius = 10

        self.padding = 20

        self.content = ft.DataTable(

            columns=columns,

            rows=rows,

            expand=True
        )