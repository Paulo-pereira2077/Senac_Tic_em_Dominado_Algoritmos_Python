#Exercício 10

meta = input("Digite a descrição da sua meta: ")
valor = float(input("Digite o valor da meta: "))
salario = float(input("Digite o seu salário: "))
despesas = float(input("Digite o valor das suas despesas mensais: "))

#Saldo após despesas
saldoPosDespesas = salario - despesas

if saldoPosDespesas > 0:
    # A reserva fixa é exatamente 30% do que sobrou
    reservaFixa = saldoPosDespesas * 0.30

    # O valor disponível para a meta após retirar a reserva fixa 
    valorDisponivelMeta = saldoPosDespesas - reservaFixa

    # Tempo para cumprir a meta
    tempo = valor / valorDisponivelMeta

    print()
    print(f"Meta: {meta} (R$ {valor:.2f})")
    print(f"Salário: R$ {salario:.2f} - Despesas: R$ {despesas:.2f}")
    print(f"Saldo após despesas: R$ {saldoPosDespesas:.2f}")
    print(f"Reserva fixa (30%): R$ {reservaFixa:.2f}")
    print(f"Valor disponível para a meta: R$ {valorDisponivelMeta:.2f} por mês")
    print(f"Prazo estimado para atingir a meta: {tempo:.2f} meses")
else:
    print("\nAs despesas superam ou são iguais ao salário. Não é possível poupar.")