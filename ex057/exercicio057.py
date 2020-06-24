'''
leia o sexo mas só aceite os valores de 'm' ou 'f'
caso esteja errado peça novamente até ter um valor correto
'''
sexo = str(input("Diga o sexo"))
while sexo not in "fFmM":
    sexo = str(input("Diga o sexo"))

print("O sexo foi", sexo)