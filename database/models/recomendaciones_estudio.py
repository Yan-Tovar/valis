from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin
from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)

class RecomendacionEstudio(Base, BaseMixin):

    __tablename__ = "recomendaciones_estudio"

    titulo = Column(String)

    estudio_id = Column(
        Integer,
        ForeignKey("estudios.id")
    )

    descripcion = Column(Text)

    estudio = relationship(
        "Estudio",
        back_populates="recomendaciones"
    )