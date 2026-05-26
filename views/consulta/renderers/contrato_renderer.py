from ..components.cards.contrato_card import build as build_contrato_card


def build_contrato_section(contrato):
    return [build_contrato_card(contrato)]
