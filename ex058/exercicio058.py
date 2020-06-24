'''
melhorar o desafio 28
o computador deve escolher um numero entre 0 e 10
só q agora o jogar vai tentar adivinhar até acertar.
tem q mostrar quantos palpites foram necessarios
'''
from random import randint
sorteado = randint(1,11)
entrada = int(input("Diga um numero ente 1 e 10"))
while sorteado != entrada:
    print("Voce errou")
    print("tente de novo")
    entrada = int(input("Diga um numero ente 1 e 10"))
print()
print()
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Voce acertou")
