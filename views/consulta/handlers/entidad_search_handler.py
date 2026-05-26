from ..components.chat_results_list import (
    build as build_results
)


class EntidadSearchHandler:

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

        self.state.entidad_query = query

        if not query:

            self.ui["results_container"].controls = []

            self.page.update()

            return

        response = self.controller.search_entidad(
            query
        )

        if not response.success:

            self.ui["results_container"].controls = []

            self.page.update()

            return

        self.state.entidad_results = response.data

        self.ui["results_container"].controls = [

            build_results(
                self.state.entidad_results,
                self.state.entidad_selected_index,
                self.ui["on_entidad_select"]
            )
        ]

        self.page.update()