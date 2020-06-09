#leia os 4 alunos sorteados e mostre a ordem


import random
aluno1 = input("Diga o nome do primeiro aluno")
aluno2 = input("Diga o nome do segundo aluno")
aluno3 = input("Diga o nome do terceiro aluno")
aluno4 = input("Diga o nome do quarto aluno")
lista = [aluno1,aluno2,aluno3,aluno4]
# escolha = random.choice(lista)
# shuffle embaralha uma lista:
random.shuffle(lista)
print("A ordem foi:")
print(lista)