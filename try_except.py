numero_str = input('Digite um valor: ')

try: #fail fast: tente executar esse bloco de código, se falhar já pule para a excessão.
    numero_str.isdigit
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Valor digitado inválido')
    