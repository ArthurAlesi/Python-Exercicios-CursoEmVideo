# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra A
# Em que posição ela aparece a primeira vez
# Em que posição ela parece a ultima vez
qtdA = 0
posiPrimeiroA = None
posiUltimoA = None




frase = input("Leia a frase")
for i in range(len(frase)):
    if(frase[i].upper() == "A"):
        posiPrimeiroA = i
        break


for i in frase:
    if(i.upper() == "A"):
        qtdA += 1


for i in range(len(frase)):
    if (frase[i].upper() == "A"):
        posiUltimoA = i


print("quantidade de a's = ", qtdA)
print("A posição do primeiro a é ",posiPrimeiroA + 1)
print("A posição do ultimo a é ",posiUltimoA + 1)
