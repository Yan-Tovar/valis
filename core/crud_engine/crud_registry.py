from core.services.usuario_service import (
    UsuarioService
)

from core.services.entidad_service import (
    EntidadService
)

from core.services.estudio_service import (
    EstudioService
)

from core.services.contrato_service import (
    ContratoService
)

from core.services.entidad_contrato_service import (
    EntidadContratoService
)

from core.services.entidad_contrato_estudio_service import (
    EntidadContratoEstudioService
)

from core.services.estudio_sala_service import (
    EstudioSalaService
)

from core.services.lista_preparacion_service import (
    ListaPreparacionService
)

from core.services.lista_preparacion_preparacion_service import (
    ListaPreparacionPreparacionService
)

from core.services.preparacion_service import (
    PreparacionService
)

from core.services.recomendacion_entidad_service import (
    RecomendacionEntidadService
)

from core.services.recomendacion_estudio_service import (
    RecomendacionEstudioService
)

from core.services.sala_service import (
    SalaService
)

from database.models import (

    Usuario,

    Entidad,

    Estudio,

    Contrato,

    EntidadContrato,

    EntidadContratoEstudio,

    EstudioSala,

    ListaPreparacion,

    ListaPreparacionPreparacion,

    Preparacion,

    RecomendacionEntidad,

    RecomendacionEstudio,

    Sala
)


