# faça o programa jogar pedra papel ou tesoura
from random import randint
cpu = randint(0,2)
opcoes  = ["Pedra","papel", "tesoura"]
cpuMao = opcoes[cpu]
print("1 - Pedra")
print("2 - papel")
print("3 - tesouza")
player = int(input("Escolha uma opcao")) - 1
playerMao = opcoes[player]

if cpu == 0:
    if player == 0:
        print("Deu empate")
        print(playerMao, " nao ganha de ", cpuMao)
    elif player ==1:
        print("voce ganhou")
        print(playerMao,"ganha de ",cpuMao )
    elif player ==2:
        print("Voce perdeu")
        print(playerMao, " nao ganha de ", cpuMao)
elif cpu ==1:
    if player == 0:
        print("Voce perdeu")
        print(playerMao, " nao ganha de ", cpuMao)
    elif player ==1:
        print("Deu empate")
        print(playerMao, " nao ganha de ", cpuMao)
    elif player ==2:
        print("Voce ganhou")
        print(playerMao, "ganha de ", cpuMao)
elif cpu == 2:
    if player == 0:
        print("Voce ganhou")
        print(playerMao, "ganha de ", cpuMao)
    elif player ==1:
        print("Deu empate")
        print(playerMao," nao ganha de ",cpuMao)
    elif player ==2:
        print("voce perdeu")
        print(playerMao, " nao ganha de ", cpuMao)

print(cpu)