##idade = int(input("Qual a sua idade? "))  # converte para inteiro
##altura = float(input("Qual a sua altura (em metros)? "))  # para número decimal


##Codigo de exemplo
##nome = input("Qual o seu nome? ")
##idade = int(input("Qual a sua idade? "))
##ano_atual = 2025
##ano_nascimento = ano_atual - idade

##print(f"{nome}, você nasceu em {ano_nascimento}.")

##print(type(idade))  # Mostra: <class 'int'>

##Segundo exercicio
##Crie um programa que:

##Pergunta o nome, ano de nascimento e altura
##Calcula a idade da pessoa
##Mostra a seguinte mensagem:
##João, você tem 32 anos e mede 1.75m de altura.


nome = input("Qual seu nome? ")
idade = int(input("Qual ano você nasceu? "))
altura = input("Qual sua altura? ")
altura = float(altura.replace(",", "."))

ano_atual = 2025

ano_nascimento = ano_atual - idade

print(f"Ola {nome}, você tem {ano_nascimento} anos e mede {altura} de altura.")

