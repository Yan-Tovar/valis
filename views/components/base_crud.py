import flet as ft

from views.components.snackbar import Snackbar


class BaseCrudView:

    # ==========================================
    # INIT
    # ==========================================

    def __init__(
        self,
        page,
        title,
        columns,
        controller
    ):

        self.page = page

        self.title = title

        self.columns = columns

        self.controller = controller

        self.data_table = ft.DataTable(
            expand=True,
            columns=[],
            rows=[]
        )

    # ==========================================
    # SNACKBAR
    # ==========================================

    def show_message(
        self,
        message,
        color="#43A047"
    ):

        Snackbar.show(
            self.page,
            message,
            color
        )

    # ==========================================
    # MODAL
    # ==========================================

    def open_modal(
        self,
        title,
        content,
        actions=None
    ):

        dialog = ft.AlertDialog(

            modal=True,

            bgcolor="white",

            title=ft.Text(
                title,
                weight=ft.FontWeight.BOLD
            ),

            content=content,

            actions=actions or [],

            actions_alignment=ft.MainAxisAlignment.END
        )

        self.page.dialog = dialog

        dialog.open = True

        self.page.update()

    # ==========================================
    # CERRAR MODAL
    # ==========================================

    def close_modal(self):

        if self.page.dialog:

            self.page.dialog.open = False

            self.page.update()

    # ==========================================
    # CONFIRMAR ELIMINAR
    # ==========================================

    def confirm_delete(
        self,
        item_id,
        callback
    ):

        dialog = ft.AlertDialog(

            modal=True,

            bgcolor="white",

            title=ft.Text(
                "Confirmar eliminación"
            ),

            content=ft.Text(
                "¿Deseas eliminar este registro?"
            ),

            actions=[

                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: self.close_modal()
                ),

                ft.ElevatedButton(
                    "Eliminar",

                    bgcolor="#D32F2F",

                    color="white",

                    on_click=lambda e: callback(
                        item_id,
                        dialog
                    )
                )
            ]
        )

        self.page.dialog = dialog

        dialog.open = True

        self.page.update()

    def close_dialog(
        self,
        dialog
    ):

        dialog.open = False

        self.page.update()

    # ==========================================
    # BOTON CREAR
    # ==========================================

    def create_button(
        self,
        callback
    ):

        return ft.ElevatedButton(

            "Nuevo Registro",

            icon=ft.icons.ADD,

            bgcolor="#43A047",

            color="white",

            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(
                    radius=12
                ),
                padding=18
            ),

            on_click=callback
        )

    # ==========================================
    # HEADER
    # ==========================================

    def build_header(
        self,
        create_callback
    ):

        return ft.Container(

            padding=20,

            bgcolor="white",

            border=ft.border.only(
                bottom=ft.BorderSide(
                    1,
                    "#E8F5E9"
                )
            ),

            content=ft.Row(

                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                controls=[

                    ft.Text(
                        self.title,
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="#1B5E20"
                    ),

                    self.create_button(
                        create_callback
                    )
                ]
            )
        )

    # ==========================================
    # GENERAR COLUMNAS
    # ==========================================

    def generate_columns(self):

        table_columns = []

        for column in self.columns:

            table_columns.append(

                ft.DataColumn(
                    ft.Text(
                        column,
                        weight=ft.FontWeight.BOLD,
                        color="#2E7D32"
                    )
                )
            )

        # ======================================
        # ACCIONES
        # ======================================

        table_columns.append(

            ft.DataColumn(
                ft.Text(
                    "Acciones",
                    weight=ft.FontWeight.BOLD
                )
            )
        )

        return table_columns

    # ==========================================
    # GENERAR FILAS
    # ==========================================

    def generate_rows(
        self,
        items,
        edit_callback,
        detail_callback,
        delete_callback
    ):

        rows = []

        for item in items:

            cells = []

            # ==================================
            # COLUMNAS
            # ==================================

            for value in item["values"]:

                cells.append(
                    ft.DataCell(
                        ft.Text(str(value))
                    )
                )

            # ==================================
            # ACCIONES
            # ==================================

            cells.append(

                ft.DataCell(

                    ft.Row(

                        spacing=5,

                        controls=[

                            # VER

                            ft.IconButton(
                                icon=ft.icons.VISIBILITY_OUTLINED,
                                icon_color="#1976D2",
                                tooltip="Ver detalle",
                                on_click=lambda e, i=item:
                                detail_callback(i)
                            ),

                            # EDITAR

                            ft.IconButton(
                                icon=ft.icons.EDIT_OUTLINED,
                                icon_color="#FB8C00",
                                tooltip="Editar",
                                on_click=lambda e, i=item:
                                edit_callback(i)
                            ),

                            # ELIMINAR

                            ft.IconButton(
                                icon=ft.icons.DELETE_OUTLINED,
                                icon_color="#D32F2F",
                                tooltip="Eliminar",
                                on_click=lambda e:
                                self.confirm_delete(
                                    item["id"],
                                    delete_callback
                                )
                            )
                        ]
                    )
                )
            )

            rows.append(
                ft.DataRow(
                    cells=cells
                )
            )

        return rows

    # ==========================================
    # TABLA
    # ==========================================

    def build_table(
        self,
        items,
        edit_callback,
        detail_callback,
        delete_callback
    ):

        self.data_table.columns = self.generate_columns()

        self.data_table.rows = self.generate_rows(
            items,
            edit_callback,
            detail_callback,
            delete_callback
        )

        return ft.Container(

            expand=True,

            padding=20,

            content=ft.Column(

                scroll=ft.ScrollMode.AUTO,

                controls=[

                    ft.Container(

                        bgcolor="white",

                        border_radius=16,

                        border=ft.border.all(
                            1,
                            "#E8F5E9"
                        ),

                        padding=20,

                        content=ft.Row(

                            scroll=ft.ScrollMode.AUTO,

                            controls=[
                                self.data_table
                            ]
                        )
                    )
                ]
            )
        )

    # ==========================================
    # BUILD GENERAL
    # ==========================================

    def build(
        self,
        items,
        create_callback,
        edit_callback,
        detail_callback,
        delete_callback
    ):

        return ft.Column(

            expand=True,

            spacing=0,

            controls=[

                # HEADER

                self.build_header(
                    create_callback
                ),

                # TABLA

                self.build_table(
                    items,
                    edit_callback,
                    detail_callback,
                    delete_callback
                )
            ]
        )