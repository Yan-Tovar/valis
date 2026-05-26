from core.components.alerts.snackbar import Snackbar
from .resultado_handler import ResultadoHandler
from ..renderers.resultado_renderer import build_error


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

        self.resultado_handler = ResultadoHandler(
            page,
            controller,
            state,
            ui
        )

    def handle(self, index):

        if (
            index is None
            or
            index >= len(self.state.estudio_results)
        ):
            return

        estudio = self.state.estudio_results[index]

        self.state.estudio_selected = estudio

        self.state.estudio_id = int(
            estudio.get("estudio_id", 0)
        )

        self.state.estudio_query = (
            f"{estudio.get('codigo_cups', '')} - "
            f"{estudio.get('nombre', '')}"
        )

        self.state.estudio_results_visible = False

        self.ui["search_estudio_input"].value = (
            self.state.estudio_query
        )

        self.ui["estudio_results_container"].controls = []

        self.page.update()

        # Mostrar mensaje de carga
        Snackbar.success(
            self.page,
            f"Cargando detalles de {estudio.get('nombre', 'Estudio')}..."
        )

        response = self.controller.get_flujo_completo(
            self.state.entidad_id,
            self.state.estudio_id
        )

        if not response.success:

            Snackbar.error(
                self.page,
                response.message
            )

            self.ui["resultado_container"].controls = (
                build_error(
                    response.message
                )
            )

            self.page.update()

            return

        self.state.resultado_completo = response.data

        Snackbar.success(
            self.page,
            "Información cargada correctamente"
        )

        self.resultado_handler.show_resultado_completo(
            response.data
        )