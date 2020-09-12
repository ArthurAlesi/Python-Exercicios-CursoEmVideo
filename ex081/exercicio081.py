'''
crie um programa que leia varios numeros e coloqueos em uma lista
- diga quantos foram digitados
- a lista de valores ordenadas de forma decrescente
- se o valor 5 foi digitado e esta ou nao na lista
'''

lista = []
while True:
    num = int(input("diga um numero"))
    continuar = str(input("Quer continuar [S/N]" ))
    lista.append(num)
    if continuar in "nN":
        break

print("lista: ", lista)
lista.sort(reverse=True)
print("lista invertida: ", lista)
if 5 in lista:
    print("5 esta na lista")
else:
    print("5 nao esta na lista")