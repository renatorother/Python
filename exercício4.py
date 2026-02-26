entrada = input('Digite um número inteiro: ')

try:   
     
    numero = int(entrada)

    if numero % 2 == 0:
        print('Número par!')
    else:
        print('Número ímpar!')

except:
    print('Você não digitou um número inteiro!')


