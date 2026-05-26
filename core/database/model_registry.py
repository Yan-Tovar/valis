from database.models import *

MODEL_REGISTRY = {

    "estudios": Estudio,

    "salas": Sala,

    "estudios_salas": EstudioSala,

    "entidades": Entidad,

    "contratos": Contrato,

    "entidades_contratos": EntidadContrato,

    "entidades_contratos_estudios": EntidadContratoEstudio,

    "preparaciones": Preparacion,

    "lista_preparaciones": ListaPreparacion,

    "lista_preparaciones_preparaciones": ListaPreparacionPreparacion,

    "recomendaciones_estudio": RecomendacionEstudio,

    "recomendaciones_entidades": RecomendacionEntidad,

    "usuarios": Usuario
}