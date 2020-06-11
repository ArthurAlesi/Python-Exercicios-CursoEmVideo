# escreva um programa que leia a velocidade um carro
# se ele ultrapassar 80 km/h multe ele
# a multa custa 7 reais por km excedido

velocidade = float(input("Informe sua velocidade"))
if velocidade > 80:
    print("Voce foi multado")
    multa = (velocidade - 80) * 7
    print("Sua multa é de ", multa)

else:
    print("Parabens. dirija com segurança")