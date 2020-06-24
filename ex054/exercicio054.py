'''
Crie um programa que leia o ano de nascimento de 7 pessoas. no final mostre
quantas pessoas ainda nao atingiram a maiooridade quantas ja são maioores
'''
qtdMaior = 0
for i in range(7):
    idade = int(input("Diga a idade"))
    if idade >= 18:
        qtdMaior += 1
qtdMenor = 7 - qtdMaior
print(qtdMaior," pessoas maiores de idade")
print(qtdMenor, " pesosas menors de idade")