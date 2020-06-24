'''
Crie um programa q leia 2 valores e mostre 1 menu como ao lado na tela
seu programa  deverá realizar a operação solicidade em casa caso
[1] somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa
'''
n1 = float(input("Diga o primeiro valor"))
n2 = float(input("Diga o segundo valor"))
menu = 0
resultado = None
while menu != 5:
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos numeros")
    print("[5] sair do programa")
    menu = int(input())


    if menu == 1:
        resultado = n1 + n2
        print(n1," + ", n2, " = ", resultado)

    elif menu == 2:
        resultado = n1 * n2
        print(n1, " x ", n2, " = ", resultado)

    elif menu == 3:
        if n1> n2:
            resultado = n1
        elif n1 == n2:
            resultado = " são iguais"
        else:
            resultado = n2
        print(" O maior é ", resultado)

    elif menu == 4:
        print("Diga novos numeros")
        n1 = float(input("Diga o primeiro valor"))
        n2 = float(input("Diga o segundo valor"))
        continue


    elif menu == 5:
        print()
        print("Voce escolheu sair")
        print()

    else:
        print(" entrada inválida")
        print("tente novamente")
        print()