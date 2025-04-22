# Desafio 5
# Monte um pequeno cadastro de pessoas, usando dicionário + lista:

# Peça o nome, idade e cidade de 3 pessoas

# Guarde cada pessoa como um dict dentro de uma list

# No final, exiba todos os cadastros

# exemplo da saida

# Cadastro:
# 1 - Maria | 28 anos | Recife
# 2 - João  | 32 anos | São Paulo
# ...
lista_nomes = []

count = 0
while count < 3:
    nome = input(f"Digite o nome {count + 1}: ")
    idade = input(f"Digite a idade {count + 1}: ")
    estado = input(f"Digite o estado {count + 1}: ")
    pessoa = {
     "nome": nome,
     "idade": idade,
     "cidade": estado}
    lista_nomes.append(pessoa)
    count += 1

print(lista_nomes)
print(pessoa)

for i, pessoa in enumerate(lista_nomes, 1):
    print(f"{i} - {pessoa['nome']} | {pessoa['idade']} anos | {pessoa['cidade']}")