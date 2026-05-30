import flet as ft

from core.theme.colors import (
    AppColors
)

from core.components.navigation.sidebar_item import (
    SidebarItem
)

from core.components.navigation.sidebar_header import (
    SidebarHeader
)

from core.components.navigation.sidebar_section import (
    SidebarSection
)

from auth.session_manager import (
    SessionManager
)

from core.router.navigation_service import (
    NavigationService
)

from core.navigation.menu_registry import (
    MENU_REGISTRY
)


class Sidebar(ft.Container):

    # =================================================
    # INIT
    # =================================================

    def __init__(
        self,
        page: ft.Page
    ):

        super().__init__()

        self._page = page

        self.width = 260

        self.bgcolor = AppColors.SIDEBAR

        self.border = ft.border.only(

            right=ft.BorderSide(
                1,
                AppColors.BORDER
            )
        )

        self.expand = False

        self.active_section = None

        # =================================================
        # USER INFO
        # =================================================

        self.user_name = ft.Text(

            "",
            size=14,
            weight=ft.FontWeight.BOLD,
            color=AppColors.WHITE
        )

        self.user_role = ft.Text(

            "",
            size=11,
            color=AppColors.WHITE70
        )

        # =================================================
        # MENU
        # =================================================

        self.menu_column = ft.Column(

            spacing=8,

            expand=True
        )

        # =================================================
        # CONTENT
        # =================================================

        self.content = ft.Column(

            expand=True,

            spacing=0,

            controls=[

                # HEADER
                ft.Container(

                    padding=20,

                    content=SidebarHeader()
                ),

                # DIVIDER
                ft.Container(

                    height=1,

                    bgcolor=AppColors.BORDER
                ),

                # USER INFO
                ft.Container(

                    padding=20,

                    border=ft.border.only(

                        bottom=ft.BorderSide(
                            1,
                            AppColors.BORDER
                        )
                    ),

                    content=ft.Column(

                        spacing=2,

                        controls=[

                            self.user_name,

                            self.user_role
                        ]
                    )
                ),

                # MENU
                ft.Container(

                    expand=True,

                    padding=15,

                    content=self.menu_column
                ),

                # FOOTER
                ft.Container(

                    padding=15,

                    border=ft.border.only(

                        top=ft.BorderSide(
                            1,
                            AppColors.BORDER
                        )
                    ),

                    content=SidebarItem(

                        label="Cerrar sesión",

                        icon=ft.icons.LOGOUT_ROUNDED,

                        on_click=NavigationService.logout
                    )
                )
            ]
        )

        self.load_user()
        self.load_menu()

    # =================================================
    # LOAD USER
    # =================================================

    def load_user(self):

        user = SessionManager.current_user()

        if not user:

            self.user_name.value = ""
            self.user_role.value = ""

            return

        self.user_name.value = (
            user["nombre_completo"]
        )

        self.user_role.value = (
            user["rol"]
        )

    # =================================================
    # TOGGLE SECTION
    # =================================================

    def toggle_section(
        self,
        section_name
    ):

        if self.active_section == section_name:

            self.active_section = None

        else:

            self.active_section = section_name

        self.load_menu()

        if self.page:

            self.update()

    # =================================================
    # LOAD MENU
    # =================================================

    def load_menu(self):

        self.menu_column.controls = (
            self.build_sections()
        )

    # =================================================
    # BUILD SECTIONS
    # =================================================

    def build_sections(self):

        user = SessionManager.current_user()

        if not user:
            return []

        user_role = user["rol"]

        current_route = (
            self._page.route
        )

        sections = {}

        # =================================================
        # GROUP ITEMS
        # =================================================

        for item in MENU_REGISTRY:

            # LOGIN NEVER
            if item["route"] == "/login":
                continue

            # ROLE FILTER
            if user_role not in item["roles"]:
                continue

            # LECTOR ONLY CONSULTAS
            if (
                user_role == "LECTOR"
                and item["section"] != "Consulta"
            ):
                continue
            
            section = item["section"]

            if section not in sections:

                sections[section] = []

            sections[section].append(

                SidebarItem(

                    label=item["label"],

                    icon=item["icon"],

                    route=item["route"],

                    active=(
                        current_route ==
                        item["route"]
                    )
                )
            )

        # =================================================
        # BUILD CONTROLS
        # =================================================

        controls = []

        for section_name, items in sections.items():

            controls.append(

                SidebarSection(

                    title=section_name,

                    controls=items,

                    opened=(
                        self.active_section ==
                        section_name
                    ),

                    on_toggle=lambda e,
                    name=section_name:
                    self.toggle_section(name)
                )
            )

        return controls

    # =================================================
    # REFRESH
    # =================================================

    def refresh_sidebar(self):

        self.load_user()

        self.load_menu()

        if self.page:

            self.update()