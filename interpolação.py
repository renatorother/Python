# Interpolação básica de strings
# s - string
# d e i - inteiro
# f - float 
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Renato'
preco = 1045.556234561234
variavel = '%s, o preço é de R$%.2f' % (nome, preco)
print(variavel)
print('O Hexadecimal de %d é %05X' % (1500, 1500))