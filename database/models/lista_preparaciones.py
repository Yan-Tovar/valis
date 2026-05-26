from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin
from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)


class ListaPreparacion(Base, BaseMixin, SoftDeleteMixin):

    __tablename__ = "lista_preparaciones"

    nombre = Column(String)

    detalle = Column(Text)

    preparaciones_rel = relationship(
        "ListaPreparacionPreparacion",
        back_populates="lista_preparacion"
    )