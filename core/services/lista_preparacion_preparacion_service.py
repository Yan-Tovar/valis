from core.services.base_service import (
    BaseService
)

from core.repositories.lista_preparacion_preparacion_repository import (
    ListaPreparacionPreparacionRepository
)


class ListaPreparacionPreparacionService(
    BaseService
):


    def __init__(self):

        super().__init__()

        self.repository = (
            ListaPreparacionPreparacionRepository(
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

        if data.get("preparacion_id"):

            data["preparacion_id"] = int(
                data["preparacion_id"]
            )

        if data.get("lista_preparacion_id"):

            data["lista_preparacion_id"] = int(
                data["lista_preparacion_id"]
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

        if data.get("preparacion_id"):

            data["preparacion_id"] = int(
                data["preparacion_id"]
            )

        if data.get("lista_preparacion_id"):

            data["lista_preparacion_id"] = int(
                data["lista_preparacion_id"]
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