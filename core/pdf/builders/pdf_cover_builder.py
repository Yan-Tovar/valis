from reportlab.platypus import (
    Spacer,
    Image,
    Paragraph,
    PageBreak,
    Table,
    TableStyle
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import (
    TA_CENTER
)

from reportlab.lib import colors

from reportlab.lib.units import mm

from core.pdf.utils.pdf_assets import (
    PARROT,
    GREEN_BUBBLE
)

from core.pdf.theme.pdf_theme import (
    PdfTheme
)


class PdfCoverBuilder:

    # =================================================
    # FULL PAGE BACKGROUND
    # =================================================

    @staticmethod
    def draw_background(canvas, doc):

        page_width = doc.pagesize[0]
        page_height = doc.pagesize[1]

        canvas.drawImage(

            GREEN_BUBBLE,

            0,
            0,

            width=page_width,
            height=page_height,

            preserveAspectRatio=False,
            mask='auto'
        )

    # =================================================
    # COVER CONTENT
    # =================================================

    @staticmethod
    def build(title):

        styles = getSampleStyleSheet()

        centered = ParagraphStyle(

            "centered",

            parent=styles["Title"],

            alignment=TA_CENTER,

            fontSize=30,

            leading=36,

            textColor=colors.HexColor(
                PdfTheme.PRIMARY
            )
        )

        elements = []

        # =================================================
        # TOP SPACE
        # =================================================

        elements.append(
            Spacer(1, 115)
        )

        # =================================================
        # PARROT LEFT CENTER
        # =================================================

        parrot = Image(

            PARROT,

            width=50 * mm,

            height=50 * mm
        )

        parrot_table = Table(

            [[parrot]],

            colWidths=[250 * mm]
        )

        parrot_table.setStyle(

            TableStyle([

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "LEFT"
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    88
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
                    30
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    0
                ),
            ])
        )

        elements.append(
            parrot_table
        )

        # =================================================
        # SPACE BEFORE TITLE
        # =================================================

        elements.append(
            Spacer(1, 280)
        )

        # =================================================
        # TITLE BOTTOM CENTER
        # =================================================

        elements.append(

            Paragraph(
                title.upper(),
                centered
            )
        )

        # =================================================
        # END PAGE
        # =================================================

        elements.append(
            PageBreak()
        )

        return elements