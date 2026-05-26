from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin
from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)

class Preparacion(Base, BaseMixin, SoftDeleteMixin):

    __tablename__ = "preparaciones"

    codigo_preparacion = Column(
        String,
        unique=True
    )

    estudio_id = Column(
        Integer,
        ForeignKey("estudios.id")
    )

    nombre = Column(String)

    estudio = relationship(
        "Estudio",
        back_populates="preparaciones"
    )

    listas_rel = relationship(
        "ListaPreparacionPreparacion",
        back_populates="preparacion"
    )