import os

from datetime import datetime

from sqlalchemy.inspection import inspect

from reportlab.platypus import (
    SimpleDocTemplate
)

from reportlab.lib.pagesizes import letter

from database.connection import (
    SessionLocal
)

from core.pdf.templates.default_template import (
    DefaultPdfTemplate
)


class PdfExportService:

    @staticmethod
    def export_model_pdf(
        model,
        destination_path
    ):

        session = SessionLocal()

        try:

            # =====================================
            # VALIDATE PATH
            # =====================================

            if not os.path.isdir(
                destination_path
            ):

                return {

                    "success": False,

                    "message": "Ruta inválida",

                    "file_path": None
                }

            # =====================================
            # FILE INFO
            # =====================================

            model_name = (
                model.__tablename__
            )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            filename = (
                f"{model_name}_{timestamp}.pdf"
            )

            pdf_path = os.path.join(
                destination_path,
                filename
            )

            # =====================================
            # DATABASE DATA
            # =====================================

            records = session.query(
                model
            ).all()

            mapper = inspect(model)

            columns = [
                column.key
                for column in mapper.columns
            ]

            parsed_records = []

            for record in records:

                item = {}

                for column in columns:

                    value = getattr(
                        record,
                        column
                    )

                    item[column] = (
                        ""
                        if value is None
                        else str(value)
                    )

                parsed_records.append(
                    item
                )

            # =====================================
            # PDF DOCUMENT
            # =====================================

            doc = SimpleDocTemplate(

                pdf_path,

                pagesize=letter,

                leftMargin=40,

                rightMargin=40,

                topMargin=40,

                bottomMargin=40
            )

            # =====================================
            # BUILD PDF
            # =====================================

            DefaultPdfTemplate.build_pdf(

                doc=doc,

                model_name=model_name,

                records=parsed_records
            )

            # =====================================
            # SUCCESS
            # =====================================

            return {

                "success": True,

                "message": (
                    "PDF generado correctamente"
                ),

                "file_path": pdf_path
            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e),

                "file_path": None
            }

        finally:

            session.close()