'''
Crie um proghrama que tenha uma tupla unica com nomes de rodutos e seus
respectivos precos, na sequência. No final, mostre uma listagem de
precos organizando os dados em forma tabular
'''
lista = (
    'lapis',1.75,
    'borracha',2,
    'caderno', 15.90,
    'estojo', 25,
    'transferidor', 4.20,
    'compasso', 9.99,
    'mochila', 120.32,
    'caneta',22.3,
    'livro',34.9,
)
for i in range(0,len(lista)):
    if i % 2 ==0:
        print(lista[i], end = " ")
    else:
        print("R$ %.2f" %lista[i])