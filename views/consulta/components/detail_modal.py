import flet as ft

from core.theme.colors import AppColors


def show_detail_modal(page, title, controls):
    """Show an AlertDialog with provided controls (list of controls or text)."""
    content = ft.Column(controls=controls, tight=True)

    dialog = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(title, weight=ft.FontWeight.BOLD, size=14, color=AppColors.PRIMARY),
                    ft.Divider(),
                    content
                ]
            ),
            padding=ft.padding.all(12),
            width=600
        ),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: _close(page))
        ]
    )

    page.dialog = dialog
    dialog.open = True
    page.update()


def _close(page):
    page.dialog.open = False
    page.update()
