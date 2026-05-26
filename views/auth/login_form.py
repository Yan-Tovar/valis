import flet as ft

from core.components.inputs.text_input import (
    TextInput
)

from core.components.buttons.primary_button import (
    PrimaryButton
)

from core.theme.spacing import (
    Spacing
)


class LoginForm(ft.Column):


    def __init__(
        self,
        on_login
    ):

        super().__init__()

        self.spacing = Spacing.MD

        self.horizontal_alignment = (
            ft.CrossAxisAlignment.CENTER
        )

        # -------------------------------------------------
        # INPUTS
        # -------------------------------------------------

        self.nombre_usuario = TextInput(
            label="Usuario"
        )

        self.password = TextInput(
            label="Contraseña",
            password=True
        )

        # -------------------------------------------------
        # EVENTS
        # -------------------------------------------------

        self.nombre_usuario.on_submit = (
            self.focus_password
        )

        self.password.on_submit = (
            self.submit_login
        )

        self.on_login = on_login

        # -------------------------------------------------
        # UI
        # -------------------------------------------------

        self.controls = [

            self.nombre_usuario,

            self.password,

            PrimaryButton(

                text="Ingresar",

                width=260,

                on_click=self.submit_login
            )
        ]


    # -------------------------------------------------
    # FOCUS PASSWORD
    # -------------------------------------------------

    def focus_password(self, e):

        self.password.focus()


    # -------------------------------------------------
    # SUBMIT
    # -------------------------------------------------

    def submit_login(self, e):

        self.on_login(

            self.nombre_usuario.value,

            self.password.value
        )