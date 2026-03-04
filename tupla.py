#tupla - uma lista imutável

nomes = ('Renato', 'Julia', 'Miguel') #tupla é uma lista sem colchetes
print(nomes)


#também posso converter uma lista em uma tupla e vice-versa
nomes = ['Renato', 'Julia', 'Miguel']
nomes = tuple(nomes)
nomes = list(nomes)