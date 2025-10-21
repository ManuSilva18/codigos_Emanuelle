# Escreva um programa que pede que o usuário informe uma senha.
# O código deve comparar a senha informada pelo usuário com uma senha pré-definida no código armazenada em uma variável 
# Depois o código deve informar se a senha é correta ou incorreta.

# OUTPUT ESPERADO
# Exemplo 1:

# Digite a senha: 123123
# Senha incorreta

# Exemplo 2:

# Digite a senha: AC12
# Senha correta

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# Define a senha correta
# Exemplo 1

senha_correta = "AC12"

# Solicita que o usuário digite a senha
senha_digitada = input("Digite a senha: ")

# Compara a senha digitada com a senha correta
if senha_digitada == senha_correta:
    print("Senha correta")
else:
    print("Senha incorreta")

    senha_correta = "123123"

# Solicita que o usuário digite a senha
# Exemplo 2

senha_digitada = input("Digite a senha: ")

# Compara a senha digitada com a senha correta
if senha_digitada == senha_correta:
    print("Senha correta")
else:
    print("Senha incorreta")



