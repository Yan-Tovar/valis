# from services.response import ServiceResponse


# def is_admin(usuario):

#     if not usuario:
#         return False

#     return usuario.rol == "administrador"



# def validate_admin(usuario):

#     if not usuario:

#         return ServiceResponse(
#             success=False,
#             message="Usuario no autenticado"
#         )

#     if usuario.rol != "administrador":

#         return ServiceResponse(
#             success=False,
#             message="No tienes permisos para esta acción"
#         )

#     return ServiceResponse(success=True)