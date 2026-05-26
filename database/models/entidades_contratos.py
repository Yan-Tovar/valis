from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin


class EntidadContrato(Base, BaseMixin):

    __tablename__ = "entidades_contratos"

    entidad_id = Column(
        Integer,
        ForeignKey("entidades.id")
    )

    contrato_id = Column(
        Integer,
        ForeignKey("contratos.id")
    )

    observaciones = Column(Text)

    entidad = relationship(
        "Entidad",
        back_populates="contratos_rel"
    )

    contrato = relationship(
        "Contrato",
        back_populates="entidades_rel"
    )

    estudios_rel = relationship(
        "EntidadContratoEstudio",
        back_populates="entidad_contrato",
        cascade="all, delete-orphan"
    )