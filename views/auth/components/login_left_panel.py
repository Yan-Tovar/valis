import flet as ft

from core.theme.colors import (
    AppColors
)

from views.auth.components.welcome_bubble import (
    WelcomeBubble
)


class LoginLeftPanel(ft.Container):


    def __init__(self):

        super().__init__()

        self.expand = True

        self.bgcolor = AppColors.WHITE

        self.content = ft.Stack(

            expand=True,

            controls=[

                # BRANCH

                ft.Container(

                    alignment=(
                        ft.alignment.bottom_left
                    ),

                    margin=ft.margin.only(
                        left=50,
                        bottom=140
                    ),

                    content=ft.Image(

                        src="branch.png",

                        width=500,

                        fit=ft.ImageFit.CONTAIN
                    )
                ),

                # PARROT

                ft.Container(

                    alignment=(
                        ft.alignment.bottom_left
                    ),

                    margin=ft.margin.only(
                        left=260,
                        bottom=230
                    ),

                    content=ft.Image(

                        src="parrot.png",

                        width=180,

                        height=180,

                        fit=ft.ImageFit.CONTAIN
                    )
                ),

                # BUBBLE

                WelcomeBubble()
            ]
        )