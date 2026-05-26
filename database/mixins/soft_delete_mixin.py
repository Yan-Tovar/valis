from sqlalchemy import Column
from sqlalchemy import String


class SoftDeleteMixin:

    estado = Column(
        String(20),
        default="ACTIVO",
        nullable=False
    )

    ACTIVE_STATE = "ACTIVO"

    INACTIVE_STATE = "INACTIVO"

    @classmethod
    def supports_soft_delete(cls):

        return True