from ..components.chat_bubble_ai import (
    build as build_ai
)

from ..components.chat_action_button import (
    build as build_action_button
)

from ..renderers.resultado_renderer import (
    build as build_resultado
)


class ResultadoHandler:

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

    def handle(self):

        response = self.controller.get_flujo_completo(

            self.state.estudio_id,
            self.state.entidad_id
        )

        if not response.success:

            self.ui["chat"].controls.append(

                build_ai(
                    response.message
                )
            )

            self.page.update()

            return

        self.state.resultado_completo = response.data

        resultado_controls = build_resultado(

            response.data,

            self.ui["on_open_detail"]
        )

        self.ui["chat"].controls.append(

            build_ai(
                "Consulta completada correctamente.",
                [resultado_controls]
            )
        )

        self.ui["chat"].controls.append(

            build_action_button(
                "Finalizar proceso",
                self.ui["on_finish"]
            )
        )

        self.state.current_step = "resultado"

        self.page.update()