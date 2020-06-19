# A confederacao nacional de natacao precisa de um prorama que leia
# o ano de nascimento de um atleta e mostre sua categoria de acordo com
# sua idade
from datetime import  date
hoje = date.today().year
nascimento = int(input("Diga o ano do seu nascimento"))
idade = hoje - nascimento
print(idade)
if( idade <= 9):
    print("Atleta mirim")
elif( idade <= 14):
    print("Atleta infantil")
elif (idade <= 19):
    print("Atleta Junior")
elif (idade <= 25):
    print("Atleta senior")
else:
    print("Atleta Master")