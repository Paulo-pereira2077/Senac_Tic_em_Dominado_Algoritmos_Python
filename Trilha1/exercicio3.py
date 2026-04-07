#Exercício 3

nome = input("Digite o nome do(a) estudante:")
print()
print("Digite suas notas:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print(f"O(a) estudante {nome} ficou com média {media}")
