import flet as ft

from core.crud_engine.crud_controller import (
    CrudController
)

from core.crud_engine.crud_toolbar import (
    CrudToolbar
)

from core.crud_engine.crud_table import (
    CrudTable
)

from core.crud_engine.crud_form import (
    CrudForm
)

from core.components.alerts.snackbar import (
    Snackbar
)

from core.relationships.relation_loader import (
    RelationLoader
)


class CrudPage:

    def __init__(
        self,
        page,
        title,
        service,
        columns,
        fields,
        routes=None
    ):

        self.page = page

        self.title = title

        self.service = service

        self.columns = columns

        self.fields = fields

        self.routes = routes or []

        # -------------------------------------------------
        # CONTROLLER
        # -------------------------------------------------

        self.controller = CrudController(
            service=service
        )

        # -------------------------------------------------
        # TABLE
        # -------------------------------------------------

        self.table = CrudTable(

            columns=columns,

            on_edit=self.open_edit,

            on_delete=self.delete_record,

            on_restore=self.restore_record,

            on_hard_delete=self.hard_delete_record
        )

        # -------------------------------------------------
        # RELATIONS
        # -------------------------------------------------

        RelationLoader.load(page)

        # -------------------------------------------------
        # FORM
        # -------------------------------------------------

        self.form_dialog = CrudForm(

            page=page,

            title=title,

            model=service.repository.model,

            fields=fields,

            on_submit=self.submit_form
        )

    # =================================================
    # LOAD DATA
    # =================================================

    def load_data(self):

        response = self.controller.get_all()

        if not response.success:

            Snackbar.error(
                self.page,
                response.message
            )

            return

        self.table.set_data(
            response.data
        )

        if self.table.body.page:

            self.table.refresh()

    # =================================================
    # SEARCH
    # =================================================

    def search(
        self,
        query_text
    ):

        if not query_text or not str(query_text).strip():

            self.load_data()

            return

        cols = []

        for col in self.columns:

            name = (
                col.get("name")
                if isinstance(col, dict)
                else None
            )

            if not name:
                continue

            if "." in name:
                continue

            cols.append(name)

        response = self.controller.search(
            query_text,
            columns=cols
        )

        if not response.success:

            Snackbar.error(
                self.page,
                response.message
            )

            return

        self.table.set_data(
            response.data
        )

        if self.table.body.page:

            self.table.refresh()

    # =================================================
    # CREATE
    # =================================================

    def open_create(self):

        self.form_dialog.open_create()

    # =================================================
    # EDIT
    # =================================================

    def open_edit(
        self,
        data
    ):

        self.form_dialog.open_edit(
            data
        )

    # =================================================
    # SUBMIT
    # =================================================

    def submit_form(
        self,
        record_id,
        data
    ):

        if record_id is not None:

            response = self.controller.update(
                record_id,
                data
            )

        else:

            response = self.controller.create(
                data
            )

        if response.success:

            Snackbar.success(
                self.page,
                response.message
            )

            self.load_data()

            self.form_dialog.close()

        else:

            Snackbar.error(
                self.page,
                response.message
            )

    # =================================================
    # SOFT DELETE
    # =================================================

    def delete_record(
        self,
        record
    ):

        response = self.controller.soft_delete(
            record["id"]
        )

        if response.success:

            Snackbar.success(
                self.page,
                response.message
            )

            self.load_data()

        else:

            Snackbar.error(
                self.page,
                response.message
            )

    # =================================================
    # RESTORE
    # =================================================

    def restore_record(
        self,
        record
    ):

        response = self.controller.restore(
            record["id"]
        )

        if response.success:

            Snackbar.success(
                self.page,
                response.message
            )

            self.load_data()

        else:

            Snackbar.error(
                self.page,
                response.message
            )

    # =================================================
    # HARD DELETE
    # =================================================

    def hard_delete_record(
        self,
        record
    ):

        response = self.controller.hard_delete(
            record["id"]
        )

        if response.success:

            Snackbar.success(
                self.page,
                response.message
            )

            self.load_data()

        else:

            Snackbar.error(
                self.page,
                response.message
            )

    # =================================================
    # BUILD
    # =================================================

    def build(self):

        self.load_data()

        return ft.Column(

            expand=True,

            spacing=20,

            controls=[

                CrudToolbar(

                    title=self.title,

                    on_create=self.open_create,

                    on_search=self.search
                ),

                self.table.build()
            ]
        )