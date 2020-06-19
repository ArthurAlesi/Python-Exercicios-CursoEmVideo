# refaça o exercicio 35 mostrando qual o tipo do triangulo



l1 = float(input("Diga o primeiro lado"))
l2 = float(input("Diga o segundo lado"))
l3 = float(input("Diga o terceiro lado"))
if (l1 + l2 < l3) or (l1 + l3 < l2) or (l1 > l2 + l3):
    print("Não é triângulo")
else:
    print("É triângulo")
    if (l1==l2==l3):
        print("É equilatero")
    elif l1 != l2 != l3 != l1:
        print("Triangulo escaleno")
    else:
        print("Triângulo isósceles")

