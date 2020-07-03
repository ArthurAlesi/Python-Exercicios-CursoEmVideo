'''
o jogador devera jogar par ou impar com a maquina
só pare se o jjogador perdeu
mostre o total de vitorias
'''

from random import randint
escolha = str(input("[P] Par ou [I]impar"))
vitoria  = 0
while True:
    jogador = int(input("diga um numero"))
    computador = randint(1,11)
    total = jogador + computador
    print()
    print("Voce escolheu: ", jogador)
    print("Computador escolheu: ",computador )
    print()
    if escolha in "pP" and total % 2 == 0:
        print("Voce ganhou")
        vitoria += 1
    elif escolha in "iI" and total % 2 != 0:
        print("Voce ganhou")
        vitoria += 1
    else:
        print("Voce perdeu")
        break

print("Voce teve %s vitoria(s)"% vitoria)