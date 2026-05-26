import flet as ft

from core.theme.colors import (
    AppColors
)


class Snackbar:


    # ---------------------------------------------------------
    # SHOW
    # ---------------------------------------------------------

    @staticmethod
    def show(
        page,
        message,
        success=True
    ):

        page.snack_bar = ft.SnackBar(

            content=ft.Text(message),

            bgcolor=(

                AppColors.SUCCESS
                if success
                else AppColors.RED
            )
        )

        page.snack_bar.open = True

        page.update()


    # ---------------------------------------------------------
    # SUCCESS
    # ---------------------------------------------------------

    @staticmethod
    def success(
        page,
        message
    ):

        Snackbar.show(
            page,
            message,
            success=True
        )


    # ---------------------------------------------------------
    # ERROR
    # ---------------------------------------------------------

    @staticmethod
    def error(
        page,
        message
    ):

        Snackbar.show(
            page,
            message,
            success=False
        )