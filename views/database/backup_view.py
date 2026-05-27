import os
import flet as ft

from core.theme.colors import AppColors
from core.components.buttons.primary_button import PrimaryButton
from core.services.backup_service import BackupService
from core.router.navigation_service import NavigationService


class BackupView:

    title = "Backup de Base de Datos"

    # =========================================================
    # INIT
    # =========================================================

    def __init__(self, page):

        self.page = page

        self.export_path = ""

        self.import_file = ""

        # =====================================================
        # FILE PICKERS
        # =====================================================

        self.export_directory_picker = ft.FilePicker(
            on_result=self._on_export_directory_selected
        )

        self.import_file_picker = ft.FilePicker(
            on_result=self._on_import_file_selected
        )

        self.page.overlay.extend([
            self.export_directory_picker,
            self.import_file_picker
        ])

        # =====================================================
        # LABELS
        # =====================================================

        self.export_path_text = ft.Text(
            "No se ha seleccionado carpeta",
            size=11,
            selectable=True,
            color=AppColors.TEXT_PRIMARY
        )

        self.import_file_text = ft.Text(
            "No se ha seleccionado archivo",
            size=11,
            selectable=True,
            color=AppColors.TEXT_PRIMARY
        )

    # =========================================================
    # BUILD
    # =========================================================

    def build(self):

        return ft.Column(

            expand=True,

            spacing=0,

            controls=[

                self._build_header(),

                ft.Container(

                    expand=True,

                    padding=20,

                    content=ft.Column(

                        scroll=ft.ScrollMode.AUTO,

                        spacing=20,

                        controls=[

                            self._build_export_section(),

                            self._build_import_section(),

                            self._build_info_section()
                        ]
                    )
                )
            ]
        )

    # =========================================================
    # HEADER
    # =========================================================

    def _build_header(self):

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

                    ft.Column(

                        spacing=2,

                        controls=[

                            ft.Text(
                                self.title,
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color="#1B5E20"
                            ),

                            ft.Text(
                                "Gestiona los backups de tu base de datos Valis",
                                size=12,
                                color=AppColors.BORDER
                            )
                        ]
                    ),

                    ft.ElevatedButton(
                        "Volver",
                        icon=ft.icons.ARROW_BACK,
                        on_click=lambda e:
                        NavigationService.navigate("/dashboard")
                    )
                ]
            )
        )

    # =========================================================
    # EXPORT SECTION
    # =========================================================

    def _build_export_section(self):

        return ft.Container(

            bgcolor="white",

            border_radius=16,

            border=ft.border.all(
                1,
                "#E8F5E9"
            ),

            padding=20,

            content=ft.Column(

                spacing=15,

                controls=[

                    ft.Row(

                        controls=[

                            ft.Icon(
                                ft.icons.CLOUD_DOWNLOAD,
                                size=28,
                                color=AppColors.PRIMARY
                            ),

                            ft.Text(
                                "Exportar Backup",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=AppColors.PRIMARY
                            )
                        ]
                    ),

                    ft.Text(
                        "Descarga una copia de tu base de datos actual.",
                        size=12,
                        color=AppColors.BORDER
                    ),

                    ft.Text(
                        "Carpeta seleccionada:",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color=AppColors.PRIMARY
                    ),

                    ft.Container(

                        border_radius=10,

                        bgcolor=AppColors.LIGHT_GRAY,

                        padding=10,

                        content=self.export_path_text
                    ),

                    ft.Row(

                        spacing=10,

                        controls=[

                            ft.ElevatedButton(
                                "Seleccionar carpeta",
                                icon=ft.icons.FOLDER_OPEN,
                                expand=True,
                                height=45,
                                on_click=self._handle_select_export_folder
                            ),

                            ft.Container(
                                expand=True,

                                content=PrimaryButton(
                                    text="Exportar Backup",
                                    width=None,
                                    on_click=self._handle_export_backup
                                )
                            )
                        ]
                    )
                ]
            )
        )

    # =========================================================
    # IMPORT SECTION
    # =========================================================

    def _build_import_section(self):

        return ft.Container(

            bgcolor="white",

            border_radius=16,

            border=ft.border.all(
                1,
                "#E8F5E9"
            ),

            padding=20,

            content=ft.Column(

                spacing=15,

                controls=[

                    ft.Row(

                        controls=[

                            ft.Icon(
                                ft.icons.CLOUD_UPLOAD,
                                size=28,
                                color=AppColors.PRIMARY
                            ),

                            ft.Text(
                                "Importar Backup",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=AppColors.PRIMARY
                            )
                        ]
                    ),

                    ft.Text(
                        "Restaura una copia de seguridad anterior.",
                        size=12,
                        color=AppColors.BORDER
                    ),

                    ft.Text(
                        "Archivo seleccionado:",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color=AppColors.PRIMARY
                    ),

                    ft.Container(

                        border_radius=10,

                        bgcolor=AppColors.LIGHT_GRAY,

                        padding=10,

                        content=self.import_file_text
                    ),

                    ft.Row(

                        spacing=10,

                        controls=[

                            ft.ElevatedButton(
                                "Seleccionar archivo",
                                icon=ft.icons.UPLOAD_FILE,
                                expand=True,
                                height=45,
                                on_click=self._handle_select_import_file
                            ),

                            ft.Container(
                                expand=True,

                                content=PrimaryButton(
                                    text="Importar Backup",
                                    width=None,
                                    on_click=self._handle_import_backup
                                )
                            )
                        ]
                    )
                ]
            )
        )

    # =========================================================
    # INFO SECTION
    # =========================================================

    def _build_info_section(self):

        return ft.Container(

            bgcolor=AppColors.LIGHT_GRAY,

            border_radius=16,

            padding=20,

            content=ft.Column(

                spacing=10,

                controls=[

                    ft.Row(

                        controls=[

                            ft.Icon(
                                ft.icons.INFO,
                                color=AppColors.PRIMARY
                            ),

                            ft.Text(
                                "Información importante",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=AppColors.PRIMARY
                            )
                        ]
                    ),

                    self._build_info_item(
                        "Realiza backups regularmente."
                    ),

                    self._build_info_item(
                        "La importación reemplaza la BD actual."
                    ),

                    self._build_info_item(
                        "Se crea un respaldo automático antes de importar."
                    )
                ]
            )
        )

    # =========================================================
    # INFO ITEM
    # =========================================================

    def _build_info_item(self, text):

        return ft.Row(

            controls=[

                ft.Text(
                    "•",
                    size=12,
                    color=AppColors.PRIMARY
                ),

                ft.Text(
                    text,
                    size=11,
                    color=AppColors.TEXT_PRIMARY
                )
            ]
        )

    # =========================================================
    # SELECT EXPORT FOLDER
    # =========================================================

    def _handle_select_export_folder(self, e):

        self.export_directory_picker.get_directory_path(
            dialog_title="Selecciona la carpeta donde guardar el backup"
        )

    # =========================================================
    # EXPORT DIRECTORY SELECTED
    # =========================================================

    def _on_export_directory_selected(
        self,
        e: ft.FilePickerResultEvent
    ):

        if e.path:

            self.export_path = e.path

            self.export_path_text.value = self.export_path

            self.page.update()

    # =========================================================
    # SELECT IMPORT FILE
    # =========================================================

    def _handle_select_import_file(self, e):

        self.import_file_picker.pick_files(

            dialog_title="Selecciona un backup",

            allow_multiple=False,

            allowed_extensions=["db"],

            file_type=ft.FilePickerFileType.CUSTOM
        )

    # =========================================================
    # IMPORT FILE SELECTED
    # =========================================================

    def _on_import_file_selected(
        self,
        e: ft.FilePickerResultEvent
    ):

        if e.files:

            selected_file = e.files[0]

            self.import_file = selected_file.path

            self.import_file_text.value = (
                selected_file.name
            )

            self.page.update()

    # =========================================================
    # EXPORT BACKUP
    # =========================================================

    def _handle_export_backup(self, e):

        result = BackupService.export_backup(
            self.export_path
        )

        self._show_result_dialog(
            title="Exportar Backup",
            result=result
        )

    # =========================================================
    # IMPORT BACKUP
    # =========================================================

    def _handle_import_backup(self, e):

        dialog = ft.AlertDialog(

            modal=True,

            title=ft.Text(
                "Confirmar importación"
            ),

            content=ft.Text(
                "¿Deseas importar este backup?"
            ),

            actions=[

                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e:
                    self._close_dialog(dialog)
                ),

                ft.ElevatedButton(
                    "Importar",
                    on_click=lambda e:
                    self._confirm_import(dialog)
                )
            ]
        )

        self.page.dialog = dialog

        dialog.open = True

        self.page.update()

    # =========================================================
    # CONFIRM IMPORT
    # =========================================================

    def _confirm_import(
        self,
        dialog
    ):

        self._close_dialog(dialog)

        result = BackupService.import_backup(
            self.import_file
        )

        self._show_result_dialog(

            title="Importar Backup",

            result=result,

            reload_app=result.get(
                "success",
                False
            )
        )

    # =========================================================
    # RESULT DIALOG
    # =========================================================

    def _show_result_dialog(
        self,
        title,
        result,
        reload_app=False
    ):

        success = result.get(
            "success",
            False
        )

        dialog = ft.AlertDialog(

            modal=True,

            title=ft.Text(title),

            content=ft.Row(

                controls=[

                    ft.Icon(

                        ft.icons.CHECK_CIRCLE
                        if success
                        else ft.icons.ERROR,

                        color=AppColors.SUCCESS
                        if success
                        else AppColors.ERROR
                    ),

                    ft.Text(

                        result.get(
                            "message",
                            "Proceso finalizado"
                        ),

                        expand=True
                    )
                ]
            ),

            actions=[

                ft.TextButton(
                    "Aceptar",
                    on_click=lambda e:
                    self._close_result_dialog(
                        dialog,
                        reload_app
                    )
                )
            ]
        )

        self.page.dialog = dialog

        dialog.open = True

        self.page.update()

    # =========================================================
    # CLOSE RESULT DIALOG
    # =========================================================

    def _close_result_dialog(
        self,
        dialog,
        reload_app=False
    ):

        self._close_dialog(dialog)

        if reload_app:

            NavigationService.navigate("/login")

    # =========================================================
    # CLOSE DIALOG
    # =========================================================

    def _close_dialog(
        self,
        dialog
    ):

        dialog.open = False

        self.page.update()