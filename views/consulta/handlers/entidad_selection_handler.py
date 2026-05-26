from ..components.chat_bubble_ai import (
    build as build_ai
)

from ..components.chat_bubble_user import (
    build as build_user
)


class EntidadSelectionHandler:

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

        entidad = self.state.entidad_results[index]

        self.state.entidad_selected = entidad
        self.state.entidad_id = entidad["id"]

        self.ui["chat"].controls.append(
            build_user(
                entidad["nombre"]
            )
        )

        self.ui["chat"].controls.append(
            build_ai(
                f"La entidad {entidad['nombre']} tiene contratos disponibles. Ahora selecciona el estudio."
            )
        )

        self.ui["entidad_input"].visible = False
        self.ui["results_container"].controls = []

        self.ui["estudio_input"].visible = True
        self.ui["estudio_input"].focus()

        self.state.current_step = "estudio"

        self.page.update()