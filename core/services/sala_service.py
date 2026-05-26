from auth.session_manager import SessionManager

from core.security.permissions import (
    Permissions
)

from core.services.base_service import (
    BaseService
)

from core.repositories.sala_repository import (
    SalaRepository
)

from core.repositories.sala_rules import (
    SalaRules
)


class SalaService(BaseService):


    def __init__(self):

        super().__init__()

        self.repository = (
            SalaRepository(
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
        sala_id
    ):

        return self.repository.get_by_id(
            sala_id
        )

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(
        self,
        data
    ):

        SalaRules.validate_codigo(
            data.get("codigo_sala")
        )

        return self.repository.create(
            data
        )

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        sala_id,
        data
    ):

        if "codigo_sala" in data:

            SalaRules.validate_codigo(
                data.get("codigo_sala")
            )

        return self.repository.update(
            sala_id,
            data
        )

    # ---------------------------------------------------------
    # SOFT DELETE
    # ---------------------------------------------------------

    def soft_delete(
        self,
        sala_id
    ):

        return self.repository.soft_delete(
            sala_id
        )

    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        sala_id
    ):

        return self.repository.restore(
            sala_id
        )

    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        sala_id
    ):

        return self.repository.hard_delete(
            sala_id
        )