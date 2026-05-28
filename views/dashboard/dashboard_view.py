import flet as ft

from core.services.dashboard_statistics_service import (
    DashboardStatisticsService
)


class DashboardView:

    # =====================================================
    # TITLE
    # =====================================================

    title = "Dashboard"

    # =====================================================
    # INIT
    # =====================================================

    def __init__(
        self,
        page: ft.Page
    ):

        self.page = page

        self.service = (
            DashboardStatisticsService()
        )

    # =====================================================
    # KPI CARD
    # =====================================================

    def build_kpi_card(
        self,
        title,
        value,
        icon,
        color
    ):

        return ft.Container(

            col={
                "xs": 12,
                "sm": 6,
                "md": 4,
                "lg": 2.4
            },

            padding=20,

            border_radius=18,

            bgcolor="white",

            border=ft.border.all(
                1,
                "#E5E7EB"
            ),

            content=ft.Row(

                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                vertical_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[

                    ft.Column(

                        spacing=4,

                        controls=[

                            ft.Text(

                                title,

                                size=13,

                                color="#6B7280",

                                weight=ft.FontWeight.W_500
                            ),

                            ft.Text(

                                str(value),

                                size=28,

                                weight=ft.FontWeight.BOLD,

                                color="#111827"
                            )
                        ]
                    ),

                    ft.Container(

                        width=52,
                        height=52,

                        border_radius=14,

                        bgcolor=color,

                        alignment=ft.alignment.center,

                        content=ft.Icon(
                            icon,
                            color="white",
                            size=26
                        )
                    )
                ]
            )
        )

    # =====================================================
    # SECTION CARD
    # =====================================================

    def build_chart_card(
        self,
        title,
        content,
        col=None,
        height=420
    ):

        return ft.Container(

            col=col or {
                "xs": 12,
                "lg": 6
            },

            height=height,

            bgcolor="white",

            border_radius=20,

            padding=20,

            border=ft.border.all(
                1,
                "#E5E7EB"
            ),

            content=ft.Column(

                expand=True,

                spacing=15,

                controls=[

                    ft.Text(

                        title,

                        size=18,

                        weight=ft.FontWeight.BOLD,

                        color="#111827"
                    ),

                    ft.Divider(height=1),

                    ft.Container(
                        expand=True,
                        content=content
                    )
                ]
            )
        )

    # =====================================================
    # HORIZONTAL BAR CHART
    # =====================================================

    def build_horizontal_chart(
        self,
        data,
        label_key,
        value_key,
        color="#2563EB"
    ):

        if not data:

            return ft.Text("Sin datos")

        max_value = max(
            item[value_key]
            for item in data
        )

        rows = []

        for item in data:

            value = item[value_key]

            width_factor = (
                value / max_value
            )

            rows.append(

                ft.Column(

                    spacing=4,

                    controls=[

                        ft.Row(

                            alignment=(
                                ft.MainAxisAlignment
                                .SPACE_BETWEEN
                            ),

                            controls=[

                                ft.Text(

                                    item[label_key][:45],

                                    size=12,

                                    weight=(
                                        ft.FontWeight.W_500
                                    )
                                ),

                                ft.Text(
                                    str(value),
                                    size=12
                                )
                            ]
                        ),

                        ft.Container(

                            height=12,

                            border_radius=20,

                            bgcolor="#E5E7EB",

                            content=ft.Row(

                                spacing=0,

                                controls=[

                                    ft.Container(

                                        width=(
                                            500 * width_factor
                                        ),

                                        bgcolor=color,

                                        border_radius=20
                                    )
                                ]
                            )
                        )
                    ]
                )
            )

        return ft.Column(

            scroll=ft.ScrollMode.AUTO,

            spacing=18,

            controls=rows
        )

    # =====================================================
    # PIE CHART
    # =====================================================

    def build_pie_chart(
        self,
        sections
    ):

        return ft.PieChart(

            sections=sections,

            center_space_radius=45,

            sections_space=2,

            expand=True
        )

    # =====================================================
    # ALERT LIST
    # =====================================================

    def build_alert_list(
        self,
        data,
        key
    ):

        return ft.Column(

            scroll=ft.ScrollMode.AUTO,

            spacing=10,

            controls=[

                ft.Container(

                    padding=12,

                    border_radius=12,

                    bgcolor="#FEF3C7",

                    content=ft.Row(

                        controls=[

                            ft.Icon(
                                ft.icons.WARNING,
                                color="#D97706"
                            ),

                            ft.Text(

                                item[key],

                                expand=True,

                                size=13,

                                color="#92400E"
                            )
                        ]
                    )
                )

                for item in data
            ]
        )

    # =====================================================
    # BUILD
    # =====================================================

    def build(self):

        # =================================================
        # DATA
        # =================================================

        kpis = (
            self.service
            .get_general_kpis()
            .data
        )

        top_estudios = (
            self.service
            .get_top_estudios_mas_contratados()
            .data
        )

        top_entidades = (
            self.service
            .get_top_entidades_contratantes()
            .data
        )

        estudios_entidad = (
            self.service
            .get_estudios_por_entidad()
            .data
        )

        estudios_salas = (
            self.service
            .get_estudios_con_mas_salas()
            .data
        )

        salas_utilizadas = (
            self.service
            .get_salas_mas_utilizadas()
            .data
        )

        estudios_sin_sala = (
            self.service
            .get_estudios_sin_sala()
            .data
        )

        preparaciones = (
            self.service
            .get_estudios_con_y_sin_preparacion()
            .data
        )

        preparaciones_complejas = (
            self.service
            .get_preparaciones_mas_complejas()
            .data
        )

        contratos_estado = (
            self.service
            .get_contratos_estado()
            .data
        )

        recomendaciones = (
            self.service
            .get_estudios_con_mas_recomendaciones()
            .data
        )

        usuarios_roles = (
            self.service
            .get_usuarios_por_rol()
            .data
        )

        # =================================================
        # UI
        # =================================================

        return ft.Container(

            expand=True,

            bgcolor="#F3F4F6",

            padding=25,

            content=ft.Column(

                expand=True,

                scroll=ft.ScrollMode.AUTO,

                spacing=25,

                controls=[

                    # =====================================
                    # HEADER
                    # =====================================

                    ft.Column(

                        spacing=4,

                        controls=[

                            ft.Text(

                                "Dashboard Estadístico",

                                size=32,

                                weight=ft.FontWeight.BOLD,

                                color="#111827"
                            ),

                            ft.Text(

                                "Resumen general del sistema",

                                size=14,

                                color="#6B7280"
                            )
                        ]
                    ),

                    # =====================================
                    # KPI ROW
                    # =====================================

                    ft.ResponsiveRow(

                        spacing=20,
                        run_spacing=20,

                        controls=[

                            self.build_kpi_card(
                                "Entidades",
                                kpis["total_entidades"],
                                ft.icons.BUSINESS,
                                "#2563EB"
                            ),

                            self.build_kpi_card(
                                "Estudios",
                                kpis["total_estudios"],
                                ft.icons.MEDICAL_SERVICES,
                                "#059669"
                            ),

                            self.build_kpi_card(
                                "Contratos",
                                kpis["total_contratos"],
                                ft.icons.DESCRIPTION,
                                "#D97706"
                            ),

                            self.build_kpi_card(
                                "Salas",
                                kpis["total_salas"],
                                ft.icons.MEETING_ROOM,
                                "#7C3AED"
                            ),

                            self.build_kpi_card(
                                "Preparaciones",
                                kpis["total_preparaciones"],
                                ft.icons.FACT_CHECK,
                                "#DC2626"
                            ),

                            self.build_kpi_card(
                                "Usuarios",
                                kpis["total_usuarios"],
                                ft.icons.GROUP,
                                "#0F766E"
                            )
                        ]
                    ),

                    # =====================================
                    # ROW 1
                    # =====================================

                    ft.ResponsiveRow(

                        spacing=20,
                        run_spacing=20,

                        controls=[

                            self.build_chart_card(

                                "Top Estudios Más Contratados",

                                self.build_horizontal_chart(

                                    top_estudios,

                                    "estudio",

                                    "cantidad",

                                    "#2563EB"
                                )
                            ),

                            self.build_chart_card(

                                "Top Entidades Contratantes",

                                self.build_horizontal_chart(

                                    top_entidades,

                                    "entidad",

                                    "cantidad",

                                    "#059669"
                                )
                            )
                        ]
                    ),

                    # =====================================
                    # ROW 2
                    # =====================================

                    ft.ResponsiveRow(

                        spacing=20,
                        run_spacing=20,

                        controls=[

                            self.build_chart_card(

                                "Estudios por Entidad",

                                self.build_horizontal_chart(

                                    estudios_entidad,

                                    "entidad",

                                    "cantidad_estudios",

                                    "#7C3AED"
                                )
                            ),

                            self.build_chart_card(

                                "Estudios con Más Salas",

                                self.build_horizontal_chart(

                                    estudios_salas,

                                    "estudio",

                                    "cantidad_salas",

                                    "#D97706"
                                )
                            )
                        ]
                    ),

                    # =====================================
                    # ROW 3
                    # =====================================

                    ft.ResponsiveRow(

                        spacing=20,
                        run_spacing=20,

                        controls=[

                            self.build_chart_card(

                                "Salas Más Utilizadas",

                                self.build_horizontal_chart(

                                    salas_utilizadas,

                                    "sala",

                                    "cantidad_estudios",

                                    "#DC2626"
                                )
                            ),

                            self.build_chart_card(

                                "Preparaciones Más Complejas",

                                self.build_horizontal_chart(

                                    preparaciones_complejas,

                                    "preparacion",

                                    "cantidad_items",

                                    "#0F766E"
                                )
                            )
                        ]
                    ),

                    # =====================================
                    # ROW 4
                    # =====================================

                    ft.ResponsiveRow(

                        spacing=20,
                        run_spacing=20,

                        controls=[

                            self.build_chart_card(

                                "Contratos Activos vs Vencidos",

                                self.build_pie_chart(

                                    sections=[

                                        ft.PieChartSection(

                                            contratos_estado["activos"],

                                            title=f'''
                                            Activos
                                            {contratos_estado["activos"]}
                                            ''',

                                            radius=90,

                                            color="#059669"
                                        ),

                                        ft.PieChartSection(

                                            contratos_estado["vencidos"],

                                            title=f'''
                                            Vencidos
                                            {contratos_estado["vencidos"]}
                                            ''',

                                            radius=90,

                                            color="#DC2626"
                                        )
                                    ]
                                )
                            ),

                            self.build_chart_card(

                                "Usuarios por Rol",

                                self.build_pie_chart(

                                    sections=[

                                        ft.PieChartSection(

                                            item["cantidad"],

                                            title=f'''
                                            {item["rol"]}
                                            ({item["cantidad"]})
                                            ''',

                                            radius=90
                                        )

                                        for item in usuarios_roles
                                    ]
                                )
                            )
                        ]
                    ),

                    # =====================================
                    # ROW 5
                    # =====================================

                    ft.ResponsiveRow(

                        spacing=20,
                        run_spacing=20,

                        controls=[

                            self.build_chart_card(

                                "Estudios con Más Recomendaciones",

                                self.build_horizontal_chart(

                                    recomendaciones,

                                    "estudio",

                                    "cantidad_recomendaciones",

                                    "#2563EB"
                                )
                            ),

                            self.build_chart_card(

                                "Estudios Sin Sala",

                                self.build_alert_list(

                                    estudios_sin_sala,

                                    "estudio"
                                )
                            )
                        ]
                    ),

                    # =====================================
                    # ROW 6
                    # =====================================

                    ft.ResponsiveRow(

                        spacing=20,
                        run_spacing=20,

                        controls=[

                            self.build_chart_card(

                                "Preparaciones Asociadas",

                                self.build_pie_chart(

                                    sections=[

                                        ft.PieChartSection(

                                            preparaciones[
                                                "con_preparacion"
                                            ],

                                            title="Con preparación",

                                            radius=90,

                                            color="#2563EB"
                                        ),

                                        ft.PieChartSection(

                                            preparaciones[
                                                "sin_preparacion"
                                            ],

                                            title="Sin preparación",

                                            radius=90,

                                            color="#D1D5DB"
                                        )
                                    ]
                                ),

                                col={
                                    "xs": 12,
                                    "lg": 12
                                },

                                height=500
                            )
                        ]
                    )
                ]
            )
        )