import flet as ft

from core.theme.colors import (
    AppColors
)

from core.theme.typography import (
    FontSize
)


class PageTitle(ft.Text):


    def __init__(
        self,
        value
    ):

        super().__init__()

        self.value = value

        self.size = FontSize.TITLE

        self.weight = ft.FontWeight.BOLD

        self.color = AppColors.BLACK