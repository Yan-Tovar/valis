# from core.components.modals.base_modal import (
#     BaseModal
# )

# from core.components.buttons.primary_button import (
#     PrimaryButton
# )

# from core.theme.colors import (
#     AppColors
# )


# class CrudModal:


#     def __init__(
#         self,
#         page,
#         title,
#         form,
#         on_save
#     ):

#         self.page = page

#         self.form = form

#         self.on_save = on_save

#         self.modal = BaseModal(

#             page=page,

#             title=title,

#             content=form,

#             actions=[

#                 PrimaryButton(
#                     text="Cancelar",
#                     color=AppColors.DARK_GRAY,
#                     on_click=lambda e:
#                         self.close()
#                 ).content,

#                 PrimaryButton(
#                     text="Guardar",
#                     on_click=self.save
#                 ).content
#             ]
#         )

#     # -------------------------------------------------
#     # SAVE
#     # -------------------------------------------------

#     def save(self, e):

#         self.on_save(
#             self.form.get_data()
#         )

#     # -------------------------------------------------
#     # OPEN
#     # -------------------------------------------------

#     def open(self):

#         self.modal.open()

#     # -------------------------------------------------
#     # CLOSE
#     # -------------------------------------------------

#     def close(self):

#         self.modal.close()