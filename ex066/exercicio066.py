'''
leia varios numeros inteiros pelo teclado
o programa vai  parar quando diginar 999
mostre quantos numeros foram digitados


'''
soma = 0
cont = 0
while True:
    num = int(input("Diga um numero [999 para parar]"))
    if num == 999:
        break
    soma += num
    cont += 1

print(cont, " numeros")
print("A soma foi ", soma)