#Exercício 4

gramas = float(input("Digite a quantidade em gramas (g). Ex: 1kg = 1000g\n"))

if gramas <= 0:
    print("Peso inválido")
else:
    if gramas >= 1000:
        preco_por_100g = 3.00  
    else:
        preco_por_100g = 3.50  
        
    total = (gramas / 100) * preco_por_100g
    
    print(f"O total é R$ {total:.2f}")