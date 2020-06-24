'''
leia um numero qualquer e mostre sue fatorial
'''

num = int(input("diga um numero"))
for i in range(1,num):
    num *= i
print(num)