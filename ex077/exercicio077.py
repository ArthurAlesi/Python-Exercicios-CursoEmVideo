'''
Crie um prograam que tenha uma tupla, com varias palavras (sem acentos).
Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais.
'''
listaPalavra = ('agua', 'banana', 'caqui', 'damasco')

for i in listaPalavra:
    print('vogais de ',i , ": ", end=" ")
    for l in i:
        if l in 'aeiouAEIOU':
            print(l, end=" ")
    print()