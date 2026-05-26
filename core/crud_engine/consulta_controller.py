from core.services.consulta_service import ConsultaService


class ConsultaController:

    def __init__(self):

        self.service = ConsultaService()

    # ---------------------------------------------------------
    # SEARCH ESTUDIO
    # ---------------------------------------------------------

    def search_estudio(self, query_text):

        return self.service.search_estudio(query_text)

    # ---------------------------------------------------------
    # SEARCH ESTUDIOS POR ENTIDAD
    # ---------------------------------------------------------

    def search_estudios_por_entidad(self, entidad_id, query_text):

        return self.service.get_estudios_por_entidad(
            entidad_id,
            query_text
        )

    # ---------------------------------------------------------
    # GET SALAS POR ESTUDIO
    # ---------------------------------------------------------

    def get_salas_por_estudio(self, estudio_id):

        return self.service.get_salas_por_estudio(estudio_id)

    # ---------------------------------------------------------
    # GET ENTIDADES POR ESTUDIO
    # ---------------------------------------------------------

    def get_entidades_por_estudio(self, estudio_id):

        return self.service.get_entidades_por_estudio(estudio_id)

    # ---------------------------------------------------------
    # SEARCH ENTIDAD
    # ---------------------------------------------------------

    def search_entidad(self, query_text):

        return self.service.search_entidad(query_text)

    # ---------------------------------------------------------
    # GET PREPARACION POR ESTUDIO
    # ---------------------------------------------------------

    def get_preparacion_por_estudio(self, estudio_id):

        return self.service.get_preparacion_por_estudio(estudio_id)

    # ---------------------------------------------------------
    # GET LISTA PREPARACIONES
    # ---------------------------------------------------------

    def get_lista_preparaciones_por_preparacion(
        self,
        preparacion_id
    ):

        return self.service.get_lista_preparaciones_por_preparacion(
            preparacion_id
        )

    # ---------------------------------------------------------
    # GET CONTRATO DETALLE
    # ---------------------------------------------------------

    def get_contrato_detalle(self, entidad_contrato_estudio_id):

        return self.service.get_contrato_detalle(
            entidad_contrato_estudio_id
        )

    # ---------------------------------------------------------
    # GET RECOMENDACIONES POR ESTUDIO
    # ---------------------------------------------------------

    def get_recomendaciones_por_estudio(
        self,
        estudio_id
    ):

        return self.service.get_recomendaciones_por_estudio(
            estudio_id
        )

    # ---------------------------------------------------------
    # GET RECOMENDACIONES POR ENTIDAD
    # ---------------------------------------------------------

    def get_recomendaciones_por_entidad(
        self,
        entidad_id
    ):

        return self.service.get_recomendaciones_por_entidad(
            entidad_id
        )

    # ---------------------------------------------------------
    # FLUJO COMPLETO
    # ---------------------------------------------------------

    def get_flujo_completo(self, estudio_id, entidad_id):

        return self.service.get_flujo_completo(
            estudio_id,
            entidad_id
        )
