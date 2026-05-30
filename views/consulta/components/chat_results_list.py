import flet as ft

from core.theme.colors import AppColors


def build(
    items,
    selected_index,
    on_select
):

    controls = []

    for index, item in enumerate(items):

        title = (
            item.get("nombre")
            or
            item.get("nombre_entidad")
            or
            "Sin nombre"
        )

        subtitle = (
            item.get("codigo_cups")
            or
            item.get("codigo_entidad")
            or
            ""
        )

        is_selected = index == selected_index

        controls.append(

            ft.Container(

                content=ft.Row(

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                    controls=[

                        ft.Column(

                            spacing=2,

                            expand=True,

                            controls=[

                                ft.Text(
                                    title,
                                    size=13,
                                    weight=ft.FontWeight.BOLD
                                ),

                                ft.Text(
                                    subtitle,
                                    size=11,
                                    color=AppColors.TEXT_SECONDARY
                                )
                            ]
                        ),

                        ft.Icon(
                            ft.icons.CHECK_CIRCLE
                            if is_selected
                            else ft.icons.RADIO_BUTTON_UNCHECKED,
                            color=AppColors.PRIMARY
                        )
                    ]
                ),

                padding=12,

                border_radius=15,

                bgcolor=(
                    AppColors.PRIMARY_LIGHT
                    if is_selected
                    else AppColors.WHITE
                ),

                border=ft.border.all(
                    1,
                    AppColors.BORDER
                ),

                ink=True,

                on_click=lambda e, idx=index:
                    on_select(idx),

                margin=ft.margin.only(
                    bottom=8
                )
            )
        )

    return ft.Container(

        height=220,

        content=ft.Column(

            controls=controls,

            spacing=0,

            scroll=ft.ScrollMode.AUTO
        ),

        border_radius=15,

        bgcolor=AppColors.WHITE,

        padding=10,

        border=ft.border.all(
            1,
            AppColors.BORDER
        )
    )