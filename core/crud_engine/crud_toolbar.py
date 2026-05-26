import flet as ft

from core.components.buttons.primary_button import (
    PrimaryButton
)


class CrudToolbar(ft.Container):


    def __init__(
        self,
        title,
        on_create,
        on_search=None
    ):

        super().__init__()

        self.search_input = ft.TextField(
            width=300,
            hint_text="Buscar...",
            autofocus=False,
            on_submit=lambda e: on_search(e.control.value) if on_search else None
        )

        self.content = ft.Row(

            alignment=(
                ft.MainAxisAlignment.SPACE_BETWEEN
            ),

            controls=[

                ft.Row(

                    spacing=10,

                    controls=[

                        ft.Text(

                            title,

                            size=28,

                            weight=ft.FontWeight.BOLD
                        ),

                        self.search_input,

                        ft.IconButton(

                            icon=ft.icons.SEARCH,

                            tooltip="Buscar",

                            on_click=lambda e: on_search(self.search_input.value) if on_search else None
                        )
                    ]
                ),

                PrimaryButton(

                    text="Nuevo",

                    icon=ft.icons.ADD,

                    on_click=lambda e:
                    on_create()
                )
            ]
        )