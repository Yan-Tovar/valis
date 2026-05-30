# from core.theme.colors import AppColors
# import flet as ft

# from auth.session_manager import SessionManager


# def build_resultado_completo(data, on_open_detail=None):
#     """
#     Return a list of compact controls for the full result view.
#     on_open_detail is a callable(payload) that will be called by link buttons.
#     """

#     # =====================================================
#     # USER SESSION
#     # =====================================================
#     user = SessionManager.current_user()

#     username = (
#         user.get("nombre_completo", "Usuario")
#         if user
#         else "Usuario"
#     )

#     # =====================================================
#     # DATA
#     # =====================================================

#     controls = []

#     estudio = data.get("estudio", {})
#     salas = data.get("salas", [])
#     contrato = data.get("contrato", {})
#     entidad = data.get("entidad", {})
#     preparacion = data.get("preparacion", {})
#     listas = data.get("lista_preparaciones", [])

#     recomendaciones_estudio = data.get(
#         "recomendaciones_estudio",
#         []
#     )

#     recomendaciones_entidad = data.get(
#         "recomendaciones_entidad",
#         []
#     )

#     # =====================================================
#     # ESTUDIO
#     # =====================================================

#     estudio_name = estudio.get(
#         "nombre",
#         "Estudio"
#     )

#     controls.append(

#         ft.Row(

#             controls=[

#                 ft.Text(
#                     f"Estudio: {estudio_name}",
#                     size=12,
#                     weight=ft.FontWeight.BOLD
#                 ),

#                 ft.TextButton(
#                     "Ver estudio",
#                     on_click=lambda e, p=estudio:
#                     on_open_detail(p)
#                     if on_open_detail
#                     else None
#                 )
#             ]
#         )
#     )

#     # =====================================================
#     # SALAS
#     # =====================================================

#     if salas:

#         controls.append(

#             ft.Text(
#                 "Salas disponibles:",
#                 size=12,
#                 weight=ft.FontWeight.BOLD,
#                 color=AppColors.PRIMARY
#             )
#         )

#         for s in salas:

#             code = s.get(
#                 "codigo",
#                 s.get("codigo_sala", "")
#             )

#             name = s.get("nombre", "")

#             controls.append(

#                 ft.Row(

#                     controls=[

#                         ft.Text(
#                             "•",
#                             size=12,
#                             color=AppColors.TEXT_SECONDARY
#                         ),

#                         ft.Text(
#                             f"{code} {name}",
#                             size=11
#                         ),

#                         ft.TextButton(
#                             "Ver",
#                             on_click=lambda e, p=s:
#                             on_open_detail(p)
#                             if on_open_detail
#                             else None
#                         )
#                     ]
#                 )
#             )

#     # =====================================================
#     # CONTRATO
#     # =====================================================

#     if contrato:

#         controls.append(

#             ft.Text(
#                 "Contrato:",
#                 size=12,
#                 weight=ft.FontWeight.BOLD,
#                 color=AppColors.PRIMARY
#             )
#         )

#         controls.append(

#             ft.Row(

#                 controls=[

#                     ft.Text(
#                         f"{contrato.get('codigo', contrato.get('id', ''))} - "
#                         f"{contrato.get('nombre', '')}",
#                         size=11
#                     ),

#                     ft.TextButton(
#                         "Ver",
#                         on_click=lambda e, p=contrato:
#                         on_open_detail(p)
#                         if on_open_detail
#                         else None
#                     )
#                 ]
#             )
#         )

#     # =====================================================
#     # ENTIDAD
#     # =====================================================

#     if entidad:

#         controls.append(

#             ft.Text(
#                 "Entidad:",
#                 size=12,
#                 weight=ft.FontWeight.BOLD,
#                 color=AppColors.PRIMARY
#             )
#         )

#         controls.append(

#             ft.Row(

#                 controls=[

#                     ft.Text(
#                         f"{entidad.get('codigo', entidad.get('entidad_id', ''))} - "
#                         f"{entidad.get('nombre_entidad', '')}",
#                         size=11
#                     ),

