#Exercício 8

qtd_p = int(input("Quantidade de açaí Pequeno: "))
qtd_m = int(input("Quantidade de açaí Médio: "))
qtd_g = int(input("Quantidade de açaí Grande: "))
desconto_str = input("Porcentagem de desconto: ")

# Valores base
preco_p = 13.50
preco_m = 15.00
preco_g = 17.50

desconto = float(desconto_str)

# Calculando o total sem desconto
total_sem_desconto = (qtd_p * preco_p) + (qtd_m * preco_m) + (qtd_g * preco_g)

# Aplicando o desconto
total_com_desconto = total_sem_desconto - (total_sem_desconto * (desconto / 100))

print(f"Seu pedido foi registrado.\n- Açaí P: {qtd_p}\n- Açaí M: {qtd_m}\n- Açaí G: {qtd_g}")
print(f"Desconto de {desconto_str}% aplicado.")
print(f"Total R$ {total_com_desconto:.2f}")
