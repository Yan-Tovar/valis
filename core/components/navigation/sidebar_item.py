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

        self.border_radius = 10

        self.padding = 12

        self.ink = True

        self.bgcolor = (

            AppColors.PRIMARY_DARK
            if active
            else "transparent"
        )

        self.on_click = self.navigate

        self.content = ft.Row(

            spacing=15,

            controls=[

                ft.Icon(
                    icon,
                    color=AppColors.WHITE,
                    size=20
                ),

                ft.Text(
                    label,
                    color=AppColors.WHITE,
                    size=14,
                    weight=ft.FontWeight.W_500
                )
            ]
        )


    # -------------------------------------------------
    # NAVIGATE
    # -------------------------------------------------

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