from core.services.base_service import (
    BaseService
)

from core.repositories.estudio_sala_repository import (
    EstudioSalaRepository
)


class EstudioSalaService(
    BaseService
):


    def __init__(self):

        super().__init__()

        self.repository = (
            EstudioSalaRepository(
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

        # ---------------------------------------------
        # CONVERTIR IDS
        # ---------------------------------------------

        if data.get("estudio_id"):

            data["estudio_id"] = int(
                data["estudio_id"]
            )

        if data.get("sala_id"):

            data["sala_id"] = int(
                data["sala_id"]
            )

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

        # ---------------------------------------------
        # CONVERTIR IDS
        # ---------------------------------------------

        if data.get("estudio_id"):

            data["estudio_id"] = int(
                data["estudio_id"]
            )

        if data.get("sala_id"):

            data["sala_id"] = int(
                data["sala_id"]
            )

        return self.repository.update(
            entity_id,
            data
        )

    # -------------------------------------------------
    # DELETE
    # -------------------------------------------------

    def soft_delete(
        self,
        entity_id
    ):

        return self.repository.soft_delete(
            entity_id
        )

    # -------------------------------------------------
    # RESTORE
    # -------------------------------------------------

    def restore(
        self,
        entity_id
    ):

        return self.repository.restore(
            entity_id
        )

    # -------------------------------------------------
    # HARD DELETE
    # -------------------------------------------------

    def hard_delete(
        self,
        entity_id
    ):

        return self.repository.hard_delete(
            entity_id
        )