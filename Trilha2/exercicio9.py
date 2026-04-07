#Exercício 9

print("Calculando o valor da mensalidade de acordo com seu curso.")

sigla_curso = input("Digite a sigla do seu curso (SI - Sistemas de Informação, \
                    ADS - Análise e Desenvolvimento de Sistemas, CS - Ciência da computação, \
                    EC - Engenharia da Computação ou ES - Engenharia de Software):\n")
isento = input()
desconto = float(input())

tabela_cursos = {
    "SI": 900.00,
    "ADS": 750.00,
    "CS": 1150.00,
    "EC": 1300.00,
    "ES": 950.00
}

if sigla_curso not in tabela_cursos:
    print("Curso não encontrado")
else:
    print("Valor da mensalidade:")
    
    if isento == "Sim":
        print("$ 0.00") 
    else:
        valor_base = tabela_cursos[sigla_curso]
        
        valor_desconto = valor_base * (desconto / 100)
        valor_final = valor_base - valor_desconto
        
        print(f"R$ {valor_final:.2f}")