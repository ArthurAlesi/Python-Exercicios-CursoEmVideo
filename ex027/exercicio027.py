# Faça um programa que leia o nome completo de uma
# pessoa mosrtando em seguida o primeiro e o ultimo nome
# separadamente
nomeCompleto = input("Diga seu nome completo").split()
primeiroNome = nomeCompleto[0]
ultimoNome = nomeCompleto[-1]
print("Primeiro nome %s"% primeiroNome)
print("Ultimo nome %s"% ultimoNome)
