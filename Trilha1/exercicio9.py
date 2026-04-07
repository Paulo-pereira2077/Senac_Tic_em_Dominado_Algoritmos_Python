#Exercício 9

tamanho_pista = int(input("Tamanho da pista em metros: "))
quantidade_voltas = int(input("Quantidade de voltas: "))
tempo_primeira_volta = float(input("Tempo da primeira volta em segundos: "))

# Calculando a distância total em metros e convertendo para quilômetros
distancia_total_m = tamanho_pista * quantidade_voltas
distancia_total_km = distancia_total_m / 1000

# Mantendo o tempo de volta, calcula o tempo total em segundos e converte para minutos
tempo_total_segundos = tempo_primeira_volta * quantidade_voltas
tempo_total_minutos = tempo_total_segundos / 60

print("Análise Preditiva Concluída-")
print(f"Distância total a ser percorrida: {distancia_total_km} km.")
print(f"Previsão de conclusão: {tempo_total_minutos} minutos.")