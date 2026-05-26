from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin
from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)


class Estudio(Base, BaseMixin, SoftDeleteMixin):

    __tablename__ = "estudios"

    codigo_cups = Column(
        String,
        unique=True,
        nullable=False
    )

    nombre = Column(
        String,
        nullable=False
    )

    sigla = Column(String)

    descripcion = Column(Text)

    salas_rel = relationship(
        "EstudioSala",
        back_populates="estudio"
    )

    preparaciones = relationship(
        "Preparacion",
        back_populates="estudio"
    )

    recomendaciones = relationship(
        "RecomendacionEstudio",
        back_populates="estudio"
    )

    entidades_contratos = relationship(
        "EntidadContratoEstudio",
        back_populates="estudio"
    )