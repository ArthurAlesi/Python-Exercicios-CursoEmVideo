entrada = input("Digite alguma coisa")
print("O tipo é ",  type(entrada))

#função que importa se apenas espaço foi digitado
print("Feito por espaços",entrada.isspace())

#informa se a entrada é  numerico
print("É um numero: ", entrada.isnumeric())

# informa se é uma letra
print("É alfabético: ", entrada.isalpha())

#informa se é alpha numerico
print("É alpha numérico", entrada.isalnum())

#retorna se está maiusculo
print("Está em maiúsculas?", entrada.isupper())

#retorna se está em letras minusculas
print("Esta em minúscula?: ", entrada.islower())

# Informa se está capitalizada (ou maiuscula ou minusculas)
print("Esta capitalizada:", entrada.istitle())



