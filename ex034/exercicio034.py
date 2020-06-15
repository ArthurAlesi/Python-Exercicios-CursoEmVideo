# Pergunte o salário de um funcionario e calcule o valor do seu aumento
# se salarior maior q 1250, calcule o aumento de 10%
# para salarios menores, o aumento é de 15%

salario = float(input("Diga é o salário"))
if salario >= 1250:
    novo = salario * 1.1
else:
    novo = salario * 1.15

print("O salario novo é :", novo)