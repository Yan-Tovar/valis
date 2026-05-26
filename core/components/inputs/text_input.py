import flet as ft

from core.theme.colors import (
    AppColors
)


class TextInput(ft.TextField):


    def __init__(
        self,
        label,
        password=False,
        multiline=False,
        expand=False
    ):

        super().__init__()

        self.label = label

        self.password = password

        self.multiline = multiline

        self.expand = expand

        self.border_color = AppColors.BORDER

        self.focused_border_color = (
            AppColors.PRIMARY
        )

        self.cursor_color = (
            AppColors.PRIMARY
        )

        self.border_radius = 8

        self.filled = True

        self.bgcolor = AppColors.WHITE