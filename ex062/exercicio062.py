'''
melhore o desafio 61 perguntando se o usuario quer mostrar mais alguns termos
encerra o programa quando mostrar 0 termos
'''
primeiro = int(input("diga o primeiro termo"))
razao = int(input("Diga a razao"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:

        print(termo)
        termo += razao
        cont += 1
    mais = int(input("Diga quantos termos voce quer mostrar a mais"))
print("Voce mostrou %d termos"% total)
