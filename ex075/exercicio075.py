'''
leia 4 valores e quarde-os em uma tupla
mostre:
quantas vezes apareceu o valor 9
qual posição do primeiro valor 3
quantos foram os numeros pares
'''

numeros = (int(input("Diga numero")),int(input("Diga numero")),
           int(input("Diga numero")),int(input("Diga numero")))

qtdPar = 0
posi3 = None
for i in numeros:
    if i % 2 == 0:
        qtdPar += 1

for i in numeros:
    if i == 3:
        posi3 = numeros.index(3) + 1
        break
    else:
        posi3 = "nao tem 3 nessa tupla"

print("quantidade de par ", qtdPar)
print("Posição do primeiro 3: ", posi3 )


