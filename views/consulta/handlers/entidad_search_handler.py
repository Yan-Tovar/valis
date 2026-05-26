from core.components.alerts.snackbar import Snackbar


class EntidadSearchHandler:

    def __init__(self, page, controller, state, ui, on_select):

        self.page = page
        self.controller = controller
        self.state = state
        self.ui = ui
        self.on_select = on_select

    def handle(self, _e):

        query = self.ui["search_entidad_input"].value.strip()

        self.state.entidad_query = query
        self.state.entidad_selected = None
        self.state.entidad_selected_index = 0
        self.state.entidad_results_visible = True

        # -------------------------------------------------
        # BUSCAR ENTIDADES
        # -------------------------------------------------
        # Buscar incluso si query está vacío para mostrar
        # todas las entidades disponibles

        response = self.controller.search_entidad(
            query
        )

        if not response.success:

            Snackbar.error(
                self.page,
                response.message
            )

            self.state.entidad_results = []

            self._render_results()

            return

        self.state.entidades_disponibles = response.data
        self.state.entidad_results = response.data
        self.state.entidad_selected_index = 0

        self._render_results()

    def _render_results(self):

        from ..components.search_results_list import (
            build as build_search_results
        )

        self.ui["entidad_results_container"].controls = (
            build_search_results(
                "Entidades disponibles",
                self.state.entidad_results,
                self.state.entidad_selected_index,
                self.on_select
            )
        )

        self.page.update()