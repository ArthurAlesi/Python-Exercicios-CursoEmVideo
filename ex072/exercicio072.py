'''
crie um programa q tenha uma tupla totalemnte preenchida
com uma contagem por extenso de 0 a 20
o programa deverá ler um numero pelo teclado entre 0 e 20
mostralo por extenso
'''
listaExtenso = ("zero", "um", "dois" , "tres","quatro","cinco","seis",
        "sete","oito","nove","dez","onze","doze","treze","catorze"
        ,"quinze","dezesseis","dezessete","dezoito",
        "dezenove","vinte")
while True:
    num = int(input("Digite um numero entre 0 e 20 "))
    if (0 <= num <= 20):
        break
    else:
        print("tente novamente")

print("Voce escolheu ", listaExtenso[num])