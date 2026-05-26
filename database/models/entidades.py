from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship

from database.base import Base, BaseMixin
from database.mixins.soft_delete_mixin import (
    SoftDeleteMixin
)

import datetime


class Entidad(Base, BaseMixin, SoftDeleteMixin):

    __tablename__ = "entidades"

    codigo_entidad = Column(
        String,
        unique=True,
        nullable=False
    )

    nombre = Column(String)

    ubicacion = Column(String)

    fecha_registro = Column(
        Date,
        default=datetime.date.today
    )

    contratos_rel = relationship(
        "EntidadContrato",
        back_populates="entidad"
    )

    recomendaciones = relationship(
        "RecomendacionEntidad",
        back_populates="entidad"
    )