texto = 'Renato' #iterável
iterator = iter(texto) #iterador

while True:
    try:
        letra = next(iterator)
        print(letra)

    except StopIteration:
        break