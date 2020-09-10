'''
Faça um pprograma que leia 5 valoes numericos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor difitado e as suas respectrivas posiçoes na lista

'''
lista = []
for i in range(5):
    lista.append(int(input("Diga um valor")))

    if i == 0:
        maior  = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print(lista)
print("maior: ", maior, end=" ")
for i, v in enumerate(lista):
    if v == maior:
        print("na posicao", i + 1, end="")

print()

print("menor: ", menor, end=" ")
for i, v in enumerate(lista):
    if v == menor:
        print("na posicao",i + 1, end="")


