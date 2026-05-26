from core.services.base_service import (
    BaseService
)

from core.repositories.contrato_repository import (
    ContratoRepository
)

from core.repositories.contrato_rules import (
    ContratoRules
)


class ContratoService(BaseService):


    def __init__(self):

        super().__init__()

        self.repository = ContratoRepository(
            self.session
        )


    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(self, data):

        ContratoRules.validate(data)

        return self.repository.create(data)


    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        contrato_id,
        data
    ):

        ContratoRules.validate(data)

        return self.repository.update(
            contrato_id,
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
        contrato_id
    ):

        return self.repository.get_by_id(
            contrato_id
        )


    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        contrato_id
    ):

        return self.repository.hard_delete(
            contrato_id
        )