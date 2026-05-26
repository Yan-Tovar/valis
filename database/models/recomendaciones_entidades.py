from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin
from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)

class RecomendacionEntidad(Base, BaseMixin, SoftDeleteMixin):

    __tablename__ = "recomendaciones_entidades"

    titulo = Column(String)

    entidad_id = Column(
        Integer,
        ForeignKey("entidades.id")
    )

    descripcion = Column(Text)

    entidad = relationship(
        "Entidad",
        back_populates="recomendaciones"
    )