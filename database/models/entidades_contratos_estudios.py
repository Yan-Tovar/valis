from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin


class EntidadContratoEstudio(Base, BaseMixin):

    __tablename__ = "entidades_contratos_estudios"

    entidad_contrato_id = Column(
        Integer,
        ForeignKey("entidades_contratos.id")
    )

    estudio_id = Column(
        Integer,
        ForeignKey("estudios.id")
    )

    valor_estudio = Column(Float)

    entidad_contrato = relationship(
        "EntidadContrato",
        back_populates="estudios_rel"
    )

    estudio = relationship(
        "Estudio",
        back_populates="entidades_contratos"
    )