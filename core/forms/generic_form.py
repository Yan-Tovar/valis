import flet as ft

from core.forms.field_factory import (
    FieldFactory
)

from core.components.forms.dynamic_form import (
    DynamicForm
)


class GenericForm(ft.Column):


    def __init__(
        self,
        model,
        fields,
        values=None,
        page=None
    ):

        super().__init__()

        self.model = model

        self.fields = fields

        self.values = values or {}

        self.page = page

        self.inputs = {}

        controls = []

        # -------------------------------------------------
        # BUILD FIELDS
        # -------------------------------------------------

        for field in fields:

            control = (
                FieldFactory.create_field(
                    model=model,
                    field_name=field,
                    value=self.values.get(field),
                    page=page
                )
            )

            if control:

                self.inputs[field] = control

                controls.append(control)

        self.controls = [

            DynamicForm(
                controls=controls
            )
        ]


    # -------------------------------------------------
    # GET VALUES
    # -------------------------------------------------

    def get_values(self):

        data = {}

        for field, control in self.inputs.items():

            if hasattr(control, "value"):

                data[field] = control.value

        return data