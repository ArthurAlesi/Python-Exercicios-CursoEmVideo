'''
leia a idade e o sexo
pergunte se o usuario quer ou nao continuar

no final mostre
quantas pessoas maiores de 18
quantos homens
quantas mulheres tem menos de 20 anos
'''
continuar = 's'
maioresQtd = 0
qtdHomem = 0
mulheresMenoresDe21 = 0
while continuar not in 'nN':

    idade = int(input("Diga a idade"))
    sexo = input("Diga o sexo")
    continuar = str(input("Deseja continuar? [s]sim [n]nao"))

    if idade >= 18:
        maioresQtd += 1
    if sexo in "mM":
        qtdHomem +=1
    if sexo in "fF" and idade < 20:
        mulheresMenoresDe21 += 1
    if continuar in "sS":
        continue
    elif continuar in "nN":
        break
    else:
        print("Voce entrou com uma entrada invalida. o programa continuará")

print("Mulheres menores de 21: ", mulheresMenoresDe21)
print("qtd de homens: ", qtdHomem)
print("Maiores de idade: ", maioresQtd)
