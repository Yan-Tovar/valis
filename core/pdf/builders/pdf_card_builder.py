from reportlab.platypus import (
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import (
    TA_LEFT,
    TA_CENTER
)

from reportlab.lib.units import mm

from reportlab.platypus.flowables import (
    KeepTogether
)

from core.pdf.theme.pdf_theme import PdfTheme


class PdfCardBuilder:

    @staticmethod
    def build(record_dict):

        styles = getSampleStyleSheet()

        # =================================================
        # DATA
        # =================================================

        record_id = str(
            record_dict.get("id", "0")
        )

        values = list(record_dict.values())

        title = (
            str(values[1])
            if len(values) > 1
            else "Registro"
        )

        # =================================================
        # STATUS COLOR
        # =================================================

        activo = str(
            record_dict.get(
                "estado",
                ""
            )
        ).strip().upper()

        status_color = (
            colors.green
            if activo == "ACTIVO"
            else colors.red
        )

        # =================================================
        # FIELDS
        # =================================================

        fields = []

        for key, value in record_dict.items():

            if key.lower() == "id":
                continue

            if value is None:
                continue

            value = str(value).strip()

            if not value:
                continue

            label = key.replace(
                "_",
                " "
            ).title()

            # Estado solo color
            if value.upper() in [
                "ACTIVO",
                "INACTIVO"
            ]:

                value = f"""
                    <font color="{status_color}">
                        {value}
                    </font>
                """

            fields.append(
                [
                    Paragraph(
                        label,
                        ParagraphStyle(
                            "label",
                            parent=styles["BodyText"],
                            fontName="Helvetica-Bold",
                            fontSize=6,
                            leading=7,
                            textColor=colors.HexColor(
                                PdfTheme.TEXT_SECONDARY
                            ),
                            alignment=TA_LEFT
                        )
                    ),

                    Paragraph(
                        value,
                        ParagraphStyle(
                            "value",
                            parent=styles["BodyText"],
                            fontSize=7,
                            leading=8,
                            textColor=colors.HexColor(
                                PdfTheme.TEXT
                            ),
                            alignment=TA_LEFT
                        )
                    )
                ]
            )

        # =================================================
        # ID BADGE
        # =================================================

        badge = Table(

            [[
                Paragraph(
                    record_id,
                    ParagraphStyle(
                        "number",
                        parent=styles["BodyText"],
                        fontName="Helvetica-Bold",
                        fontSize=10,
                        alignment=TA_CENTER,
                        textColor=colors.white
                    )
                )
            ]],

            colWidths=[12 * mm],
            rowHeights=[12 * mm]
        )

        badge.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor(
                        PdfTheme.PRIMARY
                    )
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "ROUNDEDCORNERS",
                    (0, 0),
                    (-1, -1),
                    20
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
        # CONTENT TABLE
        # =================================================

        info_table = Table(

            [
                [
                    Paragraph(
                        title,
                        ParagraphStyle(
                            "title",
                            parent=styles["BodyText"],
                            fontName="Helvetica-Bold",
                            fontSize=9,
                            leading=10,
                            textColor=colors.HexColor(
                                PdfTheme.PRIMARY_DARK
                            )
                        )
                    )
                ],

                [
                    Table(
                        fields,
                        colWidths=[
                            32 * mm,
                            78 * mm
                        ]
                    )
                ]
            ],

            colWidths=[110 * mm]
        )

        info_table.setStyle(

            TableStyle([

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
                    2
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),
            ])
        )

        # =================================================
        # MAIN CONTENT
        # =================================================

        content = Table(

            [[
                badge,
                info_table
            ]],

            colWidths=[
                18 * mm,
                120 * mm
            ]
        )

        content.setStyle(

            TableStyle([

                (
                    "VALIGN",
                    (0, 0),
                    (0, 0),
                    "MIDDLE"
                ),

                (
                    "VALIGN",
                    (1, 0),
                    (1, 0),
                    "TOP"
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
        # FINAL CARD
        # =================================================

        card = Table(

            [[content]],

            colWidths=[165 * mm]
        )

        card.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor(
                        PdfTheme.CARD
                    )
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor(
                        PdfTheme.BORDER
                    )
                ),

                (
                    "ROUNDEDCORNERS",
                    (0, 0),
                    (-1, -1),
                    PdfTheme.CARD_RADIUS
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    6
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    6
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    6
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    6
                ),
            ])
        )

        return [

            KeepTogether([

                card,

                Spacer(1, 3)
            ])
        ]