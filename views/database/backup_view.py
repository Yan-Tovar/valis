import flet as ft

from core.services.backup_service import (
    BackupService
)

from core.theme.colors import (
    AppColors
)


class BackupView:

    # =================================================
    # TITLE
    # =================================================

    title = "Backup"

    # =================================================
    # INIT
    # =================================================

    def __init__(
        self,
        page: ft.Page
    ):

        self.page = page

        # =============================================
        # FILE PICKERS
        # =============================================

        self.import_picker = ft.FilePicker(
            on_result=self.on_import_selected
        )

        self.export_picker = ft.FilePicker(
            on_result=self.on_export_selected
        )

        self.page.overlay.extend([

            self.import_picker,
            self.export_picker
        ])

        # =============================================
        # STATUS TEXT
        # =============================================

        self.status_text = ft.Text(
            "",
            size=14,
            color=AppColors.PRIMARY
        )

    # =================================================
    # SNACKBAR
    # =================================================

    def show_message(
        self,
        message,
        success=True
    ):

        self.page.snack_bar = ft.SnackBar(

            content=ft.Text(message),

            bgcolor=(
                ft.colors.GREEN_600
                if success
                else ft.colors.RED_600
            )
        )

        self.page.snack_bar.open = True

        self.page.update()

    # =================================================
    # IMPORT BACKUP
    # =================================================

    def import_backup(self, e):

        self.import_picker.pick_files(

            dialog_title="Seleccionar backup",

            allowed_extensions=["db"],

            allow_multiple=False
        )

    # =================================================
    # EXPORT BACKUP
    # =================================================

    def export_backup(self, e):

        self.export_picker.get_directory_path(

            dialog_title="Seleccionar carpeta destino"
        )

    # =================================================
    # IMPORT RESULT
    # =================================================

    def on_import_selected(
        self,
        e: ft.FilePickerResultEvent
    ):

        if not e.files:
            return

        file_path = e.files[0].path

        self.status_text.value = (
            "Importando backup..."
        )

        self.page.update()

        result = BackupService.import_backup(
            file_path
        )

        self.status_text.value = ""

        self.show_message(

            result["message"],

            success=result["success"]
        )

    # =================================================
    # EXPORT RESULT
    # =================================================

    def on_export_selected(
        self,
        e: ft.FilePickerResultEvent
    ):

        if not e.path:
            return

        self.status_text.value = (
            "Exportando backup..."
        )

        self.page.update()

        result = BackupService.export_backup(
            e.path
        )

        self.status_text.value = ""

        self.show_message(

            result["message"],

            success=result["success"]
        )

    # =================================================
    # BUILD BUTTON
    # =================================================

    def build_button(
        self,
        text,
        icon,
        on_click,
        bgcolor
    ):

        return ft.Container(

            width=260,

            height=52,

            border_radius=14,

            shadow=ft.BoxShadow(
                blur_radius=12,
                color="black12",
                offset=ft.Offset(0, 4)
            ),

            content=ft.ElevatedButton(

                text=text,

                icon=icon,

                on_click=on_click,

                style=ft.ButtonStyle(

                    bgcolor=bgcolor,

                    color=ft.colors.WHITE,

                    shape=ft.RoundedRectangleBorder(
                        radius=14
                    ),

                    text_style=ft.TextStyle(
                        size=15,
                        weight=ft.FontWeight.W_600
                    )
                )
            )
        )

    # =================================================
    # BUILD
    # =================================================

    def build(self):

        mobile = self.page.width < 700

        return ft.Container(

            expand=True,

            bgcolor="#F5F7FA",

            padding=30,

            content=ft.Column(

                expand=True,

                alignment=ft.MainAxisAlignment.CENTER,

                horizontal_alignment=(
                    ft.CrossAxisAlignment.CENTER
                ),

                spacing=25,

                controls=[

                    # =================================
                    # IMAGE
                    # =================================

                    ft.Image(

                        src="folder.png",

                        width=180 if mobile else 240,

                        height=180 if mobile else 240,

                        fit=ft.ImageFit.CONTAIN
                    ),

                    # =================================
                    # TITLE
                    # =================================

                    ft.Text(

                        "Gestión de Backups",

                        size=26 if mobile else 34,

                        weight=ft.FontWeight.BOLD,

                        color=AppColors.PRIMARY
                    ),

                    ft.Text(

                        (
                            "Importa o exporta "
                            "copias de seguridad "
                            "de la base de datos"
                        ),

                        size=14 if mobile else 16,

                        color=ft.colors.BLACK54,

                        text_align=ft.TextAlign.CENTER
                    ),

                    # =================================
                    # BUTTONS
                    # =================================

                    ft.ResponsiveRow(

                        alignment=(
                            ft.MainAxisAlignment.CENTER
                        ),

                        spacing=20,

                        run_spacing=20,

                        controls=[

                            ft.Column(

                                col={
                                    "xs": 12,
                                    "sm": 6,
                                    "md": 4
                                },

                                horizontal_alignment=(
                                    ft.CrossAxisAlignment.CENTER
                                ),

                                controls=[

                                    self.build_button(

                                        text="Importar Backup",

                                        icon=(
                                            ft.icons.UPLOAD_FILE
                                        ),

                                        on_click=(
                                            self.import_backup
                                        ),

                                        bgcolor=(
                                            AppColors.PRIMARY
                                        )
                                    )
                                ]
                            ),

                            ft.Column(

                                col={
                                    "xs": 12,
                                    "sm": 6,
                                    "md": 4
                                },

                                horizontal_alignment=(
                                    ft.CrossAxisAlignment.CENTER
                                ),

                                controls=[

                                    self.build_button(

                                        text="Exportar Backup",

                                        icon=(
                                            ft.icons.DOWNLOAD
                                        ),

                                        on_click=(
                                            self.export_backup
                                        ),

                                        bgcolor="#10B981"
                                    )
                                ]
                            )
                        ]
                    ),

                    # =================================
                    # STATUS
                    # =================================

                    self.status_text
                ]
            )
        )