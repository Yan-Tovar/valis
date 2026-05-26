import flet as ft

from core.theme.colors import AppColors
from .consulta_result_section import build as build_result_section


class ConsultaRightPanel:

    def __init__(self):

        self.resultado_container = ft.Column(
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

        self.panel = build_result_section(self.resultado_container)
