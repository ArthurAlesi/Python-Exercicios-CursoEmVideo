'''
Faça um programa q mostre a tabuada
de varios numeros 1 de cada vez e só pare  se o numero digitado for
negativo
'''
while True:
    num = int(input("Diga um numero [digite um negativo para sair]"))

    if num < 0:
        print()
        print("Voce saiu")
        break

    for i in range (1,11):
        print(num, " x ", i," = ", num*i)
    print()
    print()