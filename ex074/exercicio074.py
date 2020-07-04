'''
gera 5 numeros aleatorios e os coloque numa tbla
mostre a listagem de numero
indique o menor e maior da tupla
'''

from random import  randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print("todos os numeros sorteados: ",num)
print("maior: ", max(num))
print("menor: ",min(num))

