import flet as ft


class CustomTable:

    @staticmethod
    def build(columns, rows):

        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(col))
                for col in columns
            ],
            rows=rows
        )