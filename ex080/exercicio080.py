'''
Crie um programa onde o usuario possa difitar cinco valores numericos e cadastre-os em
uma lista, já na posicao correta de insercao(sem usar o sort(), no final mostre
a lista ordenada na tela.
'''
lista = []
for i in range(0,5):
    n = int(input('digite um valor'))
    if i ==0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1



print(lista)