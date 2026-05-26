from auth.session_manager import SessionManager

from core.security.permissions import (
    Permissions
)

from core.services.base_service import (
    BaseService
)

from core.repositories.lista_preparacion_repository import (
    ListaPreparacionRepository
)

from core.repositories.lista_preparacion_rules import (
    ListaPreparacionRules
)


class ListaPreparacionService(BaseService):


    def __init__(self):

        super().__init__()

        self.repository = (
            ListaPreparacionRepository(
                self.session
            )
        )

    # ---------------------------------------------------------
    # GET ALL
    # ---------------------------------------------------------

    def get_all(self):

        user = SessionManager.current_user()

        include_inactive = (
            Permissions.can_view_inactive(user)
        )

        return self.repository.get_all(
            include_inactive=include_inactive
        )

    # ---------------------------------------------------------
    # GET BY ID
    # ---------------------------------------------------------

    def get_by_id(
        self,
        lista_id
    ):

        return self.repository.get_by_id(
            lista_id
        )

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(
        self,
        data
    ):

        ListaPreparacionRules.validate_nombre(
            data.get("nombre")
        )

        return self.repository.create(
            data
        )

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        lista_id,
        data
    ):

        if "nombre" in data:

            ListaPreparacionRules.validate_nombre(
                data.get("nombre")
            )

        return self.repository.update(
            lista_id,
            data
        )

    # ---------------------------------------------------------
    # SOFT DELETE
    # ---------------------------------------------------------

    def soft_delete(
        self,
        lista_id
    ):

        return self.repository.soft_delete(
            lista_id
        )

    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        lista_id
    ):

        return self.repository.restore(
            lista_id
        )

    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        lista_id
    ):

        return self.repository.hard_delete(
            lista_id
        )