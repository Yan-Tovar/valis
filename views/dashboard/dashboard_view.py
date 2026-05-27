import flet as ft

from core.services.dashboard_statistics_service import (
    DashboardStatisticsService
)


class DashboardView:

    # =================================================
    # TITLE
    # =================================================

    title = "Dashboard"

    # =================================================
    # INIT
    # =================================================

    def __init__(
        self,
        page: ft.Page
    ):

        self.page = page

        self.service = (
            DashboardStatisticsService()
        )

    # =================================================
    # HELPERS
    # =================================================

    def build_section(
        self,
        title,
        data
    ):

        return ft.Container(

            padding=20,

            border_radius=12,

            bgcolor="white",

            border=ft.border.all(
                1,
                "#E5E7EB"
            ),

            content=ft.Column(

                spacing=10,

                controls=[

                    ft.Text(

                        title,

                        size=20,

                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Divider(),

                    ft.Text(
                        str(data),
                        selectable=True
                    )
                ]
            )
        )

    # =================================================
    # BUILD
    # =================================================

    def build(self):

        # =============================================
        # LOAD DATA
        # =============================================

        general_kpis = (
            self.service.get_general_kpis()
        )

        top_estudios = (
            self.service.get_top_estudios_mas_contratados()
        )

        top_entidades = (
            self.service.get_top_entidades_contratantes()
        )

        estudios_por_entidad = (
            self.service.get_estudios_por_entidad()
        )

        estudios_con_salas = (
            self.service.get_estudios_con_mas_salas()
        )

        salas_mas_utilizadas = (
            self.service.get_salas_mas_utilizadas()
        )

        estudios_sin_sala = (
            self.service.get_estudios_sin_sala()
        )

        estudios_preparacion = (
            self.service.get_estudios_con_y_sin_preparacion()
        )

        preparaciones_complejas = (
            self.service.get_preparaciones_mas_complejas()
        )

        contratos_estado = (
            self.service.get_contratos_estado()
        )

        estudios_recomendaciones = (
            self.service.get_estudios_con_mas_recomendaciones()
        )

        usuarios_roles = (
            self.service.get_usuarios_por_rol()
        )

        # =============================================
        # UI
        # =============================================

        return ft.Container(

            expand=True,

            padding=20,

            bgcolor="#F5F7FA",

            content=ft.Column(

                expand=True,

                scroll=ft.ScrollMode.AUTO,

                spacing=20,

                controls=[

                    # =================================
                    # TITLE
                    # =================================

                    ft.Text(

                        "Dashboard Estadístico",

                        size=32,

                        weight=ft.FontWeight.BOLD
                    ),

                    # =================================
                    # GENERAL KPIS
                    # =================================

                    self.build_section(

                        "KPIs Generales",

                        general_kpis.data
                        if general_kpis.success
                        else general_kpis.message
                    ),

                    # =================================
                    # TOP ESTUDIOS
                    # =================================

                    self.build_section(

                        "Top Estudios Más Contratados",

                        top_estudios.data
                        if top_estudios.success
                        else top_estudios.message
                    ),

                    # =================================
                    # TOP ENTIDADES
                    # =================================

                    self.build_section(

                        "Top Entidades Contratantes",

                        top_entidades.data
                        if top_entidades.success
                        else top_entidades.message
                    ),

                    # =================================
                    # ESTUDIOS POR ENTIDAD
                    # =================================

                    self.build_section(

                        "Cantidad de Estudios por Entidad",

                        estudios_por_entidad.data
                        if estudios_por_entidad.success
                        else estudios_por_entidad.message
                    ),

                    # =================================
                    # ESTUDIOS CON MAS SALAS
                    # =================================

                    self.build_section(

                        "Estudios con Más Salas",

                        estudios_con_salas.data
                        if estudios_con_salas.success
                        else estudios_con_salas.message
                    ),

                    # =================================
                    # SALAS MAS UTILIZADAS
                    # =================================

                    self.build_section(

                        "Salas Más Utilizadas",

                        salas_mas_utilizadas.data
                        if salas_mas_utilizadas.success
                        else salas_mas_utilizadas.message
                    ),

                    # =================================
                    # ESTUDIOS SIN SALAS
                    # =================================

                    self.build_section(

                        "Estudios Sin Sala",

                        estudios_sin_sala.data
                        if estudios_sin_sala.success
                        else estudios_sin_sala.message
                    ),

                    # =================================
                    # PREPARACIONES
                    # =================================

                    self.build_section(

                        "Estudios con y sin Preparación",

                        estudios_preparacion.data
                        if estudios_preparacion.success
                        else estudios_preparacion.message
                    ),

                    # =================================
                    # PREPARACIONES COMPLEJAS
                    # =================================

                    self.build_section(

                        "Preparaciones Más Complejas",

                        preparaciones_complejas.data
                        if preparaciones_complejas.success
                        else preparaciones_complejas.message
                    ),

                    # =================================
                    # CONTRATOS
                    # =================================

                    self.build_section(

                        "Contratos Activos vs Vencidos",

                        contratos_estado.data
                        if contratos_estado.success
                        else contratos_estado.message
                    ),

                    # =================================
                    # RECOMENDACIONES
                    # =================================

                    self.build_section(

                        "Estudios con Más Recomendaciones",

                        estudios_recomendaciones.data
                        if estudios_recomendaciones.success
                        else estudios_recomendaciones.message
                    ),

                    # =================================
                    # USUARIOS
                    # =================================

                    self.build_section(

                        "Usuarios por Rol",

                        usuarios_roles.data
                        if usuarios_roles.success
                        else usuarios_roles.message
                    )
                ]
            )
        )
    