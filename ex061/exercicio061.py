'''
REfaça o desafio 51 lendo o primeiro termo e a razao de uma PA
mostre os 10 primeiros termos usando while
'''
primeiro = int(input("diga o primeiro termo"))
razao = int(input("Diga a razao"))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo)
    termo += razao
    cont += 1
print("fim")