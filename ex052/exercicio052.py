'''
leia um numero inteiro e diga se ele é ou não um numero primo
'''

num = int(input("Diga um numero"))
ePrimo = True
for i in range(2,num):
    if(num % i == 0):
        ePrimo = False
        break

if ePrimo:
    print(num, " é primo")
else:
    print("Não é primo")


