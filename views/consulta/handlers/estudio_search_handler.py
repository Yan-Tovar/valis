from ..components.chat_results_list import (
    build as build_results
)


class EstudioSearchHandler:

    def __init__(
        self,
        page,
        controller,
        state,
        ui
    ):

        self.page = page
        self.controller = controller
        self.state = state
        self.ui = ui

    def handle(self, e):

        query = e.control.value.strip()

        if not query:
            return

        response = (
            self.controller.search_estudios_por_entidad(
                self.state.entidad_id,
                query
            )
        )

        if not response.success:

            self.ui["results_container"].controls = []

            self.page.update()

            return

        self.state.estudio_results = response.data

        self.state.estudio_selected_index = 0

        # =========================================
        # AUTOSELECT SINGLE RESULT
        # =========================================

        if len(response.data) == 1:

            estudio = response.data[0]

            self.ui["estudio_input"].value = (
                estudio["nombre"]
            )

            self.page.update()

            self.ui["on_estudio_select"](0)

            return

        self.ui["results_container"].controls = [

            build_results(
                self.state.estudio_results,
                self.state.estudio_selected_index,
                self.ui["on_estudio_select"]
            )
        ]

        self.page.update()