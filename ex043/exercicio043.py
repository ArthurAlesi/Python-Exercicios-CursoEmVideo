# Desenvolva um programa que leia o peso e a  altura de uma pessoa
# calcular o imc

altura = float(input("Diga sua altura"))
massa = float(input("Diga sua massa"))
imc = massa / (altura **2)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25<= imc <30:
    print("sobrepeso")
elif 30<=imc< 40:
    print("Obesidade")
else:
    print("Obesidade morbida")
