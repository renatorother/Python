# cuidados com dados mutáveis
# = - coppia o valor (imutáveis)
# = - aponta para o mesmo valor na memória (mutáveis)

lista_a = ['Renato', 'Julia', 1, True, 1.5]
lista_b = lista_a.copy() #está fazendo uma cópia da lista A para dentro da lista B

lista_a[0] = 'Qualquer coisa' #está fazendo uma alteração na lista A sem mexer na cópia dentro da lista B

print(lista_a)
print(lista_b)