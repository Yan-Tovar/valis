import flet as ft

from auth.session_manager import SessionManager
from ..renderers.estudio_renderer import build_estudio_info, build_salas_section
from ..renderers.resultado_renderer import build_error, build_resultado_completo
from ..components.parrot_result_bubble import build_estudio_bubble, build_resultado_bubble
from ..components.detail_modal import show_detail_modal


class ResultadoHandler:

    def __init__(self, page, controller, state, ui):
        self.page = page
        self.controller = controller
        self.state = state
        self.ui = ui

    def show_estudio_info(self):
        self.ui["resultado_container"].controls = []

        response = self.controller.get_salas_por_estudio(self.state.estudio_id)

        user = SessionManager.current_user()

        username = (
            user.get("nombre_completo", "Usuario")
            if user
            else "Usuario"
        )

        def _open_detail(payload):
            # payload can be estudio, sala, etc. Build simple controls
            controls = []
            if not payload:
                controls.append(ft.Text("No hay datos"))
            elif isinstance(payload, dict):
                for k, v in payload.items():
                    controls.append(ft.Row(controls=[ft.Text(f"{k}: ", weight=ft.FontWeight.BOLD, size=12), ft.Text(str(v), size=12)]))
            else:
                controls.append(ft.Text(str(payload)))

            show_detail_modal(self.page, "Detalle", controls)

        if response.success:
            # Show parrot bubble with estudio info
            bubble = build_estudio_bubble(
                self.state.estudio_selected,
                response.data,
                username,
                on_open_detail=_open_detail
            )
            # keep bubble at top
            self.ui["resultado_container"].controls.append(bubble)
        else:
            # Show error message with parrot bubble
            bubble = build_estudio_bubble(
                self.state.estudio_selected,
                [],
                username,
                on_open_detail=_open_detail
            )
            self.ui["resultado_container"].controls.append(bubble)

        self.page.update()

    def show_resultado_completo(self, data):


        user = SessionManager.current_user()

        username = (
            user.get("nombre_completo", "Usuario")
            if user
            else "Usuario"
        )

        def _open_detail(payload):

            controls = []

            if not payload:

                controls.append(
                    ft.Text("No hay datos")
                )

            elif isinstance(payload, dict):

                for k, v in payload.items():

                    controls.append(
                        ft.Row(
                            controls=[
                                ft.Text(
                                    f"{k}: ",
                                    weight=ft.FontWeight.BOLD,
                                    size=12
                                ),
                                ft.Text(
                                    str(v),
                                    size=12
                                )
                            ]
                        )
                    )

            else:

                controls.append(
                    ft.Text(str(payload))
                )

            show_detail_modal(
                self.page,
                "Detalle",
                controls
            )

        # ---------------------------------------------------------
        # LIMPIAR RESULTADOS ANTERIORES
        # ---------------------------------------------------------

        self.ui["resultado_container"].controls = []

        # ---------------------------------------------------------
        # MOSTRAR SOLO EL BUBBLE
        # ---------------------------------------------------------

        bubble = build_resultado_bubble(
            data,
            username,
            on_open_detail=_open_detail
        )

        self.ui["resultado_container"].controls.append(
            bubble
        )

        self.page.update()