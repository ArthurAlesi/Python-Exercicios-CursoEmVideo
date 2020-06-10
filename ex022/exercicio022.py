# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas E minúsculas
# Quantas letras ao t odo sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = input("Diga seu nome completo")
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
qtdEspaço = nome.count(' ')
qtdLetras = len(nome) - qtdEspaço
listaNomes = nome.split(" ")
qtdPrimeiroNome = len(listaNomes[0])

print("O nome em maíusculo é %s"%nomeMaiusculo)
print("O nome em mnúsculo é %s"%nomeMinusculo)
print("Quantidade de letras %s"% qtdLetras)
print("Quantidade de letras do primeiro nome %s"% qtdPrimeiroNome)

