"""Funções matemáticas básicas."""

def soma(a: float, b: float) -> float:
    return a + b

def subtracao(a: float, b: float) -> float:
    return a - b

def multiplicacao(a: float, b: float) -> float:
    return a * b

def media(*valores: float) -> float:
    if not valores:
        raise ValueError("Informe pelo menos um valor.")
    return sum(valores) / len(valores)
