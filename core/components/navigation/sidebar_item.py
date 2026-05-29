import flet as ft

from core.theme.colors import (
    AppColors
)

from core.router.navigation_service import (
    NavigationService
)


class SidebarItem(ft.Container):

    def __init__(

        self,

        label,

        icon,

        route=None,

        active=False,

        on_click=None
    ):

        super().__init__()

        self.route = route

        self.custom_on_click = on_click

        self.padding = ft.padding.symmetric(

            horizontal=12,
            vertical=10
        )

        self.border_radius = 8

        self.ink = True

        self.bgcolor = (

            AppColors.PRIMARY
            if active
            else "transparent"
        )

        self.on_click = self.navigate

        self.content = ft.Row(

            spacing=10,

            controls=[

                ft.Icon(

                    icon,

                    size=18,

                    color=AppColors.WHITE
                ),

                ft.Text(

                    label,

                    size=13,

                    color=AppColors.WHITE
                )
            ]
        )

    # =================================================
    # NAVIGATE
    # =================================================

    def navigate(
        self,
        e
    ):

        if self.custom_on_click:

            self.custom_on_click()

            return

        if self.route:

            NavigationService.navigate(
                self.route
            )