from reportlab.platypus import (
    Table,
    TableStyle,
    Image,
    Paragraph
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import (
    TA_CENTER,
    TA_LEFT
)

from reportlab.lib.units import mm

from core.pdf.utils.pdf_assets import (
    PARROT,
    UTM
)

from core.pdf.theme.pdf_theme import (
    PdfTheme
)


class PdfHeaderBuilder:

    @staticmethod
    def build(title, total):

        styles = getSampleStyleSheet()

        # =================================================
        # TITLE STYLE
        # =================================================

        title_style = ParagraphStyle(

            "title_style",

            parent=styles["Heading1"],

            fontName="Helvetica-Bold",

            fontSize=18,

            leading=22,

            alignment=TA_LEFT,

            textColor=colors.HexColor(
                PdfTheme.PRIMARY
            )
        )

        # =================================================
        # VALIS STYLE
        # =================================================

        valis_style = ParagraphStyle(

            "valis_style",

            parent=styles["BodyText"],

            fontName="Helvetica-Bold",

            fontSize=9,

            leading=10,

            alignment=TA_CENTER,

            textColor=colors.HexColor(
                PdfTheme.PRIMARY
            )
        )

        # =================================================
        # TOTAL STYLE
        # =================================================

        total_style = ParagraphStyle(

            "total_style",

            parent=styles["BodyText"],

            fontName="Helvetica-Bold",

            fontSize=16,

            leading=18,

            alignment=TA_LEFT,

            textColor=colors.HexColor(
                PdfTheme.PRIMARY
            )
        )

        # =================================================
        # LEFT - PARROT + VALIS
        # =================================================

        parrot = Table(

            [
                [
                    Image(
                        PARROT,
                        width=16 * mm,
                        height=16 * mm
                    )
                ],

                [
                    Paragraph(
                        "VALIS",
                        valis_style
                    )
                ]
            ]
        )

        parrot.setStyle(

            TableStyle([

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
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

        # =================================================
        # CENTER - TOTAL + TITLE
        # =================================================

        title_block = Table(

            [[

                Paragraph(
                    str(total),
                    total_style
                ),

                Paragraph(
                    title.upper(),
                    title_style
                )
            ]],

            colWidths=[
                16 * mm,
                115 * mm
            ]
        )

        title_block.setStyle(

            TableStyle([

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
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

        # =================================================
        # RIGHT - UTM
        # =================================================

        utm = Image(

            UTM,

            width=38 * mm,
            height=12 * mm
        )

        # =================================================
        # MAIN TABLE
        # =================================================

        table = Table(

            [[
                parrot,
                title_block,
                utm
            ]],

            colWidths=[
                32 * mm,
                120 * mm,
                38 * mm
            ]
        )

        table.setStyle(

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
                    "LEFT"
                ),

                (
                    "ALIGN",
                    (2, 0),
                    (2, 0),
                    "RIGHT"
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    10
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
            ])
        )

        return table
    