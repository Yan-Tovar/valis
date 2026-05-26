class ConsultaState:

    def __init__(self):
        self.estudio_id = None
        self.entidad_id = None
        self.estudio_query = ""
        self.entidad_query = ""
        self.estudios_disponibles = []
        self.entidades_disponibles = []
        self.estudio_results = []
        self.entidad_results = []
        self.estudio_selected_index = 0
        self.entidad_selected_index = 0
        self.estudio_selected = None
        self.entidad_selected = None
        self.estudio_results_visible = False
        self.entidad_results_visible = False
        self.loading_estudios = False
        self.loading_entidades = False
        self.resultado_completo = None

    def reset_entidad_selection(self):
        self.entidad_id = None
        self.entidad_query = ""
        self.entidad_results = []
        self.entidad_selected_index = 0
        self.entidad_selected = None
        self.entidad_results_visible = False

    def reset_resultado(self):
        self.resultado_completo = None
