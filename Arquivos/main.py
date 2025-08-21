from conversao import *
from operacoes import *

def menu():
    while True:
        print("\n===== CALCULADORA DE BASES =====")
        print("1 - Converter número")
        print("2 - Operações entre números")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Digite o número: ").upper()
            base = int(input("Base do número (2-Binário, 8-Octal, 10-Decimal, 16-Hexadecimal): "))

            try:
                decimal = converter_para_decimal(numero, base)
                print(f"\nDecimal: {decimal}")
                print(f"Binário: {decimal_para_binario(decimal)}")
                print(f"Octal: {decimal_para_octal(decimal)}")
                print(f"Hexadecimal: {decimal_para_hexadecimal(decimal)}")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            num1 = input("Digite o primeiro número: ").upper()
            base1 = int(input("Base do primeiro número (2/8/10/16): "))
            num2 = input("Digite o segundo número: ").upper()
            base2 = int(input("Base do segundo número (2/8/10/16): "))

            try:
                n1 = converter_para_decimal(num1, base1)
                n2 = converter_para_decimal(num2, base2)

                print("\nResultados em decimal:")
                print(f"Soma: {soma(n1, n2)}")
                print(f"Subtração: {subtracao(n1, n2)}")
                print(f"Multiplicação: {multiplicacao(n1, n2)}")
                print(f"Divisão: {divisao(n1, n2)}")
            except ValueError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


menu()