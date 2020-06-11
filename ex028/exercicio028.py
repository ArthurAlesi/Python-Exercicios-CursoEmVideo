# escreva um programa que faça o computador "pensar em um numero
# inteiro entre 0 e 5 para o usuario tentar descobrir qual foi o
# o numero escolhido. Deve dizer se ganhou ou perdeu

from random import randint
from time import sleep
sorteado = randint(0,5)
entrada = int(input("Diga um numero ente 0 e 5"))
if entrada == sorteado:
    print("Você ganhou")
else:
    print("Voce perdeu")
    print("O numero sorteado foi ", sorteado)