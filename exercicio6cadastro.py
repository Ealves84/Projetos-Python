# Crie um sistema de cadastro com **funções**:

# 1. Uma função chamada `cadastrar_pessoa()` que:
#     - Pede nome, idade e cidade
#     - Retorna um dicionário com os dados
# 2. Uma função chamada `mostrar_pessoas(lista)` que:
#     - Recebe uma lista de pessoas (dicionários)
#     - Exibe as informações formatadas
# 3. Um `while` para cadastrar várias pessoas (3 vezes, por exemplo)



## Etapa de cadastro 

## FUNCÃO CADASTRO
def cadastrar_pessoa(nome, idade, cidade):
    dic_cadastro = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade}
    return dic_cadastro

## FUNCÃO EXIBIR
def exibir_pessoas(lista):
    for i, cadastro in enumerate(lista, 1):
         print(f"Cadastro Numero,  {i}")
         print(f"{cadastro['nome']} | {cadastro['idade']} anos | {cadastro['cidade']}")

lista_pessoas = []

count = 0
while count < 3:
    nome = input(f"Digite o nome {count + 1}: ")
    idade = input(f"Digite a idade {count + 1}: ")
    cidade = input(f"Digite a cidade {count + 1}: ")
    cadastro = cadastrar_pessoa(nome, idade, cidade)
    lista_pessoas.append(cadastro)
    count += 1

exibir_pessoas(lista_pessoas)







