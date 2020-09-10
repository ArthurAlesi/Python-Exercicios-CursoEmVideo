'''
Crie um programa onde o usuario possa digitar varios valores
numericos e cadastre-os em uma lista. Caso o numero ja exista la dentro,
 ele nao sera adicionado. no final, serao exibidos todos os valores
  unicos digitados em ordem crescente

'''

numero = list()
while True:
    n = int(input("Digite um valor"))
    if n not in numero:
        numero.append(n)
    else:
        print(" Valor dubplicado")
    r = str(input("DEseja continuar [s/n]"))
    if r in "nN":
        break