from sqlalchemy import Column, String, Date, Text
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin


class Contrato(Base, BaseMixin):

    __tablename__ = "contratos"

    nombre = Column(String)

    fecha_inicio = Column(Date)

    fecha_fin = Column(Date)

    descripcion = Column(Text)

    entidades_rel = relationship(
        "EntidadContrato",
        back_populates="contrato"
    )