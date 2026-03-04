#append - Adiciona um item ao final
#insert - Adiciona um item no índice indicado
#pop - Remove do final ou o índice indicado
#del - apaga um índice indicado
#clear - limpa a lista
#extend - extende a lista


lista = [10, 20, 30, 40]
lista[2] = 300
lista.append(50) 
lista.append(60)
lista.pop() 
lista.append(70)
lista.insert(0, 5)
del lista[2] 

#lista.clear


print(lista)
print(lista[2])