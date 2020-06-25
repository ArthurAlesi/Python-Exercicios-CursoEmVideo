'''
crie um programa q leia varios numeriso inteiros
só para quando o uusuario digitar 999
mostre quantos numeros ele digitou e a soma de todos

'''
soma = 0
qtdNum = 0
num = int(input("Diga um numero"))
while num != 999:
    soma += num
    qtdNum +=1
    num = int(input("Diga um numero"))

print()
print("Voce digiou ", qtdNum, " numeros")
print("A soma de todos eles é ", soma)