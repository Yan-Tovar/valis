from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin
from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)

class Sala(Base, BaseMixin, SoftDeleteMixin):

    __tablename__ = "salas"

    codigo_sala = Column(
        String,
        unique=True,
        nullable=False
    )

    nombre = Column(String)

    sede = Column(String)

    localizacion = Column(String)

    representante = Column(String)

    estudios_rel = relationship(
        "EstudioSala",
        back_populates="sala"
    )