import flet as ft

from core.theme.colors import AppColors
from core.components.buttons.primary_button import PrimaryButton


def build_backup_section(
    title,
    subtitle,
    icon,
    button_text,
    button_icon,
    path_text,
    select_text,
    on_select,
    on_action
):

    return ft.Container(

        bgcolor=ft.colors.WHITE,

        border_radius=16,

        padding=20,

        border=ft.border.all(
            1,
            AppColors.BORDER
        ),

        content=ft.Column(

            spacing=15,

            controls=[

                ft.Row(

                    controls=[

                        ft.Icon(
                            icon,
                            color=AppColors.PRIMARY,
                            size=28
                        ),

                        ft.Text(
                            title,
                            size=18,
                            weight=ft.FontWeight.BOLD
                        )
                    ]
                ),

                ft.Text(
                    subtitle,
                    size=12,
                    color=AppColors.TEXT_SECONDARY
                ),

                ft.Container(

                    padding=10,

                    border_radius=10,

                    bgcolor=AppColors.LIGHT_GRAY,

                    content=ft.Text(
                        path_text,
                        size=11
                    )
                ),

                ft.Row(

                    spacing=10,

                    controls=[

                        ft.ElevatedButton(

                            select_text,

                            icon=ft.icons.FOLDER_OPEN,

                            on_click=on_select,

                            expand=True
                        ),

                        PrimaryButton(

                            text=button_text,

                            icon=button_icon,

                            on_click=on_action,

                            expand=True
                        )
                    ]
                )
            ]
        )
    )