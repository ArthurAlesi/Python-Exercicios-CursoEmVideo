# Desenvolva um programa que pergunte a distancia de uma viagem em
# Km, calcule o preço da passagem, cobrando 0,5 por km para viagens de até
# 200km e 0,45 para viagens mais longas

distancia = float(input("Diga a distância em km"))
if distancia <=200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print("O preço da passagem é %s"%preco)