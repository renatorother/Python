lista = [10, 20, 30, 40]
lista[2] = 300
lista.append(50) #adiciona ao final da lista
lista.append(60)
lista.pop() #remove o último valor da lista ou o índice indicado
lista.append(70)
del lista[2] #deleta o índice indicado da lista


print(lista)
print(lista[2])