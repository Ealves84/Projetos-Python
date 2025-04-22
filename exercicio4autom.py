# Peça para o usuário digitar 5 nomes e salve numa lista

# Depois, use o for para imprimir todos os nomes, um por um

# Digite o nome 1: Ana
# Digite o nome 2: João
# ...

# Resultado:
# - Ana
# - João
# - ...

## obter entrada para tabela através de ocorrencias com for:
tabela_nomes = []

##for i in range(5):
##    nome = input(f"Digite o nome {i + 1}: ")
##    tabela_nomes.append(nome)

## obter entrada para tabela através de ocorrencias com while:

count = 0

while count < 5:
    nome = input(f"Digite o nome {count + 1}: ")
    tabela_nomes.append(nome)
    count += 1

print("Resultado com for")
for resultado in tabela_nomes:
    print(f"Olá, {resultado}!")

#########################################
##Exemplo com While + Count
print("")
print("Resultado com While")

count = 0

while count <= 4:
     print(f"Olá, {tabela_nomes[count]}!")
     count += 1