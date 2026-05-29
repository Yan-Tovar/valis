from reportlab.platypus import (
    Spacer
)

from core.pdf.builders.pdf_cover_builder import (
    PdfCoverBuilder
)

from core.pdf.builders.pdf_header_builder import (
    PdfHeaderBuilder
)

from core.pdf.builders.pdf_card_builder import (
    PdfCardBuilder
)

from core.pdf.builders.pdf_footer_builder import (
    PdfFooterBuilder
)


class DefaultPdfTemplate:

    # =====================================
    # ELEMENTS
    # =====================================

    @staticmethod
    def build(
        model_name,
        records
    ):

        elements = []

        # =====================================
        # COVER
        # =====================================

        elements.extend(

            PdfCoverBuilder.build(
                title=model_name
            )
        )

        # =====================================
        # HEADER
        # =====================================

        elements.append(

            PdfHeaderBuilder.build(
                title=model_name,
                total=len(records)
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # =====================================
        # RECORDS
        # =====================================

        for record in records:

            elements.extend(

                PdfCardBuilder.build(
                    record
                )
            )

        # =====================================
        # FOOTER
        # =====================================

        elements.extend(
            PdfFooterBuilder.build()
        )

        return elements

    # =====================================
    # GENERATE PDF
    # =====================================

    @staticmethod
    def build_pdf(
        doc,
        model_name,
        records
    ):

        elements = DefaultPdfTemplate.build(

            model_name=model_name,

            records=records
        )

        doc.build(

            elements,

            # COVER ONLY
            onFirstPage=PdfCoverBuilder.draw_background
        )