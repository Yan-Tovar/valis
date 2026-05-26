from core.crud_engine.consulta_controller import (
    ConsultaController as CoreConsultaController
)


class ConsultaController(
    CoreConsultaController
):

    # ---------------------------------------------------------
    # SEARCH ENTIDAD
    # ---------------------------------------------------------

    def search_entidad(
        self,
        query_text
    ):

        return self.service.search_entidad(
            query_text
        )

    # ---------------------------------------------------------
    # GET ESTUDIOS POR ENTIDAD
    # ---------------------------------------------------------

    def get_estudios_por_entidad(
        self,
        entidad_id
    ):

        return self.service.get_estudios_por_entidad(
            entidad_id
        )

    # ---------------------------------------------------------
    # SEARCH ESTUDIO POR ENTIDAD
    # ---------------------------------------------------------

    def search_estudios_por_entidad(
        self,
        entidad_id,
        query_text
    ):

        return self.service.get_estudios_por_entidad(
            entidad_id,
            query_text
        )

    # ---------------------------------------------------------
    # GET FLUJO COMPLETO
    # ---------------------------------------------------------

    def get_flujo_completo(
        self,
        estudio_id,
        entidad_id
    ):

        return self.service.get_flujo_completo(
            estudio_id,
            entidad_id
        )

    # ---------------------------------------------------------
    # GET SALAS POR ESTUDIO
    # ---------------------------------------------------------

    def get_salas_por_estudio(
        self,
        estudio_id
    ):

        return self.service.get_salas_por_estudio(
            estudio_id
        )