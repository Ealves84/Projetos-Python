lista_pessoas = []

count = 0
while count < 3:
    nome = input(f"Digite o nome {count + 1}: ")
    idade = input(f"Digite a idade {count + 1}: ")
    cidade = input(f"Digite a cidade {count + 1}: ")

    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    lista_pessoas.append(pessoa)
    count += 1
print(pessoa)
print("\n📋 Cadastro Final:")
for i, pessoa in enumerate(lista_pessoas, 1):
    print(f"{i} - {pessoa['nome']} | {pessoa['idade']} anos | {pessoa['cidade']}")