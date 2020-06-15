# Desenvolva um programa que leia o comprimento de 3 reretas e diga se
# elas podem ou nao formar um triângulo

l1 = float(input("Diga o primeiro lado"))
l2 = float(input("Diga o segundo lado"))
l3 = float(input("Diga o terceiro lado"))
if (l1 + l2 < l3) or (l1 + l3 < l2) or (l1 > l2 + l3):

    print("Não é triângulo")
else:
    print("É triângulo")