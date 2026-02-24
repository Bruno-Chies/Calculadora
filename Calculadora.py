import msvcrt
import pyttsx3
números = {"0": "zero", "1": "um", "2": "dois", "3": "três", "4": "quatro", "5": "cinco", "6": "seis", "7": "sete", "8": "oito", "9": "nove"}
print("Olá, tudo bem? ")
while True:
    valor_01 = input("Digite um valor(precione 'X' para encerrar): ").upper()
    if valor_01 == "X":
        print("Encerrando o programa...")
        print("Programa finalizado!")
        break
    valor_01 = float(valor_01)
    valor_02 = input("Digite outro valor(precione 'X' para encerrar): ").upper()
    if valor_02 == "X":
        print("Encerrando o programa...")
        print("Programa finalizado!")
        break
    valor_02 = float(valor_02)
    if valor_01 != "X" and valor_02 != "X":
        print("1 - Soma;\n2 - Subtração;\n3 - Multiplicação;\n4 - Divisão")
        operação = input("Escolha uma operação: ")
        if operação == "1":
            resultado = (valor_01) + (valor_02)
            print(f"O resultado da soma entre {valor_01} e {valor_02} é: {resultado}")
        elif operação == "2":
            resultado = (valor_01) - (valor_02)
            print(f"O resultado da subtração entre {valor_01} e {valor_02} é: {resultado}")
        elif operação == "3":
            resultado = (valor_01) * (valor_02)
            print(f"O resultado da multiplicação entre {valor_01} e {valor_02} é: {resultado}")
        elif operação == "4":
            if valor_02 != 0:
                resultado = (valor_01) / (valor_02)
                print(f"O resultado da divisão entre {valor_01} e {valor_02} é: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida!")
        else:
            print("Operação inválida! Tente novamente.")
        retorno = input("Deseja realizar outra operação? (S/N): ").upper()
        if retorno == "N":
            print("Encerrando o programa...")
            print("Programa finalizado!")
            break
        if retorno == "S":
            continue