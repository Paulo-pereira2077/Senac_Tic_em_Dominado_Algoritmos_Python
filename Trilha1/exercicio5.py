#Exercício 5

nome = input("Digite seu nome: ")
valor_compra = float(input("Digite o valor da compra: "))
porcentagem_desconto = input("Digite o valor do desconto (%): ")
valor_porcentagem_desconto = float(porcentagem_desconto)

valor_desconto = valor_compra * (valor_porcentagem_desconto / 100)

# Subtrair o desconto do valor original
total_final = valor_compra - valor_desconto

print(f"Olá {nome}, sua compra de R$ {valor_compra:.2f} foi confirmada!")
print(f"Foi aplicado um desconto de {porcentagem_desconto}%.")
print(f"O total final ficou em R$ {total_final:.2f}")