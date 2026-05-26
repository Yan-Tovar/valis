import flet as ft

from core.theme.colors import AppColors


def build(item, is_selected, on_select, index):
    bg_color = AppColors.PRIMARY_LIGHT if is_selected else AppColors.WHITE
    border_color = AppColors.PRIMARY if is_selected else AppColors.BORDER
    title = item.get('nombre') or item.get('nombre_entidad') or item.get('codigo_cups', 'Sin nombre')
    subtitle = item.get('codigo_cups') or item.get('codigo_entidad') or item.get('sigla', '')
    extra = item.get('sigla', '') if item.get('codigo_cups') else item.get('nombre_entidad', '')

    # Icono de verificación cuando está seleccionado
    check_icon = ft.Icon(
        ft.icons.CHECK_CIRCLE,
        color=AppColors.PRIMARY,
        size=20
    ) if is_selected else ft.Icon(
        ft.icons.CIRCLE_OUTLINED,
        color=AppColors.BORDER,
        size=20
    )

    controls = [
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    spacing=4,
                    expand=True,
                    controls=[
                        ft.Text(title, weight=ft.FontWeight.BOLD),
                        ft.Text(subtitle, size=12, color=AppColors.TEXT_SECONDARY)
                    ]
                ),
                check_icon
            ]
        )
    ]

    if extra:
        controls.append(ft.Text(extra, size=12, color=AppColors.TEXT_SECONDARY))

    return ft.Container(
        content=ft.Column(
            spacing=6,
            controls=controls
        ),
        padding=12,
        border_radius=10,
        border=ft.border.all(2, border_color),
        bgcolor=bg_color,
        ink=True,
        on_click=lambda e, idx=index: on_select(idx),
        margin=ft.margin.only(bottom=8)
    )
