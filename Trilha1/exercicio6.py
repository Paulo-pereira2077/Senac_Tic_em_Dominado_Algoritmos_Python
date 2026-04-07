#Exercício 6

nome = input("Digite o nome: ")
altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

# Calculando o IMC
imc = peso / (altura ** 2)

print(f"{nome}, seu IMC é de {imc:.4f}")