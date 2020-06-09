# Sorteia 4 alunos e mostre o nome do sorteado
import random
aluno1 = input("Diga o nome do primeiro aluno")
aluno2 = input("Diga o nome do segundo aluno")
aluno3 = input("Diga o nome do terceiro aluno")
aluno4 = input("Diga o nome do quarto aluno")
lista = [aluno1,aluno2,aluno3,aluno4]
escolha = random.choice(lista)
print("O escolhido foi")
print(escolha)