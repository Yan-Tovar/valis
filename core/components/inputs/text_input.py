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

        expand=False,

        autofocus=False,

        read_only=False,

        prefix_icon=None,

        suffix_icon=None,

        keyboard_type=None,

        max_lines=None
    ):

        super().__init__()

        # ============================================
        # BASIC
        # ============================================

        self.label = label

        self.password = password

        self.multiline = multiline

        self.expand = expand

        self.autofocus = autofocus

        self.read_only = read_only

        self.prefix_icon = prefix_icon

        self.suffix_icon = suffix_icon

        self.keyboard_type = keyboard_type

        self.max_lines = max_lines

        # ============================================
        # STYLE
        # ============================================

        self.border_color = (
            AppColors.BORDER
        )

        self.focused_border_color = (
            AppColors.PRIMARY
        )

        self.cursor_color = (
            AppColors.PRIMARY
        )

        self.border_radius = 10

        self.filled = True

        self.bgcolor = AppColors.WHITE

        self.text_size = 14

        self.height = 52

        self.content_padding = 14

        # ============================================
        # PASSWORD
        # ============================================

        if password:

            self.can_reveal_password = True