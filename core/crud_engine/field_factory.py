import flet as ft

from sqlalchemy.inspection import inspect
from sqlalchemy.sql.sqltypes import (
    String,
    Integer,
    Float,
    Boolean,
    Date,
    Text
)

from core.components.inputs.text_input import (
    TextInput
)

from core.relationships.relationship_registry import (
    RelationshipRegistry
)

from core.theme.colors import (
    AppColors
)


class FieldFactory:


    @staticmethod
    def create_field(
        model,
        field_name,
        value=None,
        page=None
    ):

        mapper = inspect(model)

        column = mapper.columns.get(field_name)

        if column is None:
            return None

        column_type = column.type

        # -------------------------------------------------
        # RELATIONSHIP FIELD
        # -------------------------------------------------

        relation = (
            RelationshipRegistry.get_relation(
                model,
                field_name
            )
        )

        if relation:

            options = []

            if page and hasattr(page, "relation_data"):

                relation_data = (
                    page.relation_data.get(
                        field_name,
                        []
                    )
                )

                options = []

                for item in relation_data:

                    label = item.get(
                        "label"
                    )

                    # -------------------------------------------------
                    # ENTIDAD CONTRATO LABEL
                    # -------------------------------------------------

                    if not label:

                        entidad = item.get(
                            "entidad"
                        )

                        contrato = item.get(
                            "contrato"
                        )

                        if entidad and contrato:

                            label = (
                                f"{entidad} - {contrato}"
                            )

                        else:

                            label = str(
                                item.get("id")
                            )

                    options.append(

                        ft.dropdown.Option(

                            str(item["id"]),

                            label
                        )
                    )

            return ft.Dropdown(

                label=field_name.replace("_id", "").title(),

                value=(
                    str(value)
                    if value is not None
                    else None
                ),

                options=options,

                border_radius=8,

                filled=True,

                bgcolor=AppColors.WHITE
            )

        # -------------------------------------------------
        # ESTADO
        # -------------------------------------------------

        if field_name == "estado":

            return ft.Dropdown(

                label="Estado",

                value=value,

                options=[

                    ft.dropdown.Option(
                        "ACTIVO"
                    ),

                    ft.dropdown.Option(
                        "INACTIVO"
                    )
                ],

                border_radius=8,

                filled=True,

                bgcolor=AppColors.WHITE
            )

        # -------------------------------------------------
        # STRING
        # -------------------------------------------------

        if isinstance(column_type, String):

            return TextInput(
                label=field_name.title()
            )

        # -------------------------------------------------
        # TEXT
        # -------------------------------------------------

        if isinstance(column_type, Text):

            return TextInput(

                label=field_name.title(),

                multiline=True
            )

        # -------------------------------------------------
        # INTEGER
        # -------------------------------------------------

        if isinstance(column_type, Integer):

            return TextInput(
                label=field_name.title()
            )

        # -------------------------------------------------
        # FLOAT
        # -------------------------------------------------

        if isinstance(column_type, Float):

            return TextInput(
                label=field_name.title()
            )

        # -------------------------------------------------
        # BOOLEAN
        # -------------------------------------------------

        if isinstance(column_type, Boolean):

            return ft.Switch(
                label=field_name.title(),
                value=bool(value)
            )

        # -------------------------------------------------
        # DATE
        # -------------------------------------------------

        if isinstance(column_type, Date):

            date_field = ft.TextField(

                label=field_name.title(),

                value=(
                    str(value)
                    if value
                    else ""
                ),

                read_only=True,

                border_radius=8,

                filled=True,

                bgcolor=AppColors.WHITE,

                expand=True
            )

            def open_date_picker(e):

                def handle_change(event):

                    if event.control.value:

                        selected_date = (
                            event.control.value.strftime(
                                "%Y-%m-%d"
                            )
                        )

                        date_field.value = (
                            selected_date
                        )

                        page.update()

                date_picker = ft.DatePicker(

                    on_change=handle_change
                )

                page.overlay.append(
                    date_picker
                )

                page.update()

                date_picker.pick_date()

            return ft.Row(

                controls=[

                    date_field,

                    ft.IconButton(

                        icon=ft.icons.CALENDAR_MONTH,

                        on_click=open_date_picker
                    )
                ]
            )

        # -------------------------------------------------
        # DEFAULT
        # -------------------------------------------------

        return TextInput(
            label=field_name.title()
        )