#Exercício 7

print("Digite os dados abaixo:")
nota_candidato = float(input("A sua nota:\n"))
nota_corte = float(input("A nota de corte:\n"))
nota_min_aprovacao = float(input("A nota mínima de aprovação:\n"))

print("Situação candidato:")

if nota_candidato >= nota_min_aprovacao:
    print("Aprovado")
elif nota_candidato >= nota_corte:
    print("Lista de Espera")
else:
    print("Reprovado")