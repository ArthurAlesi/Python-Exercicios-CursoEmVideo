# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, coseno e tangente.
import math
angulo = float(input("Digite o ângulo em graus"))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("Seno %.2fº = %.2f"%(angulo,seno))
print("Cosseno %.2fº = %.2f"%(angulo,cosseno))
print("Tangente %.2fº = %.2f"%(angulo,tangente))