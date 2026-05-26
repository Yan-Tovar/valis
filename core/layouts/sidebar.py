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

        # store page under a private name to avoid colliding with Control.page property
        self._page = page

        self.width = 280

        self.expand = False

        self.bgcolor = AppColors.SIDEBAR

        self.border = ft.border.only(

            right=ft.BorderSide(
                1,
                AppColors.BORDER
            )
        )

        # =============================================
        # USER NAME
        # =============================================

        self.user_name = ft.Text(
            "",
            color=AppColors.WHITE,
            size=14,
            weight=ft.FontWeight.BOLD
        )

        # =============================================
        # USER ROLE
        # =============================================

        self.user_role = ft.Text(
            "",
            color=AppColors.WHITE70,
            size=12
        )

        # =============================================
        # MENU COLUMN
        # =============================================

        self.menu_column = ft.Column(
            expand=True,
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )

        # =============================================
        # CONTENT
        # =============================================

        self.content = ft.Column(

            expand=True,

            spacing=0,

            controls=[

                # =====================================
                # HEADER
                # =====================================

                ft.Container(
                    padding=20,
                    content=SidebarHeader()
                ),

                # =====================================
                # DIVIDER
                # =====================================

                ft.Container(
                    height=1,
                    bgcolor=AppColors.BORDER
                ),

                # =====================================
                # USER INFO
                # =====================================

                ft.Container(

                    padding=20,

                    border=ft.border.only(

                        bottom=ft.BorderSide(
                            1,
                            AppColors.BORDER
                        )
                    ),

                    content=ft.Column(

                        spacing=4,

                        controls=[

                            self.user_name,

                            self.user_role
                        ]
                    )
                ),

                # =====================================
                # MENU
                # =====================================

                ft.Container(

                    expand=True,

                    padding=20,

                    content=self.menu_column
                )
            ]
        )

        # =============================================
        # INITIAL LOAD
        # =============================================

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
    # LOAD MENU
    # =================================================

    def load_menu(self):

        self.menu_column.controls = [

            *self.build_sections(),

            ft.Container(expand=True),

            SidebarItem(

                label="Salir",

                icon="logout",

                on_click=NavigationService.logout
            )
        ]

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
            if self._page is not None
            else None
        )

        sections = {}

        # =============================================
        # GROUP ITEMS
        # =============================================

        for item in MENU_REGISTRY:

            if user_role not in item["roles"]:
                continue

            section_name = item["section"]

            if section_name not in sections:

                sections[section_name] = []

            sections[section_name].append(

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

        # =============================================
        # BUILD CONTROLS
        # =============================================

        controls = []

        for section_name, items in sections.items():

            controls.append(

                SidebarSection(

                    title=section_name,

                    controls=items
                )
            )

        return controls

    # =================================================
    # REFRESH
    # =================================================

    def refresh_sidebar(self):

        self.load_user()

        self.load_menu()