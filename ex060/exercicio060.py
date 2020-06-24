'''
leia um numero qualquer e mostre sue fatorial
'''

num1 = int(input("diga um numero"))
num = num1
for i in range(1,num):
    num *= i
print(num1,"! = ", num)
