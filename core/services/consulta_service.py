from core.services.base_service import BaseService

from core.repositories.estudio_repository import EstudioRepository
from core.repositories.estudio_sala_repository import EstudioSalaRepository
from core.repositories.entidad_contrato_estudio_repository import EntidadContratoEstudioRepository
from core.repositories.preparacion_repository import PreparacionRepository
from core.repositories.lista_preparacion_preparacion_repository import ListaPreparacionPreparacionRepository
from core.repositories.entidad_contrato_repository import EntidadContratoRepository
from core.repositories.entidad_repository import EntidadRepository
from core.repositories.sala_repository import SalaRepository
from core.repositories.lista_preparacion_repository import ListaPreparacionRepository
from core.repositories.recomendacion_estudio_repository import RecomendacionEstudioRepository
from core.repositories.recomendacion_entidad_repository import RecomendacionEntidadRepository

from core.database.response import Response
from core.database.serializer import Serializer


class ConsultaService(BaseService):

    def __init__(self):

        super().__init__()

        self.estudio_repo = EstudioRepository(
            self.session
        )

        self.estudio_sala_repo = EstudioSalaRepository(
            self.session
        )

        self.entidad_contrato_estudio_repo = EntidadContratoEstudioRepository(
            self.session
        )

        self.preparacion_repo = PreparacionRepository(
            self.session
        )

        self.lista_preparacion_preparacion_repo = ListaPreparacionPreparacionRepository(
            self.session
        )

        self.entidad_contrato_repo = EntidadContratoRepository(
            self.session
        )

        self.entidad_repo = EntidadRepository(
            self.session
        )

        self.sala_repo = SalaRepository(
            self.session
        )

        self.lista_preparacion_repo = ListaPreparacionRepository(
            self.session
        )

        self.recomendacion_estudio_repo = RecomendacionEstudioRepository(
            self.session
        )

        self.recomendacion_entidad_repo = RecomendacionEntidadRepository(
            self.session
        )

    # ---------------------------------------------------------
    # GET ESTUDIOS POR ENTIDAD
    # ---------------------------------------------------------

    def get_estudios_por_entidad(
        self,
        entidad_id,
        query_text
    ):

        """
        Busca estudios asociados a una entidad específica.
        """

        try:

            entidad = self.session.query(

                self.entidad_repo.model

            ).filter(

                self.entidad_repo.model.id == entidad_id,
                self.entidad_repo.model.estado == "ACTIVO"

            ).first()

            if not entidad:

                return Response.error(
                    "La entidad no existe"
                )

            # -------------------------------------------------
            # VALIDAR CONTRATOS
            # -------------------------------------------------

            entidad_contratos = self.session.query(

                self.entidad_contrato_repo.model

            ).filter(

                self.entidad_contrato_repo.model.entidad_id == entidad_id

            ).all()

            if not entidad_contratos:

                return Response.error(
                    "La entidad no tiene contratos asociados"
                )

            # -------------------------------------------------
            # BUSCAR ESTUDIOS
            # -------------------------------------------------

            estudios_query = self.session.query(

                self.entidad_contrato_estudio_repo.model

            ).join(

                self.entidad_contrato_estudio_repo.model.estudio

            ).join(

                self.entidad_contrato_estudio_repo.model.entidad_contrato

            ).filter(

                self.entidad_contrato_repo.model.entidad_id == entidad_id

            )

            # ---------------------------------------------
            # FILTRO POR CODIGO O NOMBRE
            # ---------------------------------------------

            if query_text:

                estudios_query = estudios_query.filter(

                    (
                        self.estudio_repo.model.codigo_cups.ilike(
                            f"%{query_text}%"
                        )
                    )

                    |

                    (
                        self.estudio_repo.model.nombre.ilike(
                            f"%{query_text}%"
                        )
                    )
                )

            estudios_rel = estudios_query.all()

            if not estudios_rel:

                return Response.error(
                    "No hay estudios relacionados con esta entidad"
                )

            estudios_data = []

            added = set()

            for rel in estudios_rel:

                estudio = rel.estudio

                if estudio.estado != "ACTIVO":
                    continue

                if estudio.id in added:
                    continue

                added.add(estudio.id)

                estudios_data.append({

                    "entidad_contrato_estudio_id": rel.id,

                    "estudio_id": estudio.id,

                    "codigo_cups": estudio.codigo_cups,

                    "nombre": estudio.nombre,

                    "sigla": estudio.sigla,

                    "valor_estudio": rel.valor_estudio
                })

            if not estudios_data:

                return Response.error(
                    "No hay estudios activos para esta entidad"
                )

            return Response.success(
                data=estudios_data
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # SEARCH ESTUDIO
    # ---------------------------------------------------------

    def search_estudio(
        self,
        query_text
    ):

        """
        Busca un estudio por código, nombre o ID.
        Solo retorna estudios en estado ACTIVO.
        """

        columns = ["codigo_cups", "nombre"]

        return self.estudio_repo.search(
            query_text,
            columns=columns,
            include_inactive=False
        )

    # ---------------------------------------------------------
    # GET SALAS POR ESTUDIO
    # ---------------------------------------------------------

    def get_salas_por_estudio(
        self,
        estudio_id
    ):

        """
        Obtiene las salas donde se puede realizar un estudio.
        """

        try:

            # Buscar en EstudioSala por estudio_id
            estudio_sala_records = self.session.query(

                self.estudio_sala_repo.model

            ).filter(

                self.estudio_sala_repo.model.estudio_id == estudio_id

            ).all()

            if not estudio_sala_records:

                return Response.error(
                    "No hay salas disponibles para este estudio"
                )

            # Enriquecer con datos de Sala
            salas_data = []

            for es in estudio_sala_records:

                sala = es.sala

                salas_data.append({

                    "estudio_sala_id": es.id,
                    "sala_id": sala.id,
                    "codigo_sala": sala.codigo_sala,
                    "nombre": sala.nombre,
                    "sede": sala.sede,
                    "localizacion": sala.localizacion,
                    "observaciones": es.observaciones
                })

            return Response.success(
                data=salas_data
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # GET ENTIDADES POR ESTUDIO
    # ---------------------------------------------------------

    def get_entidades_por_estudio(
        self,
        estudio_id
    ):

        """
        Obtiene todas las entidades que tienen contrato con ese estudio.
        Solo entidades activas.
        """

        try:

            # Buscar en EntidadContratoEstudio
            ece_records = self.session.query(

                self.entidad_contrato_estudio_repo.model

            ).filter(

                self.entidad_contrato_estudio_repo.model.estudio_id == estudio_id

            ).all()

            if not ece_records:

                return Response.error(
                    "No hay entidades con contrato para este estudio"
                )

            entidades_data = []

            for ece in ece_records:

                entidad_contrato = ece.entidad_contrato
                entidad = entidad_contrato.entidad

                # Solo si está activa
                if entidad.estado != "ACTIVO":
                    continue

                entidades_data.append({

                    "entidad_id": entidad.id,
                    "entidad_contrato_id": entidad_contrato.id,
                    "entidad_contrato_estudio_id": ece.id,
                    "codigo_entidad": entidad.codigo_entidad,
                    "nombre_entidad": entidad.nombre,
                    "ubicacion": entidad.ubicacion,
                    "valor_estudio": ece.valor_estudio
                })

            if not entidades_data:

                return Response.error(
                    "No hay entidades activas con contrato para este estudio"
                )

            return Response.success(
                data=entidades_data
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # SEARCH ENTIDAD (CON CONTRATOS)
    # ---------------------------------------------------------

    def search_entidad(
        self,
        query_text
    ):

        """
        Busca una entidad por código, nombre o ID.
        Solo retorna entidades ACTIVAS que tengan contratos asociados.
        
        Una entidad es válida para esta búsqueda si:
        - Estado es ACTIVO
        - Tiene al menos un contrato en la tabla entidades_contratos
        """

        try:

            # -------------------------------------------------
            # CONSULTA CON FILTRO DE CONTRATO
            # -------------------------------------------------

            query = self.session.query(

                self.entidad_repo.model

            ).join(

                self.entidad_contrato_repo.model,

                self.entidad_repo.model.id == self.entidad_contrato_repo.model.entidad_id

            ).filter(

                self.entidad_repo.model.estado == "ACTIVO"

            ).distinct()

            # -------------------------------------------------
            # APLICAR FILTRO DE BÚSQUEDA
            # -------------------------------------------------

            if query_text:

                query = query.filter(

                    (
                        self.entidad_repo.model.codigo_entidad.ilike(
                            f"%{query_text}%"
                        )
                    )

                    |

                    (
                        self.entidad_repo.model.nombre.ilike(
                            f"%{query_text}%"
                        )
                    )
                )

            entidades = query.all()

            if not entidades:

                return Response.error(
                    "No se encontraron entidades con contratos activos"
                )

            # -------------------------------------------------
            # SERIALIZAR RESPUESTA
            # -------------------------------------------------

            entidades_data = []

            for entidad in entidades:

                entidades_data.append({

                    "id": entidad.id,

                    "codigo_entidad": entidad.codigo_entidad,

                    "nombre": entidad.nombre,

                    "nombre_entidad": entidad.nombre

                })

            return Response.success(
                data=entidades_data
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # GET PREPARACION POR ESTUDIO
    # ---------------------------------------------------------

    def get_preparacion_por_estudio(
        self,
        estudio_id
    ):

        """
        Obtiene la preparación asociada a un estudio.
        Solo preparaciones en estado ACTIVO.
        """

        try:

            prep = self.session.query(

                self.preparacion_repo.model

            ).filter(

                self.preparacion_repo.model.estudio_id == estudio_id,
                self.preparacion_repo.model.estado == "ACTIVO"

            ).first()

            if not prep:

                return Response.error(
                    "No hay preparación disponible para este estudio"
                )

            return Response.success(
                data=Serializer.to_dict(prep)
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # GET LISTA PREPARACIONES POR PREPARACION
    # ---------------------------------------------------------

    def get_lista_preparaciones_por_preparacion(
        self,
        preparacion_id
    ):

        """
        Obtiene la lista de preparaciones asociadas a una preparación.
        Solo listas en estado ACTIVO.
        """

        try:

            lpp_records = self.session.query(

                self.lista_preparacion_preparacion_repo.model

            ).filter(

                self.lista_preparacion_preparacion_repo.model.preparacion_id == preparacion_id

            ).all()

            if not lpp_records:

                return Response.error(
                    "No hay lista de preparaciones para esta preparación"
                )

            listas_data = []

            for lpp in lpp_records:

                lista = lpp.lista_preparacion

                # Solo si está activa
                if lista.estado != "ACTIVO":
                    continue

                listas_data.append({

                    "lista_preparacion_preparacion_id": lpp.id,
                    "lista_preparacion_id": lista.id,
                    "nombre": lista.nombre,
                    "detalle": lista.detalle,
                    "observacion": lpp.observacion
                })

            if not listas_data:

                return Response.error(
                    "No hay lista de preparaciones activas para esta preparación"
                )

            return Response.success(
                data=listas_data
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # GET CONTRATO DETALLE
    # ---------------------------------------------------------

    def get_contrato_detalle(
        self,
        entidad_contrato_estudio_id
    ):

        """
        Obtiene detalles del contrato entre entidad, contrato y estudio.
        """

        try:

            ece = self.session.query(

                self.entidad_contrato_estudio_repo.model

            ).filter(

                self.entidad_contrato_estudio_repo.model.id == entidad_contrato_estudio_id

            ).first()

            if not ece:

                return Response.error(
                    "No se encontró el contrato"
                )

            entidad_contrato = ece.entidad_contrato
            entidad = entidad_contrato.entidad
            contrato = entidad_contrato.contrato

            contrato_data = {

                "entidad_contrato_id": entidad_contrato.id,
                "entidad_contrato_estudio_id": ece.id,
                "entidad_id": entidad.id,
                "codigo_entidad": entidad.codigo_entidad,
                "nombre_entidad": entidad.nombre,
                "ubicacion": entidad.ubicacion,
                "contrato_id": contrato.id,
                "nombre_contrato": contrato.nombre,
                "fecha_inicio": str(contrato.fecha_inicio) if contrato.fecha_inicio else None,
                "fecha_fin": str(contrato.fecha_fin) if contrato.fecha_fin else None,
                "descripcion_contrato": contrato.descripcion,
                "observaciones": entidad_contrato.observaciones,
                "valor_estudio": ece.valor_estudio
            }

            return Response.success(
                data=contrato_data
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # GET RECOMENDACIONES POR ESTUDIO
    # ---------------------------------------------------------

    def get_recomendaciones_por_estudio(
        self,
        estudio_id
    ):

        """
        Obtiene recomendaciones asociadas a un estudio.
        """

        try:

            recs = self.session.query(
                self.recomendacion_estudio_repo.model
            ).filter(
                self.recomendacion_estudio_repo.model.estudio_id == estudio_id
            ).all()

            return Response.success(
                data=[{
                    "id": rec.id,
                    "titulo": rec.titulo,
                    "descripcion": rec.descripcion
                } for rec in recs]
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # GET RECOMENDACIONES POR ENTIDAD
    # ---------------------------------------------------------

    def get_recomendaciones_por_entidad(
        self,
        entidad_id
    ):

        """
        Obtiene recomendaciones asociadas a una entidad.
        """

        try:

            recs = self.session.query(
                self.recomendacion_entidad_repo.model
            ).filter(
                self.recomendacion_entidad_repo.model.entidad_id == entidad_id
            ).all()

            return Response.success(
                data=[{
                    "id": rec.id,
                    "titulo": rec.titulo,
                    "descripcion": rec.descripcion
                } for rec in recs]
            )

        except Exception as e:

            return Response.error(str(e))

    # ---------------------------------------------------------
    # FLUJO COMPLETO
    # ---------------------------------------------------------

    def get_flujo_completo(
        self,
        entidad_id,
        estudio_id
        
    ):

        """
        Obtiene todo lo necesario para una consulta completa:
        - Datos del estudio
        - Salas disponibles
        - Contrato con entidad
        - Preparación
        - Lista de preparaciones
        """

        try:

            # 1. Obtener entidad

            entidad_response = self.entidad_repo.get_by_id(
                entidad_id
            )

            if not entidad_response.success:
                return entidad_response

            entidad_data = entidad_response.data


            # 2. Obtener estudio

            estudio_response = self.estudio_repo.get_by_id(
                estudio_id
            )

            if not estudio_response.success:
                return estudio_response

            estudio_data = estudio_response.data

            # 3. Obtener salas
            salas_response = self.get_salas_por_estudio(
                estudio_id
            )

            if not salas_response.success:
                return salas_response

            salas_data = salas_response.data

            # 4. Obtener contrato (EntidadContratoEstudio)
            ece_record = self.session.query(

                self.entidad_contrato_estudio_repo.model

            ).join(

                self.entidad_contrato_estudio_repo.model.entidad_contrato

            ).filter(

                self.entidad_contrato_estudio_repo.model.estudio_id == estudio_id,
                self.entidad_contrato_repo.model.entidad_id == entidad_id

            ).first()

            if not ece_record:

                return Response.error(
                    "No hay contrato disponible para esta entidad en este estudio"
                )

            contrato_response = self.get_contrato_detalle(
                ece_record.id
            )

            if not contrato_response.success:
                return contrato_response

            contrato_data = contrato_response.data

            # 5. Obtener preparación
            prep_response = self.get_preparacion_por_estudio(
                estudio_id
            )

            if not prep_response.success:
                return prep_response

            preparacion_data = prep_response.data

            # 6. Obtener lista de preparaciones
            listas_response = self.get_lista_preparaciones_por_preparacion(
                preparacion_data["id"]
            )

            if not listas_response.success:
                return listas_response

            listas_data = listas_response.data

            rec_estudio_response = self.get_recomendaciones_por_estudio(
                estudio_id
            )

            if not rec_estudio_response.success:
                return rec_estudio_response

            rec_entidad_response = self.get_recomendaciones_por_entidad(
                entidad_id
            )

            if not rec_entidad_response.success:
                return rec_entidad_response

            recomendaciones_estudio_data = rec_estudio_response.data
            recomendaciones_entidad_data = rec_entidad_response.data

            # Compilar resultado completo
            resultado = {

                "estudio": estudio_data,
                "salas": salas_data,
                "entidad": entidad_data,
                "contrato": contrato_data,
                "preparacion": preparacion_data,
                "lista_preparaciones": listas_data,
                "recomendaciones_estudio": recomendaciones_estudio_data,
                "recomendaciones_entidad": recomendaciones_entidad_data
            }

            return Response.success(
                data=resultado
            )

        except Exception as e:

            return Response.error(str(e))
