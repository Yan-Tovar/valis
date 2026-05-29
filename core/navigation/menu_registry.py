import flet as ft

from core.router.routes import (
    Routes
)

from core.security.permissions import (
    Permissions
)

MENU_REGISTRY = [

    # -------------------------------------------------
    # GENERAL
    # -------------------------------------------------

    {
        "section": "General",

        "label": "Inicio",

        "icon": "dashboard",

        "route": Routes.DASHBOARD,

        "roles": [
            Permissions.ADMIN,
            Permissions.LECTOR
        ]
    },

    {
        "section": "General",

        "label": "Entidades",

        "icon": "apartment",

        "route": Routes.ENTIDADES,

        "roles": [
            Permissions.ADMIN,
            Permissions.LECTOR
        ]
    },

    {
        "section": "General",

        "label": "Estudios",

        "icon": "biotech",

        "route": Routes.ESTUDIOS,

        "roles": [
            Permissions.ADMIN,
            Permissions.LECTOR
        ]
    },

    {
        "section": "Consulta",

        "label": "Consulta",

        "icon": "search",

        "route": Routes.CONSULTA,

        "roles": [
            Permissions.ADMIN,
            Permissions.LECTOR
        ]
    },

    {
        "section": "General",

        "label": "Salas",

        "icon": "meeting_room",

        "route": Routes.SALAS,

        "roles": [
            Permissions.ADMIN,
            Permissions.LECTOR
        ]
    },

    # -------------------------------------------------
    # CONFIGURACIÓN
    # -------------------------------------------------

    {
        "section": "Configuración",

        "label": "Usuarios",

        "icon": "group",

        "route": Routes.USUARIOS,

        "roles": [
            Permissions.ADMIN
        ]
    },

    {
        "section": "Configuración",

        "label": "Contratos",

        "icon": "description",

        "route": Routes.CONTRATOS,

        "roles": [
            Permissions.ADMIN
        ]
    },

    {
        "section": "Configuración",

        "label": "Entidades - Contratos",

        "icon": "hub",

        "route": Routes.ENTIDADES_CONTRATOS,

        "roles": [
            Permissions.ADMIN
        ]
    },

    {
        "section": "Configuración",

        "label": "Contratos - Estudios",

        "icon": "account_tree",

        "route": Routes.ENTIDADES_CONTRATOS_ESTUDIOS,

        "roles": [
            Permissions.ADMIN
        ]
    },

    {
        "section": "Configuración",

        "label": "Estudios - Salas",

        "icon": "lan",

        "route": Routes.ESTUDIOS_SALAS,

        "roles": [
            Permissions.ADMIN
        ]
    },

    # -------------------------------------------------
    # PREPARACIÓN
    # -------------------------------------------------

    {
        "section": "Preparación",

        "label": "Preparaciones",

        "icon": "medical_information",

        "route": Routes.PREPARACIONES,

        "roles": [
            Permissions.ADMIN
        ]
    },

    {
        "section": "Preparación",

        "label": "Listas",

        "icon": "format_list_bulleted",

        "route": Routes.LISTA_PREPARACIONES,

        "roles": [
            Permissions.ADMIN
        ]
    },

    {
        "section": "Preparación",

        "label": "Listas - Preparaciones",

        "icon": "link",

        "route": Routes.LISTA_PREPARACIONES_PREPARACIONES,

        "roles": [
            Permissions.ADMIN
        ]
    },

    # -------------------------------------------------
    # RECOMENDACIONES
    # -------------------------------------------------

    {
        "section": "Recomendaciones",

        "label": "Entidades",

        "icon": "tips_and_updates",

        "route": Routes.RECOMENDACIONES_ENTIDADES,

        "roles": [
            Permissions.ADMIN
        ]
    },

    {
        "section": "Recomendaciones",

        "label": "Estudios",

        "icon": "auto_awesome",

        "route": Routes.RECOMENDACIONES_ESTUDIOS,

        "roles": [
            Permissions.ADMIN
        ]
    },

    # -------------------------------------------------
    # BASE DE DATOS
    # -------------------------------------------------

    {
        "section": "Base de Datos",

        "label": "Backup",

        "icon": "backup",

        "route": Routes.BACKUP,

        "roles": [
            Permissions.ADMIN
        ]
    }
]
