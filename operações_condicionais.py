primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor:')

num_1 = int(primeiro_valor)
num_2 = int(segundo_valor)

if num_1 == num_2 :
    print('Os números são iguais')
elif num_1 >  num_2:
    print('O primeiro valor é maior que o segundo')
else:
    print('O primeiro valor é menor que o segundo')