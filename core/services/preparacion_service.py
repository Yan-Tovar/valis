from core.services.base_service import (
    BaseService
)

from core.repositories.preparacion_repository import (
    PreparacionRepository
)

from core.repositories.preparacion_rules import (
    PreparacionRules
)


class PreparacionService(BaseService):


    def __init__(self):

        super().__init__()

        self.repository = PreparacionRepository(
            self.session
        )


    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(self, data):

        PreparacionRules.validate_codigo(
            data.get("codigo_preparacion")
        )

        return self.repository.create(data)


    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        preparacion_id,
        data
    ):

        if "codigo_preparacion" in data:

            PreparacionRules.validate_codigo(
                data.get("codigo_preparacion")
            )

        return self.repository.update(
            preparacion_id,
            data
        )


    # ---------------------------------------------------------
    # GET ALL
    # ---------------------------------------------------------

    def get_all(self):

        return self.repository.get_all()


    # ---------------------------------------------------------
    # GET BY ID
    # ---------------------------------------------------------

    def get_by_id(
        self,
        preparacion_id
    ):

        return self.repository.get_by_id(
            preparacion_id
        )


    # ---------------------------------------------------------
    # SOFT DELETE
    # ---------------------------------------------------------

    def soft_delete(
        self,
        preparacion_id
    ):

        return self.repository.soft_delete(
            preparacion_id
        )


    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        preparacion_id
    ):

        return self.repository.restore(
            preparacion_id
        )


    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        preparacion_id
    ):

        return self.repository.hard_delete(
            preparacion_id
        )