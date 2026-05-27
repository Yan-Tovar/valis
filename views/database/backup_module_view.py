import flet as ft
import os

from core.theme.colors import AppColors
from core.components.buttons.primary_button import PrimaryButton
from core.security.permissions import Permissions
from core.services.backup_service import BackupService
from core.router.navigation_service import NavigationService

from .components.backup_section import (
    build_backup_section
)

from .components.info_section import (
    build_info_section
)

from .components.unauthorized_view import (
    build_unauthorized_view
)


class BackupModuleView:

    def __init__(self, page):

        self.page = page

        self.current_user = None

        self.export_path = None

        self.import_file = None

    # =====================================================
    # BUILD
    # =====================================================

    def build(self):

        try:

            self.current_user = (
                self.page.session.get("user")
            )

        except:

            self.current_user = None

        if not Permissions.is_admin(
            self.current_user
        ):

            return build_unauthorized_view()

        return self._build_content()

    # =====================================================
    # MAIN CONTENT
    # =====================================================

    def _build_content(self):

        return ft.Container(

            expand=True,

            padding=20,

            content=ft.Column(

                scroll=ft.ScrollMode.AUTO,

                spacing=20,

                controls=[

                    # HEADER

                    self._build_header(),

                    # EXPORT

                    build_backup_section(

                        title="Exportar Backup",

                        subtitle="Descarga una copia de tu base de datos actual",

                        icon=ft.icons.CLOUD_DOWNLOAD,

                        button_text="Exportar Backup",

                        button_icon=ft.icons.DOWNLOAD,

                        path_text=self._get_export_path_display(),

                        select_text="Seleccionar carpeta",

                        on_select=self._handle_select_export_folder,

                        on_action=self._handle_export_backup
                    ),

                    # IMPORT

                    build_backup_section(

                        title="Importar Backup",

                        subtitle="Restaura una copia de seguridad anterior",

                        icon=ft.icons.CLOUD_UPLOAD,

                        button_text="Importar Backup",

                        button_icon=ft.icons.UPLOAD,

                        path_text=self._get_import_file_display(),

                        select_text="Seleccionar archivo",

                        on_select=self._handle_select_import_file,

                        on_action=self._handle_import_backup
                    ),

                    # INFO

                    build_info_section()
                ]
            )
        )

    # =====================================================
    # HEADER
    # =====================================================

    def _build_header(self):

        return ft.Column(

            spacing=5,

            controls=[

                ft.Text(
                    "Backup de Base de Datos",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=AppColors.PRIMARY
                ),

                ft.Text(
                    "Gestiona los backups de Valis",
                    size=13,
                    color=AppColors.TEXT_SECONDARY
                )
            ]
        )

    # =====================================================
    # PATHS
    # =====================================================

    def _get_export_path_display(self):

        return (
            self.export_path
            or
            "No se ha seleccionado carpeta"
        )

    def _get_import_file_display(self):

        if self.import_file:

            return os.path.basename(
                self.import_file
            )

        return "No se ha seleccionado archivo"

    # =====================================================
    # EXPORT
    # =====================================================

    def _handle_select_export_folder(self, e):

        self._show_message(
            "Selecciona manualmente la ruta"
        )

    def _handle_export_backup(self, e):

        if not self.export_path:

            self._show_message(
                "Selecciona una carpeta",
                error=True
            )

            return

        result = BackupService.export_backup(
            self.export_path
        )

        self._show_message(
            result["message"],
            error=not result["success"]
        )

    # =====================================================
    # IMPORT
    # =====================================================

    def _handle_select_import_file(self, e):

        self._show_message(
            "Selecciona manualmente el archivo"
        )

    def _handle_import_backup(self, e):

        if not self.import_file:

            self._show_message(
                "Selecciona un archivo",
                error=True
            )

            return

        result = BackupService.import_backup(
            self.import_file
        )

        self._show_message(
            result["message"],
            error=not result["success"]
        )

    # =====================================================
    # MESSAGE
    # =====================================================

    def _show_message(
        self,
        message,
        error=False
    ):

        self.page.snack_bar = ft.SnackBar(

            content=ft.Text(message),

            bgcolor=(
                AppColors.ERROR
                if error
                else AppColors.SUCCESS
            )
        )

        self.page.snack_bar.open = True

        self.page.update()