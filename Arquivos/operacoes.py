def soma(a: int, b: int) -> int:
    return a + b

def subtracao(a: int, b: int) -> int:
    return a - b

def multiplicacao(a: int, b: int) -> int:
    return a * b

def divisao(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("Erro: Divisão por zero!")
    return a / b