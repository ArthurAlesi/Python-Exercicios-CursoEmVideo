'''
leia um termo e a razão de uma pa no
final mostre os 10 primeiros termos dessa progressão
'''

prim = int(input("primeiro termo: "))
r = int(input("Razão"))
n = int(input("diga o numero de termos"))
enesimo = prim + (n - 1)* r
for i in range(prim,enesimo,r):
    print(i)

