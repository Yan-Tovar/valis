import flet as ft


class SplashBackground(ft.Container):


    def __init__(self):

        super().__init__()

        self.expand = True

        self.alignment = ft.alignment.center

        self.content = ft.Image(

            src="parrot.gif",

            width=850,

            height=850,

            fit=ft.ImageFit.CONTAIN
        )