#                     ft.TextButton(
#                         "Ver",
#                         on_click=lambda e, p=entidad:
#                         on_open_detail(p)
#                         if on_open_detail
#                         else None
#                     )
#                 ]
#             )
#         )

#     # =====================================================
#     # PREPARACION
#     # =====================================================

#     if preparacion:

#         controls.append(

#             ft.Text(
#                 "Preparación:",
#                 size=12,
#                 weight=ft.FontWeight.BOLD,
#                 color=AppColors.PRIMARY
#             )
#         )

#         controls.append(

#             ft.Row(

#                 controls=[

#                     ft.Text(
#                         f"{preparacion.get('codigo', '')} - "
#                         f"{preparacion.get('nombre', '')}",
#                         size=11
#                     ),

#                     ft.TextButton(
#                         "Ver",
#                         on_click=lambda e, p=preparacion:
#                         on_open_detail(p)
#                         if on_open_detail
#                         else None
#                     )
#                 ]
#             )
#         )

#     # =====================================================
#     # LISTA PREPARACIONES
#     # =====================================================

#     if listas:

#         controls.append(

#             ft.Text(
#                 "Lista de preparaciones:",
#                 size=12,
#                 weight=ft.FontWeight.BOLD,
#                 color=AppColors.PRIMARY
#             )
#         )

#         for l in listas:

#             controls.append(

#                 ft.Row(

#                     controls=[

#                         ft.Text(
#                             "•",
#                             size=11,
#                             color=AppColors.TEXT_SECONDARY
#                         ),

#                         ft.Text(
#                             l.get("nombre", ""),
#                             size=11
#                         )
#                     ]
#                 )
#             )

#     # =====================================================
#     # RECOMENDACIONES
#     # =====================================================

#     if (
#         recomendaciones_entidad
#         or recomendaciones_estudio
#     ):

#         rec_controls = []

#         # ---------------------------------------------
#         # ENTIDAD RECOMENDACIONES
#         # ---------------------------------------------

#         if recomendaciones_entidad:

#             rec_controls.append(

#                 ft.Text(
#                     f"{username}, recuerde que la entidad hace estas recomendaciones:",
#                     size=11,
#                     weight=ft.FontWeight.BOLD,
#                     color=AppColors.WHITE
#                 )
#             )

#             for r in recomendaciones_entidad:

#                 rec_controls.append(

#                     ft.Row(

#                         controls=[

#                             ft.Text(
#                                 "•",
#                                 size=11,
#                                 color=AppColors.WHITE
#                             ),

#                             ft.Text(
#                                 r.get("texto", str(r)),
#                                 size=11,
#                                 color=AppColors.WHITE
#                             )
#                         ]
#                     )
#                 )

#         # ---------------------------------------------
#         # ESTUDIO RECOMENDACIONES
#         # ---------------------------------------------

#         if recomendaciones_estudio:

#             rec_controls.append(

#                 ft.Text(
#                     f"{username}, el estudio tiene estas recomendaciones:",
#                     size=11,
#                     weight=ft.FontWeight.BOLD,
#                     color=AppColors.WHITE
#                 )
#             )

#             for r in recomendaciones_estudio:

#                 rec_controls.append(

#                     ft.Row(

#                         controls=[

#                             ft.Text(
#                                 "•",
#                                 size=11,
#                                 color=AppColors.WHITE
#                             ),

#                             ft.Text(
#                                 r.get("texto", str(r)),
#                                 size=11,
#                                 color=AppColors.WHITE
#                             )
#                         ]
#                     )
#                 )

#         controls.append(

#             ft.Container(

#                 content=ft.Column(
#                     controls=rec_controls,
#                     tight=True
#                 ),

#                 padding=ft.padding.all(10),

#                 bgcolor=AppColors.RED,

#                 border_radius=10,

#                 margin=ft.margin.only(top=10)
#             )
#         )

#     return controls


# def build_error(message):

#     return [

#         ft.Card(

#             content=ft.Container(

#                 padding=15,

#                 content=ft.Text(message)
#             )
#         )
#     ]