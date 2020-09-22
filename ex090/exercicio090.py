'''
faça um programa que leia nome e media de um aluno, guardando
também a situacao em um dicionario. No final, mostre o conteudo da
estrutura da tela
'''

aluno = dict()
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f'Media de {aluno["nome"]}:'))
if aluno["media"] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno["media"] < 7:
    aluno["Situacao"] = "recuperacao"
else:
    aluno['Situacao'] = "reprovado"
print("-=" * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
