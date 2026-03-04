#append - Adiciona um item ao final
#insert - Adiciona um item no índice indicado
#pop - Remove do final ou o índice indicado
#del - apaga um índice indicado
#clear - limpa a lista
#extend - extende a lista


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

lista_a.extend(lista_b)

print(lista_a)
print(lista_c)
