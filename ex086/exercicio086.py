'''
Crie um programa que crie uma matriz de dimensao 3x3 e preencha
com valores lidos pelo teclado
no final mostre a matriz na tela com a formatacao correta
'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("diga um valor"))
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]}]", end = "")
    print()