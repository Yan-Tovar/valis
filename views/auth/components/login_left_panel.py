import flet as ft

from core.theme.colors import (
    AppColors
)

from views.auth.components.welcome_bubble import (
    WelcomeBubble
)


class LoginLeftPanel(ft.Container):

    def __init__(
        self,
        mobile=False,
        width=0
    ):

        super().__init__()

        self.expand = not mobile

        self.height = 320 if mobile else None

        self.bgcolor = AppColors.WHITE

        self.alignment = ft.alignment.center

        self.clip_behavior = ft.ClipBehavior.HARD_EDGE

        # Calcular márgenes dinámicos basados en ancho de pantalla
        if mobile:
            # En mobile, calcular margen izquierdo dinámico
            parrot_left = (width * 0.3) if width > 0 else 120
            parrot_bottom = 90
        else:
            # En desktop, usar valores fijos
            parrot_left = 260
            parrot_bottom = 230

        self.content = ft.Stack(

            expand=True,

            controls=[

                # =====================================
                # BRANCH
                # =====================================

                ft.Container(

                    alignment=(
                        ft.alignment.bottom_left
                    ),

                    margin=ft.margin.only(
                        left=20 if mobile else 50,
                        bottom=40 if mobile else 140
                    ),

                    content=ft.Image(

                        src="branch.png",

                        width=260 if mobile else 500,

                        fit=ft.ImageFit.CONTAIN
                    )
                ),

                # =====================================
                # PARROT - Posición dinámica
                # =====================================

                ft.Container(

                    alignment=(
                        ft.alignment.bottom_left
                    ),

                    margin=ft.margin.only(
                        left=parrot_left,
                        bottom=parrot_bottom
                    ),

                    content=ft.Image(

                        src="parrot.png",

                        width=180 if mobile else 180,

                        height=180 if mobile else 180,

                        fit=ft.ImageFit.CONTAIN
                    )
                ),

                # =====================================
                # BUBBLE - Posición dinámica
                # =====================================

                WelcomeBubble(
                    mobile=mobile,
                    width=width
                )
            ]
        )