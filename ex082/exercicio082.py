'''
crie um programa que vai legar varios numeros e colocar em uma lista.
Depois disso crie duas listas e extras que vao conter apenas os
 valores pares e os valores impares digitados respectivamente.
 ao final mostre o conteudo das 3 listas geradas
'''
num = []
pares = []
impares = []
while True:
    num.append(int(input("Digite um numero: ")))
    continuar = str(input("Deseja continuar [S/N]"))
    if continuar in 'nN':
        break

for i, v in enumerate(num):
    if v% 2 ==0:
        pares.append(v)
    else:
        impares.append(v)

print(num)
print(pares)
print(impares)