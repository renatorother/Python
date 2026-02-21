inicial = int(input('Qual valor deseja iniciar?'))
final = int(input('Qual valor deseja finalizar?'))

x = inicial
while ( x <= final):
    if ( x % 2 == 0):
     print(x)
    x = x + 1


""" soma = 0
cont = 1
while (cont <= 5):
    x = int(input(f'Digite a {cont}ª note: '))
    soma += x
    cont += 1
    media = soma / 5
print(f'Média final: {media}') """


""" x = int(input('Digite um valor maior que zero: '))
while(x <= 0):
    x = int(input('Digite um valor maior que zero: '))
print(f'Você digitou {x}. Encerrando o programa...') """

    
""" print('Digite uma mensagem que irei repeti-la')
print('Para encerrar o programa digite "sair"')

while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        print('Programa encerrado')
        break """

""" while True:
    nome = input('Qual o seu nome?')
    if (nome != 'Renato'):
        continue

    senha = input('Digite sua senha: ')
    if (senha == 'tatao123'):
        print('Login efetuado com sucesso')
        break """



""" for i in range(1,11,2):
    print(i) """

""" x = 2
while (x < 13):
    x += 1
    print(x) 


for i in range (3,13):
    print(i) """

""" i = 0
while (i <= 9):
    print(i)
    i += 2

for i in range (0,9,2):
    print(i) """

""" print('LANCHONETE')
print('1 - Coxinha (R$5,00)')
print('2 - Pastel (R$7,00)')
print('3 - Café (R$4,00)')
print('4 - Suco (R$6,00)')
print('5 - SAIR')

total = 0
while True:
    op = int(input('Qual item deseja comprar? '))
    
    if (op == 1):        
        qtd = int(input('Quantas unidades deseja comprar? '))
        total += qtd * 5.00

    elif (op == 2):        
        qtd = int(input('Quantas unidades deseja comprar? '))
        total += qtd * 7.00

    elif (op == 3):        
        qtd = int(input('Quantas unidades deseja comprar? '))
        total += qtd * 4.00

    elif (op == 4):        
        qtd = int(input('Quantas unidades deseja comprar? '))
        total += qtd * 5.00

    elif (op == 5):
       print(f'O valor total da compra é de {total}')        
       break

    else:
        print('Produto inválido') """


