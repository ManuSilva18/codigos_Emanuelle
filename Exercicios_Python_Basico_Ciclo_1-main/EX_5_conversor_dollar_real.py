# Escreva um programa que pede ao usuário o valor atual da cotação do dollar e a quantidade de dólares para ser convertido em reais. 
# Depois mostre na tela a conversão.

# OUTPUT ESPERADO:

# Digite a cotação do dollar: 5.60
# Digite o valor em dollar a ser convetido para real: 100
# O valor em reais é:  560.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# Solicita ao usuário a cotação do dólar
cotacao = float(input("Digite a cotação do dólar: "))

# Solicita ao usuário o valor em dólares
valor_dolar = float(input("Digite o valor em dólar a ser convertido para real: "))

# Calcula o valor em reais
valor_real = cotacao * valor_dolar

# Exibe o resultado
print("O valor em reais é:", valor_real)


