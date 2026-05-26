from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin


class ListaPreparacionPreparacion(Base, BaseMixin):

    __tablename__ = "lista_preparaciones_preparaciones"

    preparacion_id = Column(
        Integer,
        ForeignKey("preparaciones.id")
    )

    lista_preparacion_id = Column(
        Integer,
        ForeignKey("lista_preparaciones.id")
    )

    observacion = Column(Text)

    preparacion = relationship(
        "Preparacion",
        back_populates="listas_rel"
    )

    lista_preparacion = relationship(
        "ListaPreparacion",
        back_populates="preparaciones_rel"
    )