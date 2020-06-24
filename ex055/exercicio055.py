'''
leia o peso de 5 pessoas e diga qual foi o maior e o menor
'''
listaPeso = []
for i in range(5):
    listaPeso.append(int(input("Diga o peso da pessoa")))

maior = menor = listaPeso[0]
for i in range(len(listaPeso)):
    if listaPeso[i] > maior:
        maior = listaPeso[i]

    if listaPeso[i] < menor:
        menor = listaPeso[i]

print(menor)
print(maior)