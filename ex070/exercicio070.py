'''
leia o nome e preco de varios produtos
pergunte se vai continuar
mostre o total gasto na compra
quantos produtos custam mais de 1000
qual o nome do produto mais barato
'''

total = totMil = menor = cont = 0

maisBarato = ""
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preco em reais: "))
    cont += 1
    total += preco
    if preco > 1000:
        totMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        maisBarato = produto
    else:
        if preco < menor:
            menor = preco
    resp = " "
    while resp not in "sSnN":
        resp = str(input("Deseja continuar? [s]sim [n]nao "))
    if resp in "nN":
        break
print()
print("Total: ", total)
print(totMil," produtos com mais de 1000 reais")
print("O mais barato custa ", menor," e é um ", maisBarato)