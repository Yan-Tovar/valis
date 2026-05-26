from core.components.alerts.snackbar import Snackbar

from ..components.search_results_list import (
    build as build_search_results
)


class EntidadSelectionHandler:

    def __init__(
        self,
        page,
        controller,
        state,
        ui,
        on_select_estudio
    ):

        self.page = page
        self.controller = controller
        self.state = state
        self.ui = ui
        self.on_select_estudio = on_select_estudio

    def handle(self, index):

        if (
            index is None
            or
            index >= len(self.state.entidad_results)
        ):
            return

        entidad = self.state.entidad_results[index]

        self.state.entidad_selected = entidad

        self.state.entidad_id = int(
            entidad.get("id", 0)
        )

        self.state.entidad_query = (
            f"{entidad.get('codigo_entidad', '')} - "
            f"{entidad.get('nombre', '')}"
        )

        self.state.entidad_results_visible = False

        self.ui["search_entidad_input"].value = (
            self.state.entidad_query
        )

        self.ui["entidad_results_container"].controls = []

        # ---------------------------------------------------------
        # HABILITAR BUSQUEDA DE ESTUDIO
        # ---------------------------------------------------------

        self.ui["search_estudio_input"].visible = True

        self.ui["search_estudio_input"].value = ""

        # Limpiar resultados de estudios previos
        self.ui["estudio_results_container"].controls = []

        # Resetear estado de estudios
        self.state.estudio_results = []
        self.state.estudio_selected = None
        self.state.estudio_selected_index = 0
        self.state.estudio_id = None

        self.page.update()

        # Dar foco al input de estudio para que el usuario empiece a escribir
        self.ui["search_estudio_input"].focus()