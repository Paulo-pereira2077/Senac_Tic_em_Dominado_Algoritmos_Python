#Exercício 6

print("Digite abaixo duas cores primárias para mostar a combinação dessas cores:")
cor1 = input("Digite uma cor primária\n")
cor2 = input("Digite outra cor primária\n")

primarias = ["Vermelho", "Azul", "Amarelo"]

if cor1 not in primarias or cor2 not in primarias:
    print("Apenas cores primárias são aceitas.")

else:
    if (cor1 == "Vermelho" and cor2 == "Azul") or (cor1 == "Azul" and cor2 == "Vermelho"):
        resultado = "Roxo"
    elif (cor1 == "Vermelho" and cor2 == "Amarelo") or (cor1 == "Amarelo" and cor2 == "Vermelho"):
        resultado = "Laranja"
    elif (cor1 == "Azul" and cor2 == "Amarelo") or (cor1 == "Amarelo" and cor2 == "Azul"):
        resultado = "Verde"
    else:
        resultado = cor1
        
    print("A combinação resulta em:")
    print(resultado)