CRUD_REGISTRY = {

    # ---------------------------------------------------------
    # USUARIOS
    # ---------------------------------------------------------

    "usuarios": {

        "title": "Usuarios",

        "model": Usuario,

        "service": UsuarioService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "nombre_usuario",
                "label": "Usuario"
            },

            {
                "name": "nombre_completo",
                "label": "Nombre"
            },

            {
                "name": "rol",
                "label": "Rol"
            },

            {
                "name": "estado",
                "label": "Estado"
            }
        ],

        "fields": [

            {
                "name": "nombre_usuario",
                "label": "Usuario"
            },

            {
                "name": "nombre_completo",
                "label": "Nombre completo"
            },

            {
                "name": "password",
                "label": "Contraseña",
                "type": "password"
            },

            {
                "name": "rol",
                "label": "Rol",
                "type": "select",

                "options": [

                    "ADMIN",

                    "LECTOR"
                ]
            }
        ]
    },

    # ---------------------------------------------------------
    # ENTIDADES
    # ---------------------------------------------------------

    "entidades": {

        "title": "Entidades",

        "model": Entidad,

        "service": EntidadService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "codigo_entidad",
                "label": "Código"
            },

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "ubicacion",
                "label": "Ubicación"
            },

            {
                "name": "estado",
                "label": "Estado"
            }
        ],

        "fields": [

            {
                "name": "codigo_entidad",
                "label": "Código"
            },

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "ubicacion",
                "label": "Ubicación"
            }
        ]
    },

    # ---------------------------------------------------------
    # ESTUDIOS
    # ---------------------------------------------------------

    "estudios": {

        "title": "Estudios",

        "model": Estudio,

        "service": EstudioService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "codigo_cups",
                "label": "Código"
            },

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "sigla",
                "label": "Sigla"
            },

            {
                "name": "estado",
                "label": "Estado"
            }
        ],

        "fields": [

            {
                "name": "codigo_cups",
                "label": "Código CUPS"
            },

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "sigla",
                "label": "Sigla"
            },

            {
                "name": "descripcion",
                "label": "Descripción",
                "type": "textarea"
            }
        ]
    },

    # ---------------------------------------------------------
    # CONTRATOS
    # ---------------------------------------------------------

    "contratos": {

        "title": "Contratos",

        "model": Contrato,

        "service": ContratoService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "fecha_inicio",
                "label": "Inicio"
            },

            {
                "name": "fecha_fin",
                "label": "Fin"
            }
        ],

        "fields": [

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "fecha_inicio",
                "label": "Fecha inicio",
                "type": "date"
            },

            {
                "name": "fecha_fin",
                "label": "Fecha fin",
                "type": "date"
            },

            {
                "name": "descripcion",
                "label": "Descripción",
                "type": "textarea"
            }
        ]
    },

    # ---------------------------------------------------------
    # ENTIDADES CONTRATOS
    # ---------------------------------------------------------

    "entidades_contratos": {

        "title": "Entidades Contratos",

        "model": EntidadContrato,

        "service": EntidadContratoService,

        "pdf_enabled": False,

        "columns": [

            {
                "name": "entidad",
                "label": "Entidad"
            },

            {
                "name": "contrato",
                "label": "Contrato"
            },

            {
                "name": "observaciones",
                "label": "Observaciones"
            }
        ],

        "fields": [

            {
                "name": "entidad_id",
                "label": "Entidad"
            },

            {
                "name": "contrato_id",
                "label": "Contrato"
            },

            {
                "name": "observaciones",
                "label": "Observaciones",
                "type": "textarea"
            }
        ]
    },

    # ---------------------------------------------------------
    # ENTIDADES CONTRATOS ESTUDIOS
    # ---------------------------------------------------------

    "entidades_contratos_estudios": {

        "title": "Contratos Estudios",

        "model": EntidadContratoEstudio,

        "service": EntidadContratoEstudioService,

        "pdf_enabled": False,

        "columns": [

            {
                "name": "entidad_contrato.contrato.nombre",
                "label": "Contrato"
            },

            {
                "name": "estudio.nombre",
                "label": "Estudio"
            },

            {
                "name": "valor_estudio",
                "label": "Valor"
            }
        ],

        "fields": [

            {
                "name": "entidad_contrato_id",
                "label": "Entidad contrato",
                "type": "relationship"
            },

            {
                "name": "estudio_id",
                "label": "Estudio",
                "type": "relationship"
            },

            {
                "name": "valor_estudio",
                "label": "Valor",
                "type": "number"
            }
        ]
    },

    # ---------------------------------------------------------
    # ESTUDIOS SALAS
    # ---------------------------------------------------------

    "estudios_salas": {

        "title": "Estudios Salas",

        "model": EstudioSala,

        "service": EstudioSalaService,

        "pdf_enabled": False,

        "columns": [

            {
                "name": "estudio.nombre",
                "label": "Estudio"
            },

            {
                "name": "sala.nombre",
                "label": "Sala"
            }
        ],

        "fields": [

            {
                "name": "estudio_id",
                "label": "Estudio",
                "type": "relationship"
            },

            {
                "name": "sala_id",
                "label": "Sala",
                "type": "relationship"
            },

            {
                "name": "observaciones",
                "label": "Observaciones",
                "type": "textarea"
            }
        ]
    },

    # ---------------------------------------------------------
    # SALAS
    # ---------------------------------------------------------

    "salas": {

        "title": "Salas",

        "model": Sala,

        "service": SalaService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "codigo_sala",
                "label": "Código"
            },

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "sede",
                "label": "Sede"
            },

            {
                "name": "estado",
                "label": "Estado"
            }
        ],

        "fields": [

            {
                "name": "codigo_sala",
                "label": "Código"
            },

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "sede",
                "label": "Sede"
            },

            {
                "name": "localizacion",
                "label": "Localización"
            },

            {
                "name": "representante",
                "label": "Representante"
            }
        ]
    },

    # ---------------------------------------------------------
    # PREPARACIONES
    # ---------------------------------------------------------

    "preparaciones": {

        "title": "Preparaciones",

        "model": Preparacion,

        "service": PreparacionService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "codigo_preparacion",
                "label": "Código"
            },

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "estudio.nombre",
                "label": "Estudio"
            },

            {
                "name": "estado",
                "label": "Estado"
            }
        ],

        "fields": [

            {
                "name": "codigo_preparacion",
                "label": "Código"
            },

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "estudio_id",
                "label": "Estudio",
                "type": "relationship"
            }
        ]
    },

    # ---------------------------------------------------------
    # LISTA PREPARACIONES
    # ---------------------------------------------------------

    "lista_preparaciones": {

        "title": "Lista Preparaciones",

        "model": ListaPreparacion,

        "service": ListaPreparacionService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "estado",
                "label": "Estado"
            }
        ],

        "fields": [

            {
                "name": "nombre",
                "label": "Nombre"
            },

            {
                "name": "detalle",
                "label": "Detalle",
                "type": "textarea"
            }
        ]
    },

    # ---------------------------------------------------------
    # LISTA PREPARACIONES PREPARACIONES
    # ---------------------------------------------------------

    "lista_preparaciones_preparaciones": {

        "title": "Preparaciones Listas",

        "model": ListaPreparacionPreparacion,

        "service": ListaPreparacionPreparacionService,

        "pdf_enabled": False,

        "columns": [

            {
                "name": "preparacion.nombre",
                "label": "Preparación"
            },

            {
                "name": "lista_preparacion.nombre",
                "label": "Lista"
            }
        ],

        "fields": [

            {
                "name": "preparacion_id",
                "label": "Preparación",
                "type": "relationship"
            },

            {
                "name": "lista_preparacion_id",
                "label": "Lista",
                "type": "relationship"
            },

            {
                "name": "observacion",
                "label": "Observación",
                "type": "textarea"
            }
        ]
    },

    # ---------------------------------------------------------
    # RECOMENDACIONES ENTIDADES
    # ---------------------------------------------------------

    "recomendaciones_entidades": {

        "title": "Recomendaciones Entidades",

        "model": RecomendacionEntidad,

        "service": RecomendacionEntidadService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "titulo",
                "label": "Título"
            },

            {
                "name": "entidad.nombre",
                "label": "Entidad"
            },

            {
                "name": "estado",
                "label": "Estado"
            }
        ],

        "fields": [

            {
                "name": "titulo",
                "label": "Título"
            },

            {
                "name": "entidad_id",
                "label": "Entidad",
                "type": "relationship"
            },

            {
                "name": "descripcion",
                "label": "Descripción",
                "type": "textarea"
            }
        ]
    },

    # ---------------------------------------------------------
    # RECOMENDACIONES ESTUDIO
    # ---------------------------------------------------------

    "recomendaciones_estudio": {

        "title": "Recomendaciones Estudios",

        "model": RecomendacionEstudio,

        "service": RecomendacionEstudioService,

        "pdf_enabled": True,

        "columns": [

            {
                "name": "titulo",
                "label": "Título"
            },

            {
                "name": "estudio.nombre",
                "label": "Estudio"
            }
        ],

        "fields": [

            {
                "name": "titulo",
                "label": "Título"
            },

            {
                "name": "estudio_id",
                "label": "Estudio",
                "type": "relationship"
            },

            {
                "name": "descripcion",
                "label": "Descripción",
                "type": "textarea"
            }
        ]
    }
}