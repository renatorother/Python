entrada = input('Digite seu nome: ')

if len(entrada) <= 4 and len(entrada) > 0 :
    print('Seu nome é muito curto')

elif len(entrada) == 5 or len(entrada) == 6:
    print('Seu nome é normal')

elif len(entrada) > 6:
    print('Seu nome é muito grande')

else:
    print('Digite alguma coisa')