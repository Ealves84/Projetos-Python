# usar condição para avaliar
# exercicio 3
# Pergunta a idade da pessoa

# Informa:

# Se ela é menor de idade (<18)
# Se é maior de idade (18 a 64)
# Se é idosa (65 ou mais)

nome = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))

if idade < 18:
    print (f"{nome}, Você é menor de idade")
elif idade <= 64:
    print (f"{nome}, Você é maior de idade")
else:
    print (f"{nome}, Você é uma pessoa na melhor idade")

   