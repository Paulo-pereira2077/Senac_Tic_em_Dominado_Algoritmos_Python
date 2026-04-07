#Exercício 2

cor = input("Digite a cor do semáforo para a ação do pedestre correspondente (Vermelho, Amarelo ou Verde): ")

if cor == "Vermelho":
    print("Espere")
elif cor == "Verde":
    print("Atravesse")
else:
    print("Farol inoperante")