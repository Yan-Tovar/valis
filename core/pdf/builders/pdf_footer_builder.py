from datetime import datetime

from reportlab.platypus import (
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import (
    TA_CENTER,
    TA_LEFT
)

from reportlab.lib import colors

from reportlab.lib.units import mm

from core.pdf.utils.pdf_assets import (
    PARROT
)

from core.pdf.theme.pdf_theme import (
    PdfTheme
)


class PdfFooterBuilder:

    @staticmethod
    def build():

        styles = getSampleStyleSheet()

        elements = []

        # =================================================
        # STYLES
        # =================================================

        center_style = ParagraphStyle(

            "center_style",

            parent=styles["BodyText"],

            alignment=TA_CENTER,

            fontName="Helvetica-Bold",

            fontSize=11,

            leading=14,

            textColor=colors.HexColor(
                PdfTheme.PRIMARY
            )
        )

        date_style = ParagraphStyle(

            "date_style",

            parent=styles["BodyText"],

            alignment=TA_LEFT,

            fontSize=8,

            leading=10,

            textColor=colors.HexColor(
                PdfTheme.TEXT_SECONDARY
            )
        )

        # =================================================
        # TOP SPACE
        # =================================================

        elements.append(
            Spacer(1, 25)
        )

        # =================================================
        # DIVIDER
        # =================================================

        divider = Table(

            [[""]],

            colWidths=[170 * mm],
            rowHeights=[0.8]
        )

        divider.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor(
                        PdfTheme.BORDER
                    )
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),
            ])
        )

        elements.append(divider)

        elements.append(
            Spacer(1, 10)
        )

        # =================================================
        # LEFT - DATE
        # =================================================

        date_text = Paragraph(

            f"""
            Generado:
            {datetime.now().strftime('%d/%m/%Y %H:%M')}
            """,

            date_style
        )

        # =================================================
        # CENTER - VALIS
        # =================================================

        valis = Paragraph(

            "VALIS",

            center_style
        )

        # =================================================
        # RIGHT - PARROT
        # =================================================

        parrot = Image(

            PARROT,

            width=16 * mm,

            height=16 * mm
        )

        # =================================================
        # FOOTER TABLE
        # =================================================

        footer = Table(

            [[
                date_text,
                valis,
                parrot
            ]],

            colWidths=[
                60 * mm,
                90 * mm,
                20 * mm
            ]
        )

        footer.setStyle(

            TableStyle([

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (0, 0),
                    "LEFT"
                ),

                (
                    "ALIGN",
                    (1, 0),
                    (1, 0),
                    "CENTER"
                ),

                (
                    "ALIGN",
                    (2, 0),
                    (2, 0),
                    "RIGHT"
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),
            ])
        )

        elements.append(footer)

        return elements