'''
crie uma tupla preenchida com os 20 primeiros colocados
da tabela do campeonado carioca
mostre:
os 5 primeiros
os ultimos 4
time em ordem alfabetica
posicao do time da chapeconese
'''

times = ("corintias", 'palmeiras', 'santos', 'gremio',
         'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
         'atletico', 'botafogo', 'atletico-pr', 'bahia',
         'sao paulo', 'fluminense', 'sport recife',
         'ec vitoria', 'coritiba', 'havai', 'ponte preta',
        'atletico-go'
         )
print(times[0:5])
print(times[-4:])
print("Time em ordem alfabética: ", sorted(times))
for i in range(len(times)):

    if times[i] == "chapecoense":
        print("posição da chapecoense: ", i + 1)
        break