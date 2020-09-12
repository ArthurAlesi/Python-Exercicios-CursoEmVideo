'''
faça um programa que leia nome, peso de varias pessoas guardando tudo numa lista
- mostre quantas pessoas foram cadastradas
- uma listagem com as pessoas mais pesadas
- uma listagem com as pessoas mais leves

'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("diga o nome")))
    temp.append(float(input("diga o peso")))
    if len(princ) == 0:
        mai = meno = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "nN":
        break

print(princ)
print(len(princ))
print(mai)
print(men)