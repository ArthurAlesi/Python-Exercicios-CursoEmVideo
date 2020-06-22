'''
 Faça um programa que mostre na tela uma ocntagem regressiva para o esoturo
 de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo
'''
from time import sleep

for i in range(10,-1,-1):
    if(i==0):
        print("BOOM")
    else:
        print(i)
        sleep(1)

