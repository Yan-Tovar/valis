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

        self.input_order = []

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

            self.input_order.append(field_name)

            # Attach enter key handler
            self._attach_enter_handler(
                input_control,
                field_name
            )

            controls.append(
                input_control
            )

        self.dialog.content.content.controls = (
            controls
        )

    # ---------------------------------------------------------
    # ATTACH ENTER HANDLER
    # ---------------------------------------------------------

    def _attach_enter_handler(
        self,
        input_control,
        field_name
    ):

        """Attach enter key handler to input fields for navigation"""

        def on_enter(e):
            self._handle_enter_key(field_name)

        # Handle different input types
        if isinstance(input_control, ft.Row):
            # For date fields wrapped in Row
            if len(input_control.controls) > 0:
                input_control.controls[0].on_submit = on_enter

        elif hasattr(input_control, 'on_submit'):
            # For TextField and similar controls
            input_control.on_submit = on_enter

        elif hasattr(input_control, 'on_change'):
            # Fallback for other input types
            pass

    # ---------------------------------------------------------
    # HANDLE ENTER KEY
    # ---------------------------------------------------------

    def _handle_enter_key(
        self,
        current_field
    ):

        """Navigate to next field or submit on last field when Enter is pressed"""

        current_index = self.input_order.index(
            current_field
        ) if current_field in self.input_order else -1

        # If not the last input, focus next input
        if current_index >= 0 and current_index < len(
            self.input_order
        ) - 1:

            next_field = self.input_order[
                current_index + 1
            ]

            next_control = self.inputs[next_field]

            # Focus the next control
            if isinstance(next_control, ft.Row):
                if len(next_control.controls) > 0:
                    next_control.controls[0].focus()
            else:
                next_control.focus()

            self.page.update()

        # If last input, submit form
        elif current_index == len(
            self.input_order
        ) - 1:

            self.submit(None)

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