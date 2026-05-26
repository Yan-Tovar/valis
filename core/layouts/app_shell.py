import flet as ft

from core.layouts.sidebar import Sidebar
from core.layouts.topbar import TopBar


class AppShell(ft.Container):

    # =================================================
    # INIT
    # =================================================

    def __init__(self, page: ft.Page):

        super().__init__()

        # Do not set `self.page` — underlying Control may have a read-only `page` property.
        # Keep page available to child components by passing it directly where needed.
        self.expand = True

        # =============================================
        # SIDEBAR
        # =============================================

        self.sidebar = Sidebar(page)

        # =============================================
        # TOPBAR
        # =============================================

        self.topbar = TopBar("Dashboard")

        # =============================================
        # CONTENT
        # =============================================

        self.content_container = ft.Container(
            expand=True
        )

        # =============================================
        # RIGHT SIDE
        # =============================================

        self.right_side = ft.Column(

            expand=True,

            spacing=0,

            controls=[

                self.topbar,

                self.content_container
            ]
        )

        # =============================================
        # LAYOUT
        # =============================================

        self.content = ft.Row(

            expand=True,

            spacing=0,

            controls=[

                self.sidebar,

                self.right_side
            ]
        )

    # =================================================
    # SET VIEW
    # =================================================

    def set_view(

        self,

        title: str,

        content: ft.Control
    ):

        # =============================================
        # TOPBAR
        # =============================================

        self.topbar.set_title(title)

        # =============================================
        # CONTENT
        # =============================================

        self.content_container.content = content

        # =============================================
        # SIDEBAR ACTIVE
        # =============================================

        self.sidebar.refresh_sidebar()