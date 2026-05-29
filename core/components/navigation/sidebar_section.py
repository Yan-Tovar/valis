import flet as ft

from core.theme.colors import (
    AppColors
)


class SidebarSection(ft.Container):

    def __init__(

        self,

        title,

        controls,

        opened=False,

        on_toggle=None
    ):

        super().__init__()

        self.content = ft.Column(

            spacing=6,

            controls=[

                # =================================================
                # HEADER BUTTON
                # =================================================

                ft.Container(

                    bgcolor=AppColors.PRIMARY_DARK,

                    border_radius=10,

                    padding=12,

                    ink=True,

                    on_click=on_toggle,

                    content=ft.Row(

                        alignment=(
                            ft.MainAxisAlignment
                            .SPACE_BETWEEN
                        ),

                        controls=[

                            ft.Text(

                                title,

                                size=13,

                                weight=(
                                    ft.FontWeight.BOLD
                                ),

                                color=AppColors.WHITE
                            ),

                            ft.Icon(

                                (
                                    ft.icons.KEYBOARD_ARROW_DOWN
                                    if opened
                                    else ft.icons.KEYBOARD_ARROW_RIGHT
                                ),

                                size=18,

                                color=AppColors.WHITE70
                            )
                        ]
                    )
                ),

                # =================================================
                # ITEMS
                # =================================================

                ft.Column(

                    visible=opened,

                    spacing=5,

                    controls=controls
                )
            ]
        )