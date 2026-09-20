"""Funções para manipulação de textos."""

def contar_palavras(texto: str) -> int:
    return len(texto.split())

def inverter_texto(texto: str) -> str:
    return texto[::-1]
