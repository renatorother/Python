contador = 0

while contador <= 100 :
    print(contador)
    contador += 1

    if contador == 6:
        print('Não vou exibir o 6')
        continue

    if contador == 40:
        print(contador)
        break

