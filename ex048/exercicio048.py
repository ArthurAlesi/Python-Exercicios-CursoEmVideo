'''
Calcule a sdoma entre todos os numeros imapres que sao multiplso de 3
'''
soma = 0
for i in range(3,499,3):
    if(i % 2 != 0):
        soma += i

print("Soma é", soma)
