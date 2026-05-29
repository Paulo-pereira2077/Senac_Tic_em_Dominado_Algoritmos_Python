#Exercício 6

dias = int(input("Quantidade de dias: "))
pesos = []

for _ in range(dias):
    pesos.append(int(input("Peso: ")))

print(f"\nPesos informados: {', '.join(map(str, pesos))}")

maior_peso = max(pesos)
dia_maior = pesos.index(maior_peso) + 1
menor_peso = min(pesos)
dia_menor = pesos.index(menor_peso) + 1

print(f"Maior peso: {maior_peso} kg (Dia {dia_maior})")
print(f"Menor peso: {menor_peso} kg (Dia {dia_menor})")

print("\nGráfico de evolução:")
for i, peso in enumerate(pesos, start=1):
    # Calcula quantas barras imprimir (1 barra para cada 5kg)
    barras = "*" * (peso // 5)
    print(f"Dia {i} | {barras} {peso}")