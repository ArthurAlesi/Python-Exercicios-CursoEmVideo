# Escreva um programa que pergunte a quantidade de KM percorridos
#  por um carro e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar sabendo que o carro custa 6o reais por dia
#  e 0,15  reais por km rodado
dias = int(input("quantos dias alugados"))
km = float(input("quantos km rodados"))
total = (dias * 60) + (km * 0.15)
print("O total a pagar é %.2f"% total)
