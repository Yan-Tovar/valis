import flet as ft

from .consulta_controller import ConsultaController
from .state.consulta_state import ConsultaState

from .components.consulta_left_panel import (
    ConsultaLeftPanel
)

from .components.consulta_right_panel import (
    ConsultaRightPanel
)

from .builders.left_panel_builder import (
    build as build_left_panel
)

from .builders.right_panel_builder import (
    build as build_right_panel
)

from .builders.consulta_layout_builder import (
    build as build_consulta_layout
)

from .handlers.estudio_search_handler import (
    EstudioSearchHandler
)

from .handlers.estudio_selection_handler import (
    EstudioSelectionHandler
)

from .handlers.entidad_search_handler import (
    EntidadSearchHandler
)

from .handlers.entidad_selection_handler import (
    EntidadSelectionHandler
)

from .handlers.search_navigation_handler import (
    SearchNavigationHandler
)


class ConsultaView:

    title = "Consulta"

    def __init__(self, page):

        self.page = page

        self.controller = ConsultaController()

        self.state = ConsultaState()

        # =================================================
        # PANELS
        # =================================================

        self.left_panel = ConsultaLeftPanel(

            on_search_estudio=self._on_search_estudio,

            on_estudio_selected=self._on_estudio_selected,

            on_search_entidad=self._on_search_entidad,

            on_entidad_selected=self._on_entidad_selected
        )

        self.right_panel = ConsultaRightPanel()

        # =================================================
        # FLUJO INICIAL
        # =================================================

        # PASO 1: Buscar entidad primero (visible)
        # PASO 2: Buscar estudio luego (oculto hasta seleccionar entidad)

        self.left_panel.search_entidad_input.visible = True
        self.left_panel.search_estudio_input.visible = False

        # =================================================
        # UI REFERENCES
        # =================================================

        self.ui = {

            "search_estudio_input":
            self.left_panel.search_estudio_input,

            "search_entidad_input":
            self.left_panel.search_entidad_input,

            "estudio_results_container":
            self.left_panel.estudio_results_container,

            "entidad_results_container":
            self.left_panel.entidad_results_container,

            "resultado_container":
            self.right_panel.resultado_container
        }

        # =================================================
        # HANDLERS
        # =================================================

        self.estudio_search_handler = (
            EstudioSearchHandler(

                self.page,

                self.controller,

                self.state,

                self.ui,

                self._on_estudio_selected
            )
        )

        self.estudio_selection_handler = (
            EstudioSelectionHandler(

                self.page,

                self.controller,

                self.state,

                self.ui
            )
        )

        self.entidad_search_handler = (
            EntidadSearchHandler(

                self.page,

                self.controller,

                self.state,

                self.ui,

                self._on_entidad_selected
            )
        )

        self.entidad_selection_handler = (
            EntidadSelectionHandler(

                self.page,

                self.controller,

                self.state,

                self.ui,

                self._on_estudio_selected
            )
        )

        self.search_navigation_handler = (
            SearchNavigationHandler(

                self.page,

                self.state,

                self.ui
            )
        )

        # =================================================
        # KEYBOARD EVENTS
        # =================================================

        self.page.on_keyboard_event = (
            self._on_keyboard_event
        )

    # =================================================
    # ENTIDAD
    # =================================================

    def _on_search_entidad(self, e):

        self.entidad_search_handler.handle(e)

    def _on_entidad_selected(self, index):

        self.entidad_selection_handler.handle(index)

    # =================================================
    # ESTUDIO
    # =================================================

    def _on_search_estudio(self, e):

        self.estudio_search_handler.handle(e)

    def _on_estudio_selected(self, index):

        self.estudio_selection_handler.handle(index)

    # =================================================
    # KEYBOARD NAVIGATION
    # =================================================

    def _on_keyboard_event(self, e):

        focused = (
            getattr(e, "control", None)
            or
            getattr(e, "target", None)
        )

        # -------------------------------------------------
        # ESC
        # -------------------------------------------------

        if e.key == "Escape":

            self.ui[
                "estudio_results_container"
            ].controls = []

            self.ui[
                "entidad_results_container"
            ].controls = []

            self.page.update()

            return

        # -------------------------------------------------
        # ENTIDAD NAVIGATION
        # -------------------------------------------------

        if focused is self.left_panel.search_entidad_input:

            self.search_navigation_handler.handle(

                e,

                self.state.entidad_results,

                "entidad_selected_index",

                self._render_entidad_results,

                self._on_entidad_selected
            )

        # -------------------------------------------------
        # ESTUDIO NAVIGATION
        # -------------------------------------------------

        elif focused is self.left_panel.search_estudio_input:

            self.search_navigation_handler.handle(

                e,

                self.state.estudio_results,

                "estudio_selected_index",

                self._render_estudio_results,

                self._on_estudio_selected
            )

    # =================================================
    # RENDER ENTIDADES
    # =================================================

    def _render_entidad_results(self):

        from .components.search_results_list import (
            build as build_search_results
        )

        self.ui[
            "entidad_results_container"
        ].controls = build_search_results(

            "Entidades disponibles",

            self.state.entidad_results,

            self.state.entidad_selected_index,

            self._on_entidad_selected
        )

    # =================================================
    # RENDER ESTUDIOS
    # =================================================

    def _render_estudio_results(self):

        from .components.search_results_list import (
            build as build_search_results
        )

        self.ui[
            "estudio_results_container"
        ].controls = build_search_results(

            "Estudios disponibles",

            self.state.estudio_results,

            self.state.estudio_selected_index,

            self._on_estudio_selected
        )

    # =================================================
    # BUILD
    # =================================================

    def build(self):

        return build_consulta_layout(

            build_left_panel(
                self.left_panel.panel
            ),

            build_right_panel(
                self.right_panel.panel
            )
        )