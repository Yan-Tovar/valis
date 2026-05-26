from core.components.alerts.snackbar import Snackbar


class EstudioSearchHandler:

    def __init__(
        self,
        page,
        controller,
        state,
        ui,
        on_select
    ):

        self.page = page
        self.controller = controller
        self.state = state
        self.ui = ui
        self.on_select = on_select

    def handle(self, _e):

        if not self.state.entidad_selected:

            Snackbar.error(
                self.page,
                "Selecciona una entidad primero"
            )

            return

        query = self.ui["search_estudio_input"].value.strip()

        self.state.estudio_query = query
        self.state.estudio_selected = None
        self.state.estudio_selected_index = 0
        self.state.estudio_results_visible = True

        # -------------------------------------------------
        # BUSCAR ESTUDIOS FILTRADOS POR ENTIDAD
        # -------------------------------------------------
        # Incluso sin query, llamamos al método para obtener
        # todos los estudios disponibles para esta entidad

        response = (
            self.controller.search_estudios_por_entidad(
                self.state.entidad_id,
                query
            )
        )

        if not response.success:

            Snackbar.error(
                self.page,
                response.message
            )

            self.state.estudio_results = []

            self._render_results()

            return

        self.state.estudios_disponibles = response.data
        self.state.estudio_results = response.data
        self.state.estudio_selected_index = 0

        self._render_results()

    def _render_results(self):

        from ..components.search_results_list import (
            build as build_search_results
        )

        self.ui["estudio_results_container"].controls = (
            build_search_results(
                "Estudios disponibles",
                self.state.estudio_results,
                self.state.estudio_selected_index,
                self.on_select
            )
        )

        self.page.update()