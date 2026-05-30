import flet as ft

from .consulta_controller import ConsultaController

from .state.consulta_state import (
    ConsultaState
)

from auth.session_manager import (
    SessionManager
)

from .components.chat_bubble_ai import (
    build as build_ai
)

from .components.chat_input import (
    build as build_chat_input
)

from .components.detail_modal import (
    show_detail_modal
)

from .handlers.entidad_search_handler import (
    EntidadSearchHandler
)

from .handlers.entidad_selection_handler import (
    EntidadSelectionHandler
)

from .handlers.estudio_search_handler import (
    EstudioSearchHandler
)

from .handlers.estudio_selection_handler import (
    EstudioSelectionHandler
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

        # =====================================================
        # CHAT
        # =====================================================

        self.chat = ft.ListView(

            expand=True,

            spacing=15,

            auto_scroll=True
        )

        # =====================================================
        # INPUTS
        # =====================================================

        self.entidad_input = build_chat_input(

            "Buscar entidad...",

            self._on_search_entidad,

            visible=True,

            autofocus=True
        )

        self.estudio_input = build_chat_input(

            "Buscar estudio...",

            self._on_search_estudio,

            visible=False
        )

        # =====================================================
        # RESULTS
        # =====================================================

        self.results_container = ft.Column()

        # =====================================================
        # UI
        # =====================================================

        self.ui = {

            "chat": self.chat,

            "entidad_input": self.entidad_input,

            "estudio_input": self.estudio_input,

            "results_container": self.results_container,

            "on_entidad_select": self._on_entidad_selected,

            "on_estudio_select": self._on_estudio_selected,

            "on_finish": self._restart_flow,

            "on_open_detail": self._open_detail,

            "add_message": self._add_chat_message
        }

        # =====================================================
        # HANDLERS
        # =====================================================

        self.entidad_search_handler = (
            EntidadSearchHandler(
                page,
                self.controller,
                self.state,
                self.ui
            )
        )

        self.entidad_selection_handler = (
            EntidadSelectionHandler(
                page,
                self.controller,
                self.state,
                self.ui
            )
        )

        self.estudio_search_handler = (
            EstudioSearchHandler(
                page,
                self.controller,
                self.state,
                self.ui
            )
        )

        self.estudio_selection_handler = (
            EstudioSelectionHandler(
                page,
                self.controller,
                self.state,
                self.ui
            )
        )

        self.search_navigation_handler = (
            SearchNavigationHandler(
                page,
                self.state,
                self.ui
            )
        )

        # =====================================================
        # INIT
        # =====================================================

        self._start_chat()

    # =====================================================
    # START
    # =====================================================

    def _start_chat(self):

        # =================================================
        # CLEAR CHAT
        # =================================================

        self.chat.controls.clear()

        # =================================================
        # CURRENT USER
        # =================================================

        user = SessionManager.current_user()

        nombre = "Usuario"

        if user:

            nombre = user.get(
                "nombre_completo",
                "Usuario"
            )

        # =================================================
        # WELCOME MESSAGE
        # =================================================

        self.chat.controls.append(

            build_ai(
                f"Hola, {nombre}. ¿Qué entidad quieres consultar hoy?"
            )
        )

    # =====================================================
    # ADD MESSAGE
    # =====================================================

    def _add_chat_message(
        self,
        control
    ):

        self.chat.controls.append(control)

        self.page.update()

        self.chat.scroll_to(
            offset=-1,
            duration=300
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def _on_search_entidad(self, e):

        self.entidad_search_handler.handle(e)

    def _on_search_estudio(self, e):

        self.estudio_search_handler.handle(e)

    # =====================================================
    # SELECT
    # =====================================================

    def _on_entidad_selected(self, index):

        self.entidad_selection_handler.handle(index)

    def _on_estudio_selected(self, index):

        self.estudio_selection_handler.handle(index)

    # =====================================================
    # DETAIL
    # =====================================================

    def _open_detail(self, payload):

        show_detail_modal(
            self.page,
            "Detalle completo",
            payload
        )
    # =====================================================
    # RESTART
    # =====================================================

    def _restart_flow(self, e):

        # =================================================
        # RESET STATE
        # =================================================

        self.state.reset()

        # =================================================
        # RESET INPUTS
        # =================================================

        self.entidad_input.visible = True
        self.estudio_input.visible = False

        self.entidad_input.value = ""
        self.estudio_input.value = ""

        # =================================================
        # RESET RESULTS
        # =================================================

        self.results_container.controls.clear()

        # =================================================
        # RESET CHAT
        # =================================================

        self.chat.controls.clear()

        # =================================================
        # START AGAIN
        # =================================================

        self._start_chat()

        self.page.update()

        # =================================================
        # FOCUS
        # =================================================

        self.entidad_input.focus()

    # =====================================================
    # BUILD
    # =====================================================

    def build(self):

        return ft.Container(

            expand=True,

            padding=20,

            content=ft.Column(

                expand=True,

                spacing=15,

                controls=[

                    # CHAT
                    self.chat,

                    # RESULTS
                    self.results_container,

                    # INPUTS
                    self.entidad_input,

                    self.estudio_input
                ]
            )
        )