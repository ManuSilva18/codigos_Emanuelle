# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# Dados do produto
produto = "FIAT TORO"
preco = 200000
desconto_percentual = 15

# Cálculo do desconto
valor_desconto = preco * (desconto_percentual / 100)
preco_final = preco - valor_desconto

# Exibição dos resultados
print(f"Produto: {produto}")
print(f"Preço: {preco}")
print(f"Porcentagem de desconto: {desconto_percentual}")
print(f"O {produto} com {desconto_percentual:.1f}% de desconto custará R$ {preco_final:.1f}")

