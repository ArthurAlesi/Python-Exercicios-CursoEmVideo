'''
leia um numero inteiro n
mostre na tela os n primeiros elementos de uma sequencia fibonaci
'''

qtd = int(input("Diga quantos termos voce quer "))
t1 = 0
t2 = 1
cont = 3
while cont <= qtd:
    t3 = t1 + t2
    print(t3, end = " ")
    t1 = t2
    t2 = t3
    cont +=1
