# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o preço normal e condição de pagamento
# a vista dinheiro 10% de desconto
# a vista cartao 5% de desconto
# 2x cartao preço normal
# 3x ou mais
compra = float(input("Informe o preço das compras"))
print("Escolha a forma de pagamento")
print("1 - vista dinheiro/cheque")
print("2 - vista cartao")
print("3 - 2x cartao")
print("4 - 3x ou + cartao")
entrada = int(input())
if entrada == 1:
    total = compra * 0.9
    print("Voce pagara ", total)
elif entrada == 2:
    total = compra * 0.95
    print("Voce pagara ", total)
elif entrada == 3:
    parcela = compra / 2
    print("2 parcelas de ", parcela)
elif entrada ==4:
    total = compra * 1.2
    parcela = total / 3
    print("3 parcelas de ", parcela)
