from ..handlers.resultado_handler import (
    ResultadoHandler
)

from ..components.chat_bubble_user import (
    build as build_user
)


class EstudioSelectionHandler:

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

    def handle(self, index):

        estudio = self.state.estudio_results[index]

        self.state.estudio_selected = estudio
        self.state.estudio_id = estudio["estudio_id"]

        self.ui["chat"].controls.append(

            build_user(
                estudio["nombre"]
            )
        )

        self.ui["results_container"].controls = []

        self.ui["estudio_input"].visible = False

        ResultadoHandler(

            self.page,
            self.controller,
            self.state,
            self.ui

        ).handle()