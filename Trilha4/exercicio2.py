#Exercício 2
qtd = int(input("Quantidade de meses: "))
faturamento = []
for _ in range(qtd):
    faturamento.append(float(input("Faturamento: ")))

print("\n>> Análise de Faturamento <<")
print(f"Faturamento informado: {', '.join(map(str, faturamento))}")

crescimento = all(faturamento[i] >= faturamento[i-1] for i in range(1, len(faturamento)))
queda = all(faturamento[i] <= faturamento[i-1] for i in range(1, len(faturamento)))
constante = all(f == faturamento[0] for f in faturamento)

if constante:
    situacao = "Constante"
elif crescimento:
    situacao = "Crescimento"
elif queda:
    situacao = "Queda"
else:
    situacao = "Sem padrão"

print(f"Situação: {situacao}")
