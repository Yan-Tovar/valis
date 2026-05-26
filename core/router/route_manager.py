from views.splash.splash_view import (
    SplashView
)

from views.auth.login_view import (
    LoginView
)

from views.dashboard.dashboard_view import (
    DashboardView
)

from views.consulta.consulta_view import (
    ConsultaView
)

from views.usuarios.usuarios_view import (
    UsuariosView
)

from views.estudios.estudios_view import (
    EstudiosView
)

from views.salas.salas_view import (
    SalasView
)

from views.contratos.contratos_view import (
    ContratosView
)

from views.entidades_contratos.entidades_contratos_view import (
    EntidadesContratosView
)

from views.entidades_contratos_estudios.entidades_contratos_estudios_view import (
    EntidadesContratosEstudiosView
)

from views.estudios_salas.estudios_salas_view import (
    EstudiosSalasView
)

from views.preparaciones.preparaciones_view import (
    PreparacionesView
)

from views.lista_preparaciones.lista_preparaciones_view import (
    ListaPreparacionesView
)

from views.lista_preparaciones_preparaciones.lista_preparaciones_preparaciones_view import (
    ListaPreparacionesPreparacionesView
)

from views.recomendaciones_entidades.recomendaciones_entidades_view import (
    RecomendacionesEntidadesView
)

from views.recomendaciones_estudio.recomendaciones_estudio_view import (
    RecomendacionesEstudioView
)

from core.router.routes import (
    Routes
)

from views.entidades.entidades_view import (
    EntidadesView
)


class RouteManager:


    @staticmethod
    def get_view(
        page,
        route
    ):

        routes = {

            Routes.SPLASH:
                SplashView(page),

            Routes.LOGIN:
                LoginView(page),
            
            Routes.ENTIDADES:
                EntidadesView(page),
            
            Routes.DASHBOARD:
                DashboardView(page),
            
            Routes.CONSULTA:
                ConsultaView(page),
            
            Routes.USUARIOS:
                UsuariosView(page),

            Routes.ESTUDIOS:
                EstudiosView(page),

            Routes.SALAS:
                SalasView(page),
            
            Routes.CONTRATOS:
                ContratosView(page),
            
            Routes.ENTIDADES_CONTRATOS:
                EntidadesContratosView(page),
            
            Routes.ENTIDADES_CONTRATOS_ESTUDIOS:
                EntidadesContratosEstudiosView(page),
            
            Routes.ESTUDIOS_SALAS:
                EstudiosSalasView(page),

            Routes.PREPARACIONES:
                PreparacionesView(page),

            Routes.LISTA_PREPARACIONES:
                ListaPreparacionesView(page),
            
            Routes.LISTA_PREPARACIONES_PREPARACIONES:
                ListaPreparacionesPreparacionesView(page),
            
            Routes.RECOMENDACIONES_ENTIDADES:
                RecomendacionesEntidadesView(page),

            Routes.RECOMENDACIONES_ESTUDIOS:
                RecomendacionesEstudioView(page)
        }

        return routes.get(route)