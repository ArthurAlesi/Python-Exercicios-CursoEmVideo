# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre
# O comprimento da Hipotenusa

catetoOposto = float(input("Cateto oposto:"))
catetoAdjacente = float(input("Cateto adjacente"))
hipotenusa = (catetoOposto**2  + catetoAdjacente**2) ** 0.5
print("A hipotenusa é %.2f"%(hipotenusa))