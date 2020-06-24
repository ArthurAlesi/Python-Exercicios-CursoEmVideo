'''
leia uma frase e diga se é um palindromo
'''
frase = str(input("Digite"))
fraseSemEspaco = frase.replace(" ","")
fraseAoContrario = fraseSemEspaco[::-1]
if fraseSemEspaco == fraseAoContrario:
    print("É palindromo")
else:
    print("não é plandromo")