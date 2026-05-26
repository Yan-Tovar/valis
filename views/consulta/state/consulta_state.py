class ConsultaState:

    def __init__(self):

        # =====================================================
        # ENTIDAD
        # =====================================================

        self.entidad_id = None
        self.entidad_selected = None
        self.entidad_query = ""

        self.entidad_results = []
        self.entidad_selected_index = 0

        # =====================================================
        # ESTUDIO
        # =====================================================

        self.estudio_id = None
        self.estudio_selected = None
        self.estudio_query = ""

        self.estudio_results = []
        self.estudio_selected_index = 0

        # =====================================================
        # RESULTADO
        # =====================================================

        self.resultado_completo = None

        # =====================================================
        # CHAT FLOW
        # =====================================================

        self.current_step = "entidad"

        """
        Steps:

        entidad
        estudio
        resultado
        """

    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        self.__init__()