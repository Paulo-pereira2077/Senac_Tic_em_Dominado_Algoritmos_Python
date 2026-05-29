#Exercício 1
qtd = int(input("Quantidade de alunos: "))
notas = []
for _ in range(qtd):
    notas.append(float(input("Nota: ")))

print("\n>> Resultado da Turma <<")
print(f"Notas informadas: {', '.join(map(str, notas))}")

media = sum(notas) / qtd
print(f"Média da turma: {media:.1f}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")

aprovados = sum(1 for n in notas if n >= 6)
reprovados = qtd - aprovados
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")

if reprovados == 0:
    print("Situação geral: Todos os alunos foram aprovados")
else:
    print("Situação geral: Nem todos os alunos foram aprovados")