import flet as ft


class SplashBackground(ft.Container):


    def __init__(self):

        super().__init__()

        self.expand = True

        self.bgcolor = "white"

        # ==================================================
        # DECORATIVE BACKGROUND
        # ==================================================

        self.content = ft.Stack(

            expand=True,

            controls=[

                # ==========================================
                # LIGHT DECORATIVE CIRCLE
                # ==========================================

                ft.Container(

                    width=700,

                    height=700,

                    border_radius=350,

                    bgcolor="#F5F9F7",

                    opacity=0.7,

                    alignment=ft.alignment.center,

                    left=-120,

                    top=-120
                ),

                # ==========================================
                # SECONDARY SHAPE
                # ==========================================

                ft.Container(

                    width=450,

                    height=450,

                    border_radius=225,

                    bgcolor="#EEF7F1",

                    opacity=0.8,

                    right=-80,

                    bottom=-80
                )
            ]
        )