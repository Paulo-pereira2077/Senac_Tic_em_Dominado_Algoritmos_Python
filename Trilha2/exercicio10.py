#Exercício 10

print("---- Cinema ----")
qtd_inteiras = int(input("Digite a quantidade de entradas inteiras:\n"))
qtd_meias = int(input("Digite a quantidade de entradas meias:\n"))
dia_semana = input("Digite o dia da semana:\n")
nacional = input("Digite se é filema nacional (Sim ou Não):\n")

total_pessoas = qtd_inteiras + qtd_meias

if nacional == "Sim":
    total = total_pessoas * 5.00
elif dia_semana == "Quarta-feira":
    total = total_pessoas * 14.50
else:
    total = (qtd_inteiras * 28.50) + (qtd_meias * (28.50 / 2))

print("Total à pagar:")
print(f"R$ {total:.2f}")