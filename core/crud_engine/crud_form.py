import flet as ft

from core.theme.colors import (
    AppColors
)

from core.components.buttons.primary_button import (
    PrimaryButton
)

from core.crud_engine.field_factory import (
    FieldFactory
)

class CrudForm:


    def __init__(

        self,

        page,

        title,

        model,

        fields,

        on_submit
    ):

        self.page = page

        self.title = title

        self.model = model

        self.fields_config = fields

        self.on_submit = on_submit

        self.inputs = {}

        self.record_id = None

        self.dialog = ft.AlertDialog(

            modal=True,

            bgcolor=AppColors.WHITE,

            shape=ft.RoundedRectangleBorder(
                radius=20
            ),

            on_dismiss=self.close,

            content=ft.Container(

                width=500,

                padding=20,

                content=ft.Column(

                    tight=True,

                    spacing=20,

                    controls=[]
                )
            )
        )

        self.build_form()


    # ---------------------------------------------------------
    # BUILD FORM
    # ---------------------------------------------------------

    def build_form(self):

        controls = []

        # TITLE

        controls.append(

            ft.Text(

                self.title,

                size=22,

                weight=ft.FontWeight.BOLD,

                color=AppColors.PRIMARY
            )
        )

        # FIELDS

        for field in self.fields_config:

            field_name = field["name"]

            input_control = FieldFactory.create_field(

                model=self.model,

                field_name=field_name,

                page=self.page
            )

            if input_control is None:
                continue

            self.inputs[field_name] = (
                input_control
            )

            controls.append(
                input_control
            )

        self.dialog.content.content.controls = (
            controls
        )

    # ---------------------------------------------------------
    # DIALOG BUILDER
    # ---------------------------------------------------------

    def _recreate_dialog(
        self,
        title_text
    ):

        return ft.AlertDialog(

            modal=True,

            bgcolor=AppColors.WHITE,

            shape=ft.RoundedRectangleBorder(
                radius=20
            ),

            on_dismiss=self.close,

            title=title_text,

            content=self.dialog.content,

            actions=[

                ft.TextButton(

                    "Cancelar",

                    on_click=self.close
                ),

                PrimaryButton(

                    text="Guardar",

                    on_click=self.submit
                )
            ],

            actions_alignment=ft.MainAxisAlignment.END
        )


    # ---------------------------------------------------------
    # OPEN CREATE
    # ---------------------------------------------------------

    def open_create(self):

        self.record_id = None

        for input_control in self.inputs.values():

            if isinstance(input_control, ft.Row):

                input_control.controls[0].value = ""

            else:

                input_control.value = ""

        self.dialog = self._recreate_dialog(
            ft.Text(
                f"Crear {self.title}",
                size=22,
                weight=ft.FontWeight.BOLD,
                color=AppColors.PRIMARY
            )
        )

        self.page.dialog = self.dialog

        self.dialog.open = True

        self.page.update()


    # ---------------------------------------------------------
    # OPEN EDIT
    # ---------------------------------------------------------

    def open_edit(
        self,
        record
    ):

        self.record_id = record["id"]

        for field_name, input_control in self.inputs.items():

            value = record.get(
                field_name,
                ""
            )

            # -------------------------------------------------
            # DATE OBJECT
            # -------------------------------------------------

            if hasattr(
                value,
                "strftime"
            ):

                value = value.strftime(
                    "%Y-%m-%d"
                )

            else:

                value = str(value)

            # -------------------------------------------------
            # DATE FIELD (ROW)
            # -------------------------------------------------

            if isinstance(
                input_control,
                ft.Row
            ):

                input_control.controls[0].value = (
                    value
                )

            # -------------------------------------------------
            # NORMAL FIELD
            # -------------------------------------------------

            else:

                input_control.value = value

        self.dialog = self._recreate_dialog(
            ft.Text(
                f"Editar {self.title}",
                size=22,
                weight=ft.FontWeight.BOLD,
                color=AppColors.PRIMARY
            )
        )

        self.page.dialog = self.dialog

        self.dialog.open = True

        self.page.update()


    # ---------------------------------------------------------
    # SUBMIT
    # ---------------------------------------------------------

    def submit(
        self,
        e
    ):

        data = {}

        for field_name, input_control in self.inputs.items():

            # -------------------------------------------------
            # DATE FIELD (ROW)
            # -------------------------------------------------

            if isinstance(input_control, ft.Row):

                date_field = input_control.controls[0]

                data[field_name] = (
                    date_field.value
                )

            # -------------------------------------------------
            # NORMAL FIELD
            # -------------------------------------------------

            else:

                data[field_name] = (
                    input_control.value
                )

        self.on_submit(
            self.record_id,
            data
        )


    # ---------------------------------------------------------
    # CLOSE
    # ---------------------------------------------------------

    def close(
        self,
        e=None
    ):

        # ---------------------------------------------
        # CERRAR DIALOG
        # ---------------------------------------------

        self.dialog.open = False

        # ---------------------------------------------
        # LIMPIAR REFERENCIA GLOBAL
        # ---------------------------------------------

        if self.page.dialog == self.dialog:

            self.page.dialog = None

        # ---------------------------------------------
        # UPDATE
        # ---------------------------------------------

        self.page.update()