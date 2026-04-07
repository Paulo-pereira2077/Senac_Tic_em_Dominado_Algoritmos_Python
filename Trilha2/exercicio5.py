#Exercício 5

# Lê as três notas e a quantidade de faltas
nota1 = float(input("Digite sua nota 1:\n"))
nota2 = float(input("Digite sua nota 2:\n"))
nota3 = float(input("Digite sua nota 3:\n"))
faltas = int(input("Digite sua quantidade de faltas:\n"))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

if media < 0 or media > 10 or faltas < 0:
    print("Parâmetros inválidos")
else:
    print(f"Média: {media:.1f}.")
    
    if faltas > 4:
        print("Situação: Reprovado por Falta")
    elif media == 0:
        print("Situação: Desistente")
    elif media < 6.0:
        print("Situação: Recuperação")
    elif media < 8.0: 
        print("Situação: Aprovado")
    else: 
        print("Situação: Aprovado com sucesso")