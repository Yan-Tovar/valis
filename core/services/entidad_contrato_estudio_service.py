from core.services.base_service import (
    BaseService
)

from core.repositories.entidad_contrato_estudio_repository import (
    EntidadContratoEstudioRepository
)


class EntidadContratoEstudioService(
    BaseService
):


    def __init__(self):

        super().__init__()

        self.repository = (
            EntidadContratoEstudioRepository(
                self.session
            )
        )

    # -------------------------------------------------
    # GET ALL
    # -------------------------------------------------

    def get_all(self):

        return self.repository.get_all()


    # -------------------------------------------------
    # CREATE
    # -------------------------------------------------

    def create(
        self,
        data
    ):

        return self.repository.create(
            data
        )


    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    def update(
        self,
        entity_id,
        data
    ):

        return self.repository.update(
            entity_id,
            data
        )


    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        entity_id
    ):

        return self.repository.hard_delete(
            entity_id
        )