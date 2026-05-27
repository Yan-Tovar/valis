import flet as ft
import threading
import time

from core.theme.colors import AppColors
from core.theme.typography import FontSize


class AnimatedLogo(ft.Column):


    def __init__(
        self,
        page: ft.Page,
        text="Valis"
    ):

        super().__init__()

        self.page = page

        self.text = text

        # ==================================================
        # LAYOUT
        # ==================================================

        self.horizontal_alignment = (
            ft.CrossAxisAlignment.CENTER
        )

        self.alignment = (
            ft.MainAxisAlignment.CENTER
        )

        self.spacing = 0

        # ==================================================
        # LETTERS
        # ==================================================

        self.letters = []

        for char in self.text:

            letter = ft.Text(

                value=char,

                size=56,

                weight=ft.FontWeight.W_700,

                color=AppColors.PRIMARY,

                opacity=0,

                offset=ft.transform.Offset(0, -1.5),

                animate_opacity=400,

                animate_offset=ft.Animation(
                    duration=300,
                    curve=ft.AnimationCurve.BOUNCE_OUT
                )
            )

            self.letters.append(letter)

        # ==================================================
        # UI
        # ==================================================

        self.controls = [

            # ==============================================
            # GIF
            # ==============================================

            ft.Image(

                src="parrot.gif",

                width=640,

                fit=ft.ImageFit.CONTAIN
            ),

            # ==============================================
            # TEXT BLOCK
            # ==============================================

            ft.Container(

                margin=ft.margin.only(top=-70),

                content=ft.Column(

                    horizontal_alignment=(
                        ft.CrossAxisAlignment.CENTER
                    ),

                    spacing=-4,

                    controls=[

                        # ==================================
                        # TITLE
                        # ==================================

                        ft.Row(

                            alignment=(
                                ft.MainAxisAlignment.CENTER
                            ),

                            spacing=2,

                            controls=self.letters
                        ),

                        # ==================================
                        # SUBTITLE
                        # ==================================

                        ft.Text(

                            "Validación para Citas",

                            size=FontSize.TEXT,

                            color=AppColors.DARK_GRAY,

                            text_align=ft.TextAlign.CENTER
                        )
                    ]
                )
            )
        ]

        # ==================================================
        # START ANIMATION
        # ==================================================

        threading.Thread(
            target=self.animate,
            daemon=True
        ).start()

    # ======================================================
    # ANIMATION
    # ======================================================

    def animate(self):

        time.sleep(1)

        for letter in self.letters:

            letter.opacity = 1

            letter.offset = (
                ft.transform.Offset(0, 0)
            )

            self.page.update()

            time.sleep(0.10)