from database.models import (

    Entidad,

    Contrato,

    Estudio,

    Sala,

    Usuario,

    EntidadContrato,

    Preparacion,

    ListaPreparacion
)


class RelationshipRegistry:


    RELATIONSHIPS = {

        # -------------------------------------------------
        # ENTIDAD CONTRATO
        # -------------------------------------------------

        "entidad_id": {

            "model": Entidad,

            "label_field": "nombre"
        },

        # -------------------------------------------------
        # ENTIDAD CONTRATO ESTUDIO
        # -------------------------------------------------

        "entidad_contrato_id": {

            "model": EntidadContrato,

            "label_field": "contrato.nombre"
        },

        # -------------------------------------------------
        # CONTRATO
        # -------------------------------------------------

        "contrato_id": {

            "model": Contrato,

            "label_field": "nombre"
        },

        # -------------------------------------------------
        # ESTUDIO
        # -------------------------------------------------

        "estudio_id": {

            "model": Estudio,

            "label_field": "nombre"
        },

        # -------------------------------------------------
        # SALA
        # -------------------------------------------------

        "sala_id": {

            "model": Sala,

            "label_field": "nombre"
        },


        # -------------------------------------------------
        # PREPARACION
        # -------------------------------------------------

        "preparacion_id": {

            "model": Preparacion,

            "label_field": "nombre"
        },

        # -------------------------------------------------
        # LISTA PREPARACION
        # -------------------------------------------------

        "lista_preparacion_id": {

            "model": ListaPreparacion,

            "label_field": "nombre"
        },

        # -------------------------------------------------
        # USUARIO
        # -------------------------------------------------

        "usuario_id": {

            "model": Usuario,

            "label_field": "nombre_completo"
        }
    }


    # -------------------------------------------------
    # GET RELATION
    # -------------------------------------------------

    @classmethod
    def get_relation(
        cls,
        model,
        field_name
    ):

        return cls.RELATIONSHIPS.get(
            field_name
        )