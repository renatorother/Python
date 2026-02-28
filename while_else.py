string = ('Renato Rother')
i = 0
formato = ''

while i < len(string):
    letra = string[i]
    print(letra)  
    i += 1

    if letra == ' ':
        break

else:
    print('Não encontrei espaços na String!')
print('Fora do While!')