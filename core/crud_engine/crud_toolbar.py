import flet as ft

from core.components.buttons.primary_button import (
    PrimaryButton
)

from core.services.pdf_export_service import (
    PdfExportService
)


class CrudToolbar(ft.Container):

    # =====================================================
    # INIT
    # =====================================================

    def __init__(
        self,
        page,
        model,
        on_create,
        on_search=None,
        pdf_enabled=False
    ):

        super().__init__()

        self.page = page

        self.model = model

        self.on_create = on_create

        self.on_search = on_search

        self.pdf_enabled = pdf_enabled

        # =================================================
        # SEARCH INPUT
        # =================================================

        self.search_input = ft.TextField(

            expand=True,

            height=45,

            hint_text="Buscar...",

            border_radius=10,

            autofocus=False,

            prefix_icon=ft.icons.SEARCH,

            on_submit=lambda e:
            self.execute_search()
        )

        # =================================================
        # DIRECTORY PICKER
        # =================================================

        self.directory_picker = ft.FilePicker(
            on_result=self.on_directory_selected
        )

        self.page.overlay.append(
            self.directory_picker
        )

        # =================================================
        # ACTION BUTTONS
        # =================================================

        action_buttons = []

        # ================================================
        # PDF BUTTON
        # ================================================

        if self.pdf_enabled:

            action_buttons.append(

                PrimaryButton(

                    text="PDF",

                    icon=ft.icons.PICTURE_AS_PDF,

                    color="#DC2626",

                    on_click=lambda e:
                    self.export_pdf()
                )
            )

        # ================================================
        # CREATE BUTTON
        # ================================================

        action_buttons.append(

            PrimaryButton(

                text="Nuevo",

                icon=ft.icons.ADD,

                on_click=lambda e:
                self.on_create()
            )
        )

        # =================================================
        # CONTENT
        # =================================================

        self.content = ft.Row(

            alignment=(
                ft.MainAxisAlignment.SPACE_BETWEEN
            ),

            vertical_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

            controls=[

                # =========================================
                # SEARCH
                # =========================================

                ft.Container(

                    expand=True,

                    margin=ft.margin.only(
                        right=20
                    ),

                    content=self.search_input
                ),

                # =========================================
                # ACTIONS
                # =========================================

                ft.Row(

                    spacing=10,

                    controls=action_buttons
                )
            ]
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def execute_search(self):

        if self.on_search:

            self.on_search(
                self.search_input.value
            )

    # =====================================================
    # EXPORT PDF
    # =====================================================

    def export_pdf(self):

        self.directory_picker.get_directory_path()

    # =====================================================
    # DIRECTORY SELECTED
    # =====================================================

    def on_directory_selected(self, e):

        if not e.path:
            return

        result = (
            PdfExportService.export_model_pdf(

                model=self.model,

                destination_path=e.path
            )
        )

        snack = ft.SnackBar(

            content=ft.Text(
                result["message"]
            ),

            bgcolor=(

                "#16A34A"

                if result["success"]

                else "#DC2626"
            )
        )

        self.page.open(snack)

        self.page.update()