"""Minha Biblioteca Python - funções simples para estudos e automação."""

from .calculos import soma, subtracao, multiplicacao, media
from .texto import contar_palavras, inverter_texto
from .utilidades import eh_par

__version__ = "0.1.0"

__all__ = [
    "soma",
    "subtracao",
    "multiplicacao",
    "media",
    "contar_palavras",
    "inverter_texto",
    "eh_par",
]
