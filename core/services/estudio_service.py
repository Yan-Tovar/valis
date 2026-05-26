from auth.session_manager import SessionManager

from core.security.permissions import (
    Permissions
)

from core.services.base_service import (
    BaseService
)

from core.repositories.estudio_repository import (
    EstudioRepository
)

from core.repositories.estudio_rules import (
    EstudioRules
)


class EstudioService(BaseService):


    def __init__(self):

        super().__init__()

        self.repository = (
            EstudioRepository(
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
        estudio_id
    ):

        return self.repository.get_by_id(
            estudio_id
        )

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(
        self,
        data
    ):

        EstudioRules.validate_sigla(
            data.get("sigla")
        )

        return self.repository.create(
            data
        )

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        estudio_id,
        data
    ):

        if "sigla" in data:

            EstudioRules.validate_sigla(
                data.get("sigla")
            )

        return self.repository.update(
            estudio_id,
            data
        )

    # ---------------------------------------------------------
    # SOFT DELETE
    # ---------------------------------------------------------

    def soft_delete(
        self,
        estudio_id
    ):

        return self.repository.soft_delete(
            estudio_id
        )

    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        estudio_id
    ):

        return self.repository.restore(
            estudio_id
        )

    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        estudio_id
    ):

        return self.repository.hard_delete(
            estudio_id
        )