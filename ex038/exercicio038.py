# escreva um programa que leia dos numeros e compare-os
#  qual o maior ou se são iguais
n1 = int(input("diga um numero inteiros"))
n2 = int(input("diga um numero inteiro"))
maior = None
if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2
else:
    maior = "são iguais"

print("O numero maior é: ",maior)