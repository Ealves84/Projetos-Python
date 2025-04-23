# Desafio 7
# Crie uma versão melhorada da aula passada:

# Use try/except para garantir que a idade seja número

# Não deixe o campo de nome e cidade vazio

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
    try:
        nome = input(f"Digite o nome {count + 1}: ").strip()
        if nome == "":
           print("nome nao pode ser vazio!") 
           continue
        idade = int(input(f"Digite a idade {count + 1}: "))
        cidade = input(f"Digite a cidade {count + 1}: ").strip()
        if cidade == "":
           print("cidade nao pode ser vazio!")
           continue 
        cadastro = cadastrar_pessoa(nome, idade, cidade)
        lista_pessoas.append(cadastro)
        count += 1
    except ValueError:
        print("Digite apenas números!")

exibir_pessoas(lista_pessoas)
