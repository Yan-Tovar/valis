import flet as ft


class DynamicForm(ft.Column):


    def __init__(
        self,
        controls
    ):

        super().__init__()

        self.controls = controls

        self.spacing = 15