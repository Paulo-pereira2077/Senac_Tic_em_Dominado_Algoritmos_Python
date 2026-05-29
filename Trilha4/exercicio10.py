#Exercício 10

qtd_a = int(input("Qtd figurinhas Jogador 1: "))
fig_a = []
for _ in range(qtd_a):
    fig_a.append(int(input()))

qtd_b = int(input("Qtd figurinhas Jogador 2: "))
fig_b = []
for _ in range(qtd_b):
    fig_b.append(int(input()))

# Removendo repetidas internas do próprio jogador e separando a lógica
comuns = sorted(list(set(f for f in fig_a if f in fig_b)))
apenas_a = sorted(list(set(f for f in fig_a if f not in fig_b)))
apenas_b = sorted(list(set(f for f in fig_b if f not in fig_a)))

print(f"\nFigurinhas em comum: {', '.join(map(str, comuns))}")
print(f"Apenas jogador 1: {', '.join(map(str, apenas_a))}")
print(f"Apenas jogador 2: {', '.join(map(str, apenas_b))}")

# A quantidade de trocas será baseada em quem tem menos figurinhas exclusivas para oferecer
trocas = min(len(apenas_a), len(apenas_b))
print(f"Quantidade de trocas possíveis: {trocas}")