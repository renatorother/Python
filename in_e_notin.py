# Operadores in e not in
# String são iteráveis
# 0 1 2 3 4 5
# R e n a t o
#-6-5-4-3-2-1

# nome = 'Renato'
# # print(nome[5])
# # print(nome[-6])
# print('a' in nome)
# print('z' in nome)
# print('z' not in nome)
# print('a' not in nome)

nome = input('Digite seu nome: ')
find = input('O que você deseja encontrar?: ')

if find in nome:
    print(f'{find} está em {nome}')
else:
    print(f'{find} não está em {nome}')