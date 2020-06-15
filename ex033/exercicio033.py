# Faça um programa que leia 3 numeros
#  e mostre qual o maior e qual o menor

num1 = int(input("Diga um numero"))
num2 = int(input("Diga um numero"))
num3 = int(input("Diga um numero"))

menor = maior = num1

# menor _______________________________________________
if(num2 < num1) and (num2 < num3):
    menor = num2
if(num3 < num1) and (num3 <num2):
    menor = num3

# maior _______________________________________________
if( num2 > num1) and (num2 > num3):
    maior = num2
if (num3 > num1) and (num3 > num2):
    maior = num3

print("Maior: ", maior)
print("Menor: ", menor)