"""Conversão de bases numéricas implementada do zero.

Não usa bin(), hex(), oct(), int(texto, base), format() nem bibliotecas
de conversão. Só aritmética (multiplicação, divisão e resto).
"""

DIGITOS = "0123456789ABCDEF"
BASES = {"decimal": 10, "binario": 2, "hexadecimal": 16, "octal": 8}
NOMES = {"decimal": "Decimal", "binario": "Binário",
         "hexadecimal": "Hexadecimal", "octal": "Octal"}


def para_decimal(texto, base):
    """Texto na base informada -> inteiro decimal (método posicional)."""
    texto = texto.strip().upper()
    if not texto:
        raise ValueError("Digite um número.")
    valor = 0
    for caractere in texto:
        posicao = DIGITOS.find(caractere)
        if posicao == -1 or posicao >= base:
            raise ValueError(f"'{caractere}' não é um dígito válido nessa base.")
        valor = valor * base + posicao
    return valor


def de_decimal(numero, base):
    """Inteiro decimal -> texto na base informada (divisões sucessivas)."""
    if numero == 0:
        return "0"
    resultado = ""
    while numero > 0:
        resultado = DIGITOS[numero % base] + resultado
        numero //= base
    return resultado


def converter(texto, origem, destino):
    """Converte `texto` da base `origem` para `destino` (nomes em BASES)."""
    if origem not in BASES or destino not in BASES:
        raise ValueError("Base desconhecida.")
    return de_decimal(para_decimal(texto, BASES[origem]), BASES[destino])
