#Exercício 7

nome = input("Digite o nome da pessoa: ")
livro = input("Digite o nome do livro: ")
paginas = int(input("Total de páginas: "))
segundos = int(input("Tempo em segundos de leitura por página: "))

tempo_total_segundos = paginas * segundos

horas = tempo_total_segundos / 3600

print(f"{nome}, você finalizará a leitura do livro {livro} \nem aproximadamente {horas:.2f} horas.")