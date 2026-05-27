from datetime import date

from sqlalchemy import func, distinct

from core.services.base_service import BaseService

from core.repositories.entidad_repository import (
    EntidadRepository
)

from core.repositories.estudio_repository import (
    EstudioRepository
)

from core.repositories.contrato_repository import (
    ContratoRepository
)

from core.repositories.entidad_contrato_repository import (
    EntidadContratoRepository
)

from core.repositories.entidad_contrato_estudio_repository import (
    EntidadContratoEstudioRepository
)

from core.repositories.estudio_sala_repository import (
    EstudioSalaRepository
)

from core.repositories.sala_repository import (
    SalaRepository
)

from core.repositories.preparacion_repository import (
    PreparacionRepository
)

from core.repositories.lista_preparacion_preparacion_repository import (
    ListaPreparacionPreparacionRepository
)

from core.repositories.recomendacion_estudio_repository import (
    RecomendacionEstudioRepository
)

from core.repositories.recomendacion_entidad_repository import (
    RecomendacionEntidadRepository
)

from core.repositories.usuario_repository import (
    UsuarioRepository
)

from core.database.response import Response


class DashboardStatisticsService(BaseService):

    def __init__(self):

        super().__init__()

        self.entidad_repo = EntidadRepository(
            self.session
        )

        self.estudio_repo = EstudioRepository(
            self.session
        )

        self.contrato_repo = ContratoRepository(
            self.session
        )

        self.entidad_contrato_repo = (
            EntidadContratoRepository(
                self.session
            )
        )

        self.entidad_contrato_estudio_repo = (
            EntidadContratoEstudioRepository(
                self.session
            )
        )

        self.estudio_sala_repo = (
            EstudioSalaRepository(
                self.session
            )
        )

        self.sala_repo = SalaRepository(
            self.session
        )

        self.preparacion_repo = (
            PreparacionRepository(
                self.session
            )
        )

        self.lista_preparacion_preparacion_repo = (
            ListaPreparacionPreparacionRepository(
                self.session
            )
        )

        self.recomendacion_estudio_repo = (
            RecomendacionEstudioRepository(
                self.session
            )
        )

        self.recomendacion_entidad_repo = (
            RecomendacionEntidadRepository(
                self.session
            )
        )

        self.usuario_repo = UsuarioRepository(
            self.session
        )

    # =====================================================
    # 1. KPIS GENERALES
    # =====================================================

    def get_general_kpis(self):

        try:

            data = {

                "total_entidades":

                    self.session.query(
                        self.entidad_repo.model
                    ).count(),

                "total_estudios":

                    self.session.query(
                        self.estudio_repo.model
                    ).count(),

                "total_contratos":

                    self.session.query(
                        self.contrato_repo.model
                    ).count(),

                "total_salas":

                    self.session.query(
                        self.sala_repo.model
                    ).count(),

                "total_preparaciones":

                    self.session.query(
                        self.preparacion_repo.model
                    ).count(),

                "total_usuarios":

                    self.session.query(
                        self.usuario_repo.model
                    ).count()
            }

            return Response.success(
                data=data
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 2. TOP ESTUDIOS MAS CONTRATADOS
    # =====================================================

    def get_top_estudios_mas_contratados(
        self,
        limit=10
    ):

        try:

            records = self.session.query(

                self.estudio_repo.model.nombre,

                func.count(
                    self.entidad_contrato_estudio_repo.model.id
                ).label("cantidad")

            ).join(

                self.entidad_contrato_estudio_repo.model,

                self.estudio_repo.model.id ==
                self.entidad_contrato_estudio_repo.model.estudio_id

            ).group_by(

                self.estudio_repo.model.nombre

            ).order_by(

                func.count(
                    self.entidad_contrato_estudio_repo.model.id
                ).desc()

            ).limit(limit).all()

            return Response.success(
                data=[
                    {
                        "estudio": r[0],
                        "cantidad": r[1]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 3. TOP ENTIDADES CON MAS CONTRATOS
    # =====================================================

    def get_top_entidades_contratantes(
        self,
        limit=10
    ):

        try:

            records = self.session.query(

                self.entidad_repo.model.nombre,

                func.count(
                    self.entidad_contrato_estudio_repo.model.id
                ).label("cantidad")

            ).join(

                self.entidad_contrato_repo.model,

                self.entidad_repo.model.id ==
                self.entidad_contrato_repo.model.entidad_id

            ).join(

                self.entidad_contrato_estudio_repo.model,

                self.entidad_contrato_repo.model.id ==
                self.entidad_contrato_estudio_repo.model.entidad_contrato_id

            ).group_by(

                self.entidad_repo.model.nombre

            ).order_by(

                func.count(
                    self.entidad_contrato_estudio_repo.model.id
                ).desc()

            ).limit(limit).all()

            return Response.success(
                data=[
                    {
                        "entidad": r[0],
                        "cantidad": r[1]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 4. ESTUDIOS POR ENTIDAD
    # =====================================================

    def get_estudios_por_entidad(self):

        try:

            records = self.session.query(

                self.entidad_repo.model.nombre,

                func.count(
                    distinct(
                        self.entidad_contrato_estudio_repo.model.estudio_id
                    )
                ).label("cantidad")

            ).join(

                self.entidad_contrato_repo.model,

                self.entidad_repo.model.id ==
                self.entidad_contrato_repo.model.entidad_id

            ).join(

                self.entidad_contrato_estudio_repo.model,

                self.entidad_contrato_repo.model.id ==
                self.entidad_contrato_estudio_repo.model.entidad_contrato_id

            ).group_by(

                self.entidad_repo.model.nombre

            ).all()

            return Response.success(
                data=[
                    {
                        "entidad": r[0],
                        "cantidad_estudios": r[1]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 5. ESTUDIOS CON MAS SALAS
    # =====================================================

    def get_estudios_con_mas_salas(self):

        try:

            records = self.session.query(

                self.estudio_repo.model.nombre,

                func.count(
                    self.estudio_sala_repo.model.id
                ).label("cantidad")

            ).join(

                self.estudio_sala_repo.model,

                self.estudio_repo.model.id ==
                self.estudio_sala_repo.model.estudio_id

            ).group_by(

                self.estudio_repo.model.nombre

            ).order_by(

                func.count(
                    self.estudio_sala_repo.model.id
                ).desc()

            ).all()

            return Response.success(
                data=[
                    {
                        "estudio": r[0],
                        "cantidad_salas": r[1]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 6. SALAS MAS UTILIZADAS
    # =====================================================

    def get_salas_mas_utilizadas(self):

        try:

            records = self.session.query(

                self.sala_repo.model.nombre,

                func.count(
                    self.estudio_sala_repo.model.id
                ).label("cantidad")

            ).join(

                self.estudio_sala_repo.model,

                self.sala_repo.model.id ==
                self.estudio_sala_repo.model.sala_id

            ).group_by(

                self.sala_repo.model.nombre

            ).order_by(

                func.count(
                    self.estudio_sala_repo.model.id
                ).desc()

            ).all()

            return Response.success(
                data=[
                    {
                        "sala": r[0],
                        "cantidad_estudios": r[1]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 7. ESTUDIOS SIN SALA
    # =====================================================

    def get_estudios_sin_sala(self):

        try:

            records = self.session.query(

                self.estudio_repo.model.nombre

            ).outerjoin(

                self.estudio_sala_repo.model,

                self.estudio_repo.model.id ==
                self.estudio_sala_repo.model.estudio_id

            ).filter(

                self.estudio_sala_repo.model.id == None

            ).all()

            return Response.success(
                data=[
                    {
                        "estudio": r[0]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 8. ESTUDIOS CON PREPARACION
    # =====================================================

    def get_estudios_con_y_sin_preparacion(self):

        try:

            con_preparacion = self.session.query(

                self.preparacion_repo.model

            ).count()

            total_estudios = self.session.query(

                self.estudio_repo.model

            ).count()

            sin_preparacion = (
                total_estudios - con_preparacion
            )

            return Response.success(
                data={

                    "con_preparacion":
                        con_preparacion,

                    "sin_preparacion":
                        sin_preparacion
                }
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 9. PREPARACIONES MAS COMPLEJAS
    # =====================================================

    def get_preparaciones_mas_complejas(self):

        try:

            records = self.session.query(

                self.preparacion_repo.model.nombre,

                func.count(
                    self.lista_preparacion_preparacion_repo.model.id
                ).label("cantidad")

            ).join(

                self.lista_preparacion_preparacion_repo.model,

                self.preparacion_repo.model.id ==
                self.lista_preparacion_preparacion_repo.model.preparacion_id

            ).group_by(

                self.preparacion_repo.model.nombre

            ).order_by(

                func.count(
                    self.lista_preparacion_preparacion_repo.model.id
                ).desc()

            ).all()

            return Response.success(
                data=[
                    {
                        "preparacion": r[0],
                        "cantidad_items": r[1]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 10. CONTRATOS ACTIVOS VS VENCIDOS
    # =====================================================

    def get_contratos_estado(self):

        try:

            today = date.today()

            activos = self.session.query(

                self.contrato_repo.model

            ).filter(

                self.contrato_repo.model.fecha_fin >= today

            ).count()

            vencidos = self.session.query(

                self.contrato_repo.model

            ).filter(

                self.contrato_repo.model.fecha_fin < today

            ).count()

            return Response.success(
                data={

                    "activos": activos,
                    "vencidos": vencidos
                }
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 11. ESTUDIOS CON MAS RECOMENDACIONES
    # =====================================================

    def get_estudios_con_mas_recomendaciones(self):

        try:

            records = self.session.query(

                self.estudio_repo.model.nombre,

                func.count(
                    self.recomendacion_estudio_repo.model.id
                ).label("cantidad")

            ).join(

                self.recomendacion_estudio_repo.model,

                self.estudio_repo.model.id ==
                self.recomendacion_estudio_repo.model.estudio_id

            ).group_by(

                self.estudio_repo.model.nombre

            ).order_by(

                func.count(
                    self.recomendacion_estudio_repo.model.id
                ).desc()

            ).all()

            return Response.success(
                data=[
                    {
                        "estudio": r[0],
                        "cantidad_recomendaciones": r[1]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))

    # =====================================================
    # 12. USUARIOS POR ROL
    # =====================================================

    def get_usuarios_por_rol(self):

        try:

            records = self.session.query(

                self.usuario_repo.model.rol,

                func.count(
                    self.usuario_repo.model.id
                ).label("cantidad")

            ).group_by(

                self.usuario_repo.model.rol

            ).all()

            return Response.success(
                data=[
                    {
                        "rol": r[0],
                        "cantidad": r[1]
                    }
                    for r in records
                ]
            )

        except Exception as e:

            return Response.error(str(e))
        