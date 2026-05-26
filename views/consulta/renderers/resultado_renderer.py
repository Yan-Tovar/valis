import flet as ft

from .resultado_renderer_old import (
    build_resultado_completo
)


def build(
    data,
    on_open_detail
):

    return ft.Column(

        spacing=10,

        controls=build_resultado_completo(
            data,
            on_open_detail
        )
    )