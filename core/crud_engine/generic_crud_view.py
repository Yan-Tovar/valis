from core.crud_engine.crud_page import (
    CrudPage
)

from core.crud_engine.crud_registry import (
    CRUD_REGISTRY
)


class GenericCrudView:

    def __init__(
        self,
        page,
        module
    ):

        self.page = page

        self.module = module

    # =====================================================
    # BUILD
    # =====================================================

    def build(self):

        config = CRUD_REGISTRY[
            self.module
        ]

        service = config[
            "service"
        ]()

        return CrudPage(

            page=self.page,

            title=config["title"],

            service=service,

            columns=config["columns"],

            fields=config["fields"],

            pdf_enabled=config.get(
                "pdf_enabled",
                False
            )
        ).build()