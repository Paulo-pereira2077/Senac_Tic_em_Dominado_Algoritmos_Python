#Exercício 5

palavra = list(input("Palavra secreta: ").upper())
print("\n" * 50)  # Limpa o console empurrando o texto para cima
oculta = ["_"] * len(palavra)
erros = 0

while erros < 7 and "_" in oculta:
    print(f"\nEstado: {' '.join(oculta)}")
    print(f"Erros: {erros}")
    letra = input("Letra: ").upper()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                oculta[i] = letra
    else:
        erros += 1

if "_" not in oculta:
    print(f"\nEstado: {' '.join(oculta)}\nErros: {erros}")
    print("Parabéns! Você descobriu a palavra.")
else:
    print(f"\nEstado: {' '.join(oculta)}\nErros: {erros}")
    print(f"Você perdeu! A palavra era: {''.join(palavra)}")