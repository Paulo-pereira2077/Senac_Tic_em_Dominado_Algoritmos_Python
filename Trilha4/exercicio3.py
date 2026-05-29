#Exercício 3

projeto = input("Nome do projeto: ")
qtd = int(input("Quantidade de doações: "))
meta = float(input("Meta financeira: "))

doacoes = []
for _ in range(qtd):
    doacoes.append(float(input("Doação: ")))

print("\n>> Resumo das Doações <<")
print(f"Projeto: {projeto}")
print(f"Doações recebidas: {', '.join(map(str, doacoes))}")

total = sum(doacoes)
print(f"Total arrecadado: {total}")
print(f"Maior doação: {max(doacoes)}")

if total >= meta:
    print("Situação: Meta atingida")
else:
    print("Situação: Meta não atingida")