from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin


class EstudioSala(Base, BaseMixin):

    __tablename__ = "estudios_salas"

    estudio_id = Column(
        Integer,
        ForeignKey("estudios.id")
    )

    sala_id = Column(
        Integer,
        ForeignKey("salas.id")
    )

    observaciones = Column(Text)

    estudio = relationship(
        "Estudio",
        back_populates="salas_rel"
    )

    sala = relationship(
        "Sala",
        back_populates="estudios_rel"
    )