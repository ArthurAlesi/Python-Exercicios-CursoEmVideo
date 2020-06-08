# Faça um produto que leia o preço de um produto
# e mostre o seu preço com 5% de desconto

preco = float(input("Diga o preço do produto"))
desconto = 0.95
precoNovo = preco * desconto
print("O preco antigo era R$%.2f"% preco)
print("O preço novo é R$%.2f"% precoNovo)