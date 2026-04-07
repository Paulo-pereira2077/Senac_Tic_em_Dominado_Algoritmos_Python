#Exercício 2
quantPessoas = int(input("Quantas pessoas vão participar do churrasco? "))

carne = quantPessoas * 0.300
frango = quantPessoas * 0.150
linguica = quantPessoas * 0.200

precoCarne = carne * 50.00
precoFrango = frango * 22.00
precoLinguica = linguica * 28.00
precoTotal = precoCarne + precoFrango + precoLinguica
precoPorPessoa = precoTotal / quantPessoas

print(f"Quantidades:\n Carne: {carne:.2f}kg - Frango: {frango:.2f}kg - Linguiça: {linguica:.2f}kg")
print(f"Custo total:\n Carne: R$ {precoCarne:.2f} - Frango: R$ {precoFrango:.2f} - Linguiça: R$ {precoLinguica:.2f}")
print(f"Custo total do churrasco: R$ {precoTotal:.2f}")
print(f"Cada pessoa deverá contribuir com R$ {precoPorPessoa:.2f}")
