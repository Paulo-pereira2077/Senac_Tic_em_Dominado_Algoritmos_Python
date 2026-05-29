#Exercício 4

qtd = int(input("Quantidade de medicamentos: "))
farmacia_a = []
farmacia_b = []

print("Preços na Farmácia A:")
for _ in range(qtd):
    farmacia_a.append(float(input()))

print("Preços na Farmácia B:")
for _ in range(qtd):
    farmacia_b.append(float(input()))

print("\n>> FARMAZOOM <<")
print(f"Farmácia A: {', '.join(map(str, farmacia_a))}")
print(f"Farmácia B: {', '.join(map(str, farmacia_b))}")

barato_a = barato_b = empate = 0
for a, b in zip(farmacia_a, farmacia_b):
    if a < b:
        barato_a += 1
    elif b < a:
        barato_b += 1
    else:
        empate += 1

print("\n>> Produtos mais Baratos <<")
print(f"Na Farmácia A: {barato_a}")
print(f"Na Farmácia B: {barato_b}")
print(f"Mesmo preço: {empate}")

total_a = sum(farmacia_a)
total_b = sum(farmacia_b)

print("\nTotal")
print(f"Farmácia A: R$ {total_a:.2f}")
print(f"Farmácia B: R$ {total_b:.2f}")

print("\nMelhor opção")
if total_a < total_b:
    print("Farmácia A")
elif total_b < total_a:
    print("Farmácia B")
else:
    print("Empate")