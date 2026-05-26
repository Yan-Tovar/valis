# import flet as ft

# from core.theme.colors import (
#     AppColors
# )


# class BaseModal:


#     def __init__(
#         self,
#         page,
#         title,
#         content,
#         actions=None,
#         width=700
#     ):

#         self.page = page

#         self.dialog = ft.AlertDialog(

#             modal=True,

#             title=ft.Text(
#                 title,
#                 size=22,
#                 weight=ft.FontWeight.BOLD
#             ),

#             content=ft.Container(

#                 content=content,

#                 width=width,

#                 padding=20
#             ),

#             actions=actions or [],

#             bgcolor=AppColors.WHITE,

#             on_dismiss=lambda e: self.cleanup()
#         )

#     # -------------------------------------------------
#     # OPEN
#     # -------------------------------------------------

#     def open(self):

#         self.page.dialog = self.dialog

#         self.dialog.open = True

#         self.page.update()

#     # -------------------------------------------------
#     # CLOSE
#     # -------------------------------------------------

#     def close(self):

#         self.dialog.open = False

#         self.page.update()

#         self.cleanup()

#     # -------------------------------------------------
#     # CLEANUP
#     # -------------------------------------------------

#     def cleanup(self):

#         if self.page.dialog == self.dialog:

#             self.page.dialog = None