# leia duas notas, calcule a media e dia se foi aprovado ou reprovado
n1 = float(input("Diga a 1 nota"))
n2 = float(input("Diga a 2 nota"))
n3 = float(input("Diga a 3 nota"))
media = (n1 + n2 + n3) /3
if(media >= 7):
    print("Voce passou")
else:
    print("Voce reprovou")