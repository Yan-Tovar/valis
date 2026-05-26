from sqlalchemy import Column, String

from database.base import Base, BaseMixin
from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)

class Usuario(Base, BaseMixin, SoftDeleteMixin):

    __tablename__ = "usuarios"

    nombre_usuario = Column(
        String,
        unique=True,
        nullable=False
    )

    nombre_completo = Column(String)

    rol = Column(String)

    password = Column(String)