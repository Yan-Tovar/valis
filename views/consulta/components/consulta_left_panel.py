import flet as ft

from core.components.buttons.primary_button import PrimaryButton
from core.theme.colors import AppColors

from .search_input import build as build_search_input


class ConsultaLeftPanel:

    def __init__(
        self,
        on_search_estudio,
        on_estudio_selected,
        on_search_entidad,
        on_entidad_selected
    ):

        self.search_estudio_input = build_search_input(
            "Buscar Estudio",
            "Por código, nombre o ID",
            300,
            "",
            on_submit=on_search_estudio,
            on_change=on_search_estudio,
            autofocus=False,
            visible=False
        )

        self.search_entidad_input = build_search_input(
            "Buscar Entidad (EPS)",
            "Por código o nombre",
            300,
            "",
            on_submit=on_search_entidad,
            on_change=on_search_entidad,
            autofocus=True,
            visible=True
        )

        self.estudio_results_container = ft.Column(spacing=5)
        self.entidad_results_container = ft.Column(spacing=5)

        # -------------------------------------------------
        # CONTENEDORES CON SCROLL PARA RESULTADOS LARGOS
        # -------------------------------------------------

        self.entidad_results_scroll = ft.Container(
            content=ft.Column(
                controls=[self.entidad_results_container],
                spacing=5,
                scroll=ft.ScrollMode.AUTO
            ),
            height=250,
            expand=False,
            border_radius=10,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            border=ft.border.all(1, AppColors.BORDER)
        )

        self.estudio_results_scroll = ft.Container(
            content=ft.Column(
                controls=[self.estudio_results_container],
                spacing=5,
                scroll=ft.ScrollMode.AUTO
            ),
            height=250,
            expand=False,
            border_radius=10,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            border=ft.border.all(1, AppColors.BORDER)
        )

        self.btn_buscar_estudio = PrimaryButton(
            text="Buscar",
            icon=ft.icons.SEARCH,
            on_click=on_search_estudio,
            width=100
        )
        self.btn_buscar_estudio.visible = False

        self.btn_buscar_entidad = PrimaryButton(
            text="Buscar",
            icon=ft.icons.SEARCH,
            on_click=on_search_entidad,
            width=100
        )
        self.btn_buscar_entidad.visible = False  # Los búsquedas se disparan con on_change

        self.panel = ft.Column(
            spacing=15,
            width=420,
            controls=[
                ft.Text(
                    "Búsqueda de Consulta",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=AppColors.PRIMARY
                ),
                ft.Divider(),
                # PASO 1: BUSCAR ENTIDAD (PRIMERO)
                ft.Column(
                    spacing=10,
                    controls=[
                        self.search_entidad_input,
                        self.btn_buscar_entidad,
                        self.entidad_results_scroll
                    ]
                ),
                ft.Divider(),
                # PASO 2: BUSCAR ESTUDIO (DESPUÉS)
                ft.Column(
                    spacing=10,
                    controls=[
                        self.search_estudio_input,
                        self.btn_buscar_estudio,
                        self.estudio_results_scroll
                    ]
                ),
                ft.Container(expand=True)
            ]
        )
