# faça um programa q leia o ano de nascimento de um jovem e informe de
# acordo com sua idade se ele ainda vai se alistar ao serviço miliar,
# se é a hora de se alistar ou se ja passsou do tempo do alistamento

from datetime import date
hoje = date.today().year
print(hoje)
nascimento = int(input("Diga o ano que voce nasceu"))
idade = hoje - nascimento
if idade == 18:
    print("Esta na hora de voce se alistar")
elif idade < 18:
    print("Voce ainda vai ter q se alistar")
else:
    print("Ja passou da hora de voce se alistar")
