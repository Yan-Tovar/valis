import shutil
import os
from datetime import datetime
from database.connection import SessionLocal, engine
import sqlite3


class BackupService:

    """
    Servicio para manejar importación y exportación de backups de la base de datos
    """

    # Ruta de la base de datos
    DB_NAME = "valis.db"
    DB_PATH = os.path.join(os.getcwd(), DB_NAME)

    @staticmethod
    def export_backup(destination_path):
        """
        Exporta un backup de la base de datos a la ruta especificada

        Args:
            destination_path (str): Ruta donde guardar el backup

        Returns:
            dict: {'success': bool, 'message': str, 'file_path': str}
        """

        try:

            # Validar que la base de datos existe
            if not os.path.exists(BackupService.DB_PATH):
                return {
                    "success": False,
                    "message": "La base de datos no existe",
                    "file_path": None
                }

            # Validar que el destino es un directorio válido
            if not os.path.isdir(destination_path):
                return {
                    "success": False,
                    "message": "La ruta de destino no es un directorio válido",
                    "file_path": None
                }

            # Validar permisos de escritura
            if not os.access(destination_path, os.W_OK):
                return {
                    "success": False,
                    "message": "No tienes permisos para escribir en la ruta seleccionada",
                    "file_path": None
                }

            # Crear nombre del backup con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"valis_backup_{timestamp}.db"
            backup_path = os.path.join(destination_path, backup_filename)

            # Copiar el archivo de base de datos
            shutil.copy2(BackupService.DB_PATH, backup_path)

            return {
                "success": True,
                "message": f"Backup exportado exitosamente: {backup_filename}",
                "file_path": backup_path
            }

        except PermissionError:
            return {
                "success": False,
                "message": "Permiso denegado al escribir el archivo",
                "file_path": None
            }

        except Exception as e:
            return {
                "success": False,
                "message": f"Error al exportar backup: {str(e)}",
                "file_path": None
            }

    @staticmethod
    def import_backup(backup_path):
        """
        Importa un backup de base de datos, reemplazando la actual

        Args:
            backup_path (str): Ruta del archivo de backup a importar

        Returns:
            dict: {'success': bool, 'message': str}
        """

        try:

            # Validar que el archivo de backup existe
            if not os.path.exists(backup_path):
                return {
                    "success": False,
                    "message": "El archivo de backup no existe"
                }

            # Validar que es un archivo válido
            if not os.path.isfile(backup_path):
                return {
                    "success": False,
                    "message": "La ruta seleccionada no es un archivo válido"
                }

            # Validar que tiene extensión .db
            if not backup_path.endswith('.db'):
                return {
                    "success": False,
                    "message": "El archivo debe tener extensión .db"
                }
            
            # =====================================================
            # VALIDAR QUE EL BACKUP PERTENECE A VALIS
            # =====================================================

            validation = BackupService.validate_backup_file(
                backup_path
            )

            if not validation["valid"]:

                return {
                    "success": False,
                    "message": validation["message"]
                }

            # Cerrar todas las sesiones
            session = SessionLocal()
            session.close()

            # Cerrar el engine
            engine.dispose()

            # Crear respaldo de la BD actual antes de importar
            current_backup = f"{BackupService.DB_PATH}.backup"
            if os.path.exists(BackupService.DB_PATH):
                shutil.copy2(BackupService.DB_PATH, current_backup)

            # Reemplazar la BD actual con el backup
            shutil.copy2(backup_path, BackupService.DB_PATH)

            # Reinicializar sesión
            new_session = SessionLocal()

            new_session.close()

            return {
                "success": True,
                "message": "Backup importado exitosamente. La base de datos ha sido restaurada."
            }

        except PermissionError:
            return {
                "success": False,
                "message": "Permiso denegado al leer o escribir el archivo"
            }

        except Exception as e:
            return {
                "success": False,
                "message": f"Error al importar backup: {str(e)}"
            }
        
    @staticmethod
    def validate_backup_file(file_path):
        """
        Valida que un archivo sea un backup válido de Valis

        Args:
            file_path (str): Ruta del archivo a validar

        Returns:
            dict: {'valid': bool, 'message': str}
        """

        try:

            if not os.path.exists(file_path):
                return {
                    "valid": False,
                    "message": "El archivo no existe"
                }

            if not file_path.endswith('.db'):
                return {
                    "valid": False,
                    "message": "El archivo debe tener extensión .db"
                }

            if not os.path.isfile(file_path):
                return {
                    "valid": False,
                    "message": "La ruta no corresponde a un archivo"
                }

            # =====================================================
            # VALIDAR SQLITE
            # =====================================================

            if not BackupService._is_sqlite_database(file_path):

                return {
                    "valid": False,
                    "message": "El archivo no es una base de datos SQLite válida"
                }

            # =====================================================
            # VALIDAR ESTRUCTURA VALIS
            # =====================================================

            connection = sqlite3.connect(file_path)

            cursor = connection.cursor()

            # Verificar existencia de tabla usuarios
            cursor.execute("""

                SELECT name
                FROM sqlite_master
                WHERE type='table'
                AND name='usuarios'

            """)

            table_exists = cursor.fetchone()

            if not table_exists:

                connection.close()

                return {
                    "valid": False,
                    "message": "La base de datos no pertenece a Valis"
                }

            # =====================================================
            # OBTENER COLUMNAS
            # =====================================================

            cursor.execute(
                "PRAGMA table_info(usuarios)"
            )

            columns_info = cursor.fetchall()

            connection.close()

            existing_columns = {
                column[1]
                for column in columns_info
            }

            # =====================================================
            # CAMPOS OBLIGATORIOS
            # =====================================================

            required_columns = {

                "nombre_usuario",
                "nombre_completo",
                "rol",
                "password"
            }

            # =====================================================
            # VALIDAR CAMPOS
            # =====================================================

            if not required_columns.issubset(existing_columns):

                return {
                    "valid": False,
                    "message": "La base de datos no pertenece a Valis"
                }

            return {
                "valid": True,
                "message": "Archivo válido"
            }

        except Exception as e:

            return {
                "valid": False,
                "message": f"Error al validar: {str(e)}"
            }
    
    @staticmethod
    def _is_sqlite_database(file_path):
        """
        Verifica si un archivo es una base de datos SQLite válida

        Args:
            file_path (str): Ruta del archivo

        Returns:
            bool: True si es válido, False en caso contrario
        """

        try:
            with open(file_path, 'rb') as f:
                header = f.read(16)
                # Magic number de SQLite: "SQLite format 3\0"
                return header.startswith(b'SQLite format 3')

        except Exception:
            return False
