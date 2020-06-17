# escreva um programa q leia um numero inteiro qualquer e peça
# para o usuario escolher qual sera a base de conversao
# binario, octal, hexadecimal

num = int(input("diga um numero inteiro"))
print("1 - binario")
print("2 - octal")
print("3 - hexadecimal")

entrada = int(input("escolha sua conversao"))
if entrada == 1:
    numNovo = bin(num)
elif entrada == 2:
    numNovo = oct(num)
elif entrada== 3:
    numNovo = hex(num)
else:
    numNovo = None
    print("entrada inválica")
if numNovo != None:
    print(num, " : ", numNovo)

