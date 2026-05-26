import flet as ft


class FormModal:

    # ==========================================
    # INIT
    # ==========================================

    def __init__(
        self,
        page,
        title,
        fields,
        on_save,
        width=500
    ):

        self.page = page

        self.title = title

        self.fields = fields

        self.on_save = on_save

        self.width = width

        self.dialog = None

    # ==========================================
    # OBTENER DATOS
    # ==========================================

    def get_data(self):

        data = {}

        for key, field in self.fields.items():

            if isinstance(field, ft.Checkbox):

                data[key] = field.value

            elif isinstance(field, ft.Dropdown):

                data[key] = field.value

            else:

                data[key] = field.value.strip()

        return data

    # ==========================================
    # VALIDAR
    # ==========================================

    def validate(self):

        valid = True

        for key, field in self.fields.items():

            # ======================================
            # SOLO TEXTFIELDS
            # ======================================

            if isinstance(field, ft.TextField):

                # ==================================
                # CAMPOS OPCIONALES
                # ==================================

                optional = getattr(
                    field,
                    "optional",
                    False
                )

                # ==================================
                # VALIDAR SOLO SI ES REQUERIDO
                # ==================================

                if not optional:

                    if not field.value or not field.value.strip():

                        field.error_text = "Campo requerido"

                        valid = False

                    else:

                        field.error_text = None

                else:

                    field.error_text = None

        self.page.update()

        return valid

    # ==========================================
    # GUARDAR
    # ==========================================

    def save(self, e):

        if not self.validate():

            return

        data = self.get_data()

        self.on_save(data)

    # ==========================================
    # CERRAR
    # ==========================================

    def close(self, e=None):

        self.dialog.open = False

        self.page.update()

    # ==========================================
    # FOOTER
    # ==========================================

    def footer(self):

        return [

            # ==================================
            # CANCELAR
            # ==================================

            ft.TextButton(
                "Cancelar",
                on_click=self.close
            ),

            # ==================================
            # GUARDAR
            # ==================================

            ft.ElevatedButton(

                "Guardar",

                icon=ft.icons.SAVE_OUTLINED,

                bgcolor="#43A047",

                color="white",

                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(
                        radius=10
                    ),
                    padding=18
                ),

                on_click=self.save
            )
        ]

    # ==========================================
    # CONTENT
    # ==========================================

    def content(self):

        controls = []

        for field in self.fields.values():

            controls.append(field)

        return ft.Container(

            width=self.width,

            content=ft.Column(

                tight=True,

                scroll=ft.ScrollMode.AUTO,

                spacing=15,

                controls=controls
            )
        )

    # ==========================================
    # BUILD
    # ==========================================

    def build(self):

        self.dialog = ft.AlertDialog(

            modal=True,

            bgcolor="white",

            title=ft.Text(
                self.title,
                size=22,
                weight=ft.FontWeight.BOLD,
                color="#1B5E20"
            ),

            content=self.content(),

            actions=self.footer(),

            actions_alignment=ft.MainAxisAlignment.END
        )

        return self.dialog

    # ==========================================
    # OPEN
    # ==========================================

    def open(self):

        self.page.dialog = self.build()

        self.page.dialog.open = True

        self.page.update()