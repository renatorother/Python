nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = (f'{nome[ : :-1]}')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    
    if nome and ' ' in nome:
        print('Seu nome contém espaço(s)')

    elif nome and ' ' not in nome:
        print('Seu nome não contém espaço(s)')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Preencha as informações')










    