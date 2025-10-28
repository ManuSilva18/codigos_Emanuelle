# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("| ---------- CADASTRO ---------- |")

nome = input("Digite o seu nome")
idade = float(input("Digite a sua idade"))
email = input("Digite o seu Email")
senha = float("Digite sua senha")

# Exibe os dados formatados

print(f"| Nome: {nome}")
print(f"| Idade: {idade}")
print(f"| Email: {email}")
print(f"| Senha: {senha}")

print("\n| ------------------------------ |")
print("| ----- USUÁRIO CADASTRADO ----- |")
print(f"| Seja bem vindo(a) {nome}!")
print(f"| Email: {email}")
print("| ------------------------------ |")
