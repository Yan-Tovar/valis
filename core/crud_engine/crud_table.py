import flet as ft

from core.theme.colors import (
    AppColors
)

from core.crud_engine.crud_state_badge import (
    CrudStateBadge
)


class CrudTable:


    def __init__(

        self,

        columns,

        on_edit,

        on_delete,

        on_restore,

        on_hard_delete
    ):

        self.columns = columns

        self.on_edit = on_edit

        self.on_delete = on_delete

        self.on_restore = on_restore

        self.on_hard_delete = on_hard_delete

        self.data = []

        self.body = ft.ListView(
            expand=True,
            spacing=0,
            controls=[]
        )

    # ---------------------------------------------------------
    # SET DATA
    # ---------------------------------------------------------

    def set_data(
        self,
        data
    ):

        self.data = data

    # ---------------------------------------------------------
    # GET NESTED VALUE
    # ---------------------------------------------------------

    def get_nested_value(
        self,
        data,
        path
    ):

        if not path:
            return ""

        keys = path.split(".")

        current = data

        for key in keys:

            if not isinstance(current, dict):

                return ""

            current = current.get(key)

            if current is None:

                return ""

        return current

    # ---------------------------------------------------------
    # FORMAT RELATION VALUE
    # ---------------------------------------------------------

    def format_relation_value(
        self,
        value
    ):

        if isinstance(value, dict):

            # ---------------------------------------------
            # CODIGO + NOMBRE
            # ---------------------------------------------

            codigo = (

                value.get("codigo_entidad")

                or value.get("codigo_sala")

                or value.get("codigo_cups")

                or value.get("codigo_preparacion")
            )

            nombre = value.get("nombre")

            if codigo and nombre:

                return f"{codigo} - {nombre}"

            # ---------------------------------------------
            # SOLO NOMBRE
            # ---------------------------------------------

            if nombre:

                return nombre

            # ---------------------------------------------
            # TITULO
            # ---------------------------------------------

            if value.get("titulo"):

                return value.get("titulo")

            # ---------------------------------------------
            # ID
            # ---------------------------------------------

            if value.get("id"):

                return str(value.get("id"))

            return str(value)

        return value

    # ---------------------------------------------------------
    # BUILD HEADER
    # ---------------------------------------------------------

    def build_header(self):

        controls = []

        for column in self.columns:

            controls.append(

                ft.Container(

                    expand=1,

                    content=ft.Text(

                        column["label"],

                        weight=ft.FontWeight.BOLD,

                        color=AppColors.TEXT_PRIMARY
                    )
                )
            )

        controls.append(

            ft.Container(

                width=160,

                content=ft.Text(

                    "Acciones",

                    weight=ft.FontWeight.BOLD
                )
            )
        )

        return ft.Container(

            padding=ft.padding.symmetric(
                vertical=10,
                horizontal=5
            ),

            content=ft.Row(
                controls=controls
            )
        )

    # ---------------------------------------------------------
    # BUILD ROW
    # ---------------------------------------------------------

    def build_row(
        self,
        record
    ):

        controls = []

        # -----------------------------------------------------
        # DYNAMIC COLUMNS
        # -----------------------------------------------------

        for column in self.columns:

            value = self.get_nested_value(
                record,
                column["name"]
            )

            value = self.format_relation_value(
                value
            )

            # -------------------------------------------------
            # ESTADO
            # -------------------------------------------------

            if column["name"] == "estado":

                content = CrudStateBadge(
                    value
                )

            else:

                content = ft.Text(
                    str(value)
                )

            controls.append(

                ft.Container(

                    expand=1,

                    content=content
                )
            )

        # -----------------------------------------------------
        # ACTIONS
        # -----------------------------------------------------

        estado = record.get("estado")

        action_controls = []

        # -----------------------------------------------------
        # REGISTRO ACTIVO (SOFT DELETE)
        # -----------------------------------------------------

        if estado == "ACTIVO":

            action_controls.extend([

                ft.IconButton(

                    icon=ft.icons.EDIT,

                    icon_color=AppColors.INFO,

                    tooltip="Editar",

                    on_click=lambda e,
                    r=record:
                    self.on_edit(r)
                ),

                ft.IconButton(

                    icon=ft.icons.DELETE,

                    icon_color=AppColors.ERROR,

                    tooltip="Desactivar",

                    on_click=lambda e,
                    r=record:
                    self.on_delete(r)
                )
            ])

        # -----------------------------------------------------
        # REGISTRO INACTIVO
        # -----------------------------------------------------

        elif estado == "INACTIVO":

            action_controls.extend([

                ft.IconButton(

                    icon=ft.icons.RESTORE,

                    icon_color=AppColors.SUCCESS,

                    tooltip="Restaurar",

                    on_click=lambda e,
                    r=record:
                    self.on_restore(r)
                ),

                ft.IconButton(

                    icon=ft.icons.DELETE_FOREVER,

                    icon_color=AppColors.ERROR,

                    tooltip="Eliminar definitivamente",

                    on_click=lambda e,
                    r=record:
                    self.on_hard_delete(r)
                )
            ])

        # -----------------------------------------------------
        # REGISTROS SIN SOFT DELETE
        # -----------------------------------------------------

        else:

            action_controls.extend([

                ft.IconButton(

                    icon=ft.icons.EDIT,

                    icon_color=AppColors.INFO,

                    tooltip="Editar",

                    on_click=lambda e,
                    r=record:
                    self.on_edit(r)
                ),

                ft.IconButton(

                    icon=ft.icons.DELETE_FOREVER,

                    icon_color=AppColors.ERROR,

                    tooltip="Eliminar",

                    on_click=lambda e,
                    r=record:
                    self.on_hard_delete(r)
                )
            ])

        actions = ft.Row(

            spacing=0,

            controls=action_controls
        )

        controls.append(

            ft.Container(

                width=160,

                content=actions
            )
        )

        return ft.Container(

            padding=ft.padding.symmetric(
                vertical=10,
                horizontal=5
            ),

            border=ft.border.only(

                bottom=ft.BorderSide(
                    1,
                    AppColors.BORDER
                )
            ),

            content=ft.Row(
                controls=controls
            )
        )

    # ---------------------------------------------------------
    # BUILD BODY
    # ---------------------------------------------------------

    def build_body(self):

        self.body.controls = [

            self.build_row(record)

            for record in self.data
        ]

        return self.body

    # ---------------------------------------------------------
    # REFRESH
    # ---------------------------------------------------------

    def refresh(self):

        self.body.controls = [

            self.build_row(record)

            for record in self.data
        ]

        if self.body.page:

            self.body.update()

    # ---------------------------------------------------------
    # BUILD
    # ---------------------------------------------------------

    def build(self):

        return ft.Container(

            expand=True,

            bgcolor=AppColors.WHITE,

            border_radius=15,

            padding=20,

            border=ft.border.all(
                1,
                AppColors.BORDER
            ),

            content=ft.Column(

                expand=True,

                spacing=0,

                controls=[

                    self.build_header(),

                    ft.Divider(
                        height=1,
                        color=AppColors.BORDER
                    ),

                    self.build_body()
                ]
            )
        )