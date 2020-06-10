# Diga se  o nome duma cidade digitada começa com santo
cidade = input("Diga o nome de uma cidade")
if(cidade[:5].upper() == 'SANTO'):
    print("%s começa com Santo"%cidade)
else:
    print("%s não começa com Santo"%cidade)