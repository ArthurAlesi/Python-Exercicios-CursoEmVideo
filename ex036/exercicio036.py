# escreva um programa para aprovar o emprestimo bancario para a compra de uma
# de uma casa. Pergunte o valor da casa, o salario do comprador e
# em quantos anos ele vai pagar
# A prestacao mensal nao pode exercer 30% do salario ou entao o
# emprestimo sera negado

valorCasa = float(input("Diga o valor da casa"))
salario = float(input("Diga o seu salário"))
ano = int(input("Diga em quantos anos você pretende pagar"))
prestacao = valorCasa / (ano * 12)
limite = salario  * 0.3
if prestacao >= limite:
    print("emprestimo negado")
else:
    print("Pode pagar! ")