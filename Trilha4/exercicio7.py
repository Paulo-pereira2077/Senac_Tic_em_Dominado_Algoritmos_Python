#Exercício 7

transacoes = []

while len(transacoes) < 1000:
    valor = float(input("Transação (-1 para sair, 0 para cancelar): "))
    if valor == -1:
        break
    elif valor == 0:
        if transacoes:
            transacoes.pop() # Remove a última transação válida
    else:
        transacoes.append(valor)

saldo = sum(transacoes)
print(f"\nSaldo final: {saldo}")