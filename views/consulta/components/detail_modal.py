import flet as ft

from core.theme.colors import AppColors


def show_detail_modal(
    page,
    title,
    controls
):

    dialog = ft.AlertDialog(

        content=ft.Container(

            width=700,

            padding=20,

            content=ft.Column(

                tight=True,

                controls=[

                    ft.Text(
                        title,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=AppColors.PRIMARY
                    ),

                    ft.Divider(),

                    *controls
                ]
            )
        ),

        actions=[

            ft.TextButton(
                "Cerrar",
                on_click=lambda e: close_modal(page)
            )
        ]
    )

    page.dialog = dialog

    dialog.open = True

    page.update()


def close_modal(page):

    page.dialog.open = False

    page.update()