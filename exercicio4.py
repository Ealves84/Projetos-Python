# Peça para o usuário digitar 5 nomes e salve numa lista

# Depois, use o for para imprimir todos os nomes, um por um

# Digite o nome 1: Ana
# Digite o nome 2: João
# ...

# Resultado:
# - Ana
# - João
# - ...

nome1 = input("Digite o Nome 1: ")
nome2 = input("Digite o Nome 2: ")
nome3 = input("Digite o Nome 3: ")
nome4 = input("Digite o Nome 4: ")
nome5 = input("Digite o Nome 5: ")

tabela_nomes = [nome1, nome2, nome3, nome4, nome5]

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