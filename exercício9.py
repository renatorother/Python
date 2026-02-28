while True:
    input_1 = input('Digite o primeiro número: ')
    operacao = input('[+] [-] [*] [/] : ')
    input_2 = input('Digite o segundo número: ')

    numeros_validos = None

    try:
        num_1 = float(input_1)
        num_2 = float(input_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos')
        continue

    operadores_permitidos = '+-*/'

    if operacao not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operacao) > 1:
        print('Digite apenas um operador')
        continue

    # OPERAÇÕES ----------------------------------

    if operacao == '+':
        print(num_1 + num_2)

    elif operacao == '-':
        print(num_1 - num_2)

    elif operacao == '*':
        print(num_1 * num_2)

    elif operacao == '/':
        print(num_1 / num_2)

    else:
        print('Não deveria ter chegado aqui.')         

   
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break



    