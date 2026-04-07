#Exercício 8

print("---- Calculadora ----")
valor1 = float(input("Digite o primeiro valor:\n"))
valor2 = float(input("Digite o segundo valor:\n"))

operacao = input("Digite a operação (+, -, *, /, mod, ^):\n")

operacao_valida = True

if operacao == "1" or operacao == "Soma":
    resultado = valor1 + valor2
    simbolo = "+"
elif operacao == "2" or operacao == "Subtração":
    resultado = valor1 - valor2
    simbolo = "-"
elif operacao == "3" or operacao == "Multiplicação":
    resultado = valor1 * valor2
    simbolo = "*"
elif operacao == "4" or operacao == "Divisão":
    resultado = valor1 / valor2
    simbolo = "/"
elif operacao == "5" or operacao == "Resto":
    resultado = valor1 % valor2
    simbolo = "mod"
elif operacao == "6" or operacao == "Potência":
    resultado = valor1 ** valor2
    simbolo = "^"
else:
    operacao_valida = False

if operacao_valida:
    print(f"{valor1} {simbolo} {valor2} = {resultado}")
else:
    print("Operação não suportada")