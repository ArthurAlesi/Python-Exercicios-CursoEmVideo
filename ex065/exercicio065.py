'''
leia varios numeros inteiros pelo teclado
no final mostre a soma entre todos
o maior e o menor
o programa deve perguntar se el quer continuar ou nao a digitar válores

'''

num = int(input("Diga um numero"))
soma = num
maior = menor = num
continuar = str(input("Deseja continuar? [s] sim [n] não"))
while (continuar == 's'):
    num = int(input("Diga um numero"))
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = str(input("Deseja continuar? [s] sim [n] não"))

print("O maior foi ", maior)
print("O menor foi ", menor)
print("A soma é ", soma)