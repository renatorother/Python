# s - string
# d - int
# f - float
# .<número de casas decimais>f
# x ou X - Hexadecimal
# (caractere)(><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centro
# = - força o número a aparecer antes
# sinal - + ou -
# conversion flags - !r !s !a


variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')