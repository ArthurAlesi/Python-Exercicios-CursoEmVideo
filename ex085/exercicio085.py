'''
Crie um programa onde o usuario possa digitar sete valores numericos e dacastre-os em
uma lista unica que mantenha separados os valores pares e impares. No final, mnostre
os valores pares e imapres em ordem crescente
'''

num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f"Digite o  {c}valor:"))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)



num[0].sort()
num[1].sort()
print(num[0])
print(num[1])