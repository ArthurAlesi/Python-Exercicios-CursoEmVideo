'''
Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
seu aplicativo deverá analisar se a expressao passada esta com os parenteses abertos
e fechados na ordem correta
'''
expressao = str(input("digite uma expressao"))
pilha = []
for simb in expressao:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expressao está valida")
else:
    print("Sua expressao está errada")