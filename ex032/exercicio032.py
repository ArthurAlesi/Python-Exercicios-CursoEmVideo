# Faça um programa que leia um ano qualquer
# e mostre se ele é bissexo

ano = int(input("diga o ano"))

if (ano % 4 ==0) and (ano%100!=0):
    print(ano,  " é bissexto")
else:
    print(ano, " não Bissexto")