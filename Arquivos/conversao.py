def validar_numero(numero: str, base: int) -> bool:
    numero = numero.upper()
    if numero.startswith("-"):
        numero = numero[1:]  
    if base == 2:
        return all(d in "01" for d in numero)
    elif base == 8:
        return all(d in "01234567" for d in numero)
    elif base == 10:
        return numero.isdigit()
    elif base == 16:
        return all(d in "0123456789ABCDEF" for d in numero)
    return False

def converter_para_decimal(numero: str, base: int) -> int:
    if not validar_numero(numero, base):
        raise ValueError(f"O número '{numero}' contém dígitos inválidos para a base {base}.")
    return int(numero, base)

def decimal_para_binario(n: int) -> str:
    return bin(n)[2:]

def decimal_para_octal(n: int) -> str:
    return oct(n)[2:]

def decimal_para_hexadecimal(n: int) -> str:
    return hex(n)[2:].upper()