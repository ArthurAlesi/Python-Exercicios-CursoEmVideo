'''
simule um caixa eletronico
pergunte o valor a ser sacado em inteiro
informar quantas cedulas de cada valor serao entregues
considerando possuir celdulas de 50 20 10 e 1
'''

valor = int(input("Diga quanto você quer sacar"))
total = valor
ced = 50
totalCed  = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed >0:
            print("Total de %s cédulas de %d"% (totalCed, ced))
        if ced ==50:
            ced =20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print()
print("fim")