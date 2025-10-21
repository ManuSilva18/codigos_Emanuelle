# Escreva um código que pede ao usuário a altura e o peso e faça o cálculo do IMC (Índice de massa corporal) do usuário.
# Dica:
# Para calcular o IMC você deve dividir o peso pela altura ao quadrado
# imc = peso / (altura ** 2)


# OUTPUT ESPERADO:

# Digite sua altura: 1.78
# Digite seu peso: 85
# O seu IMC é: 26.83

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# Solicita a altura e o peso do usuário
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado com duas casas decimais
print(f"O seu IMC é: {imc:.2f}")

