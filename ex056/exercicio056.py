'''
leia nome idade e sexo de 4 pessoas
mostre a media da idade do grupo
qual o mais velho
quantas mulheres de menos de 20 anos
'''


qtdMulherMaiorDe20 = 0
idade = int(input("Diga a idade"))
sexo = str(input("Diga o sexo"))

if sexo in "fF" and idade >= 20:
    print("foi")
    qtdMulherMaiorDe20 +=1


maisVelho = 0
media = 0

for i in range(3):
    idade = int(input("Diga a idade"))
    sexo = str(input("Diga o sexo"))
    if idade > maisVelho and sexo in "mM":
        maisVelho = idade
    media += idade
    if sexo in "fF" and idade >= 20:
        print("foi")
        qtdMulherMaiorDe20

media /= 4

print("A media foi ", media)
print("Tem ",qtdMulherMaiorDe20," mulheres maiores de 20 anos")
print("O homem mais velho tem ", maisVelho," anos")