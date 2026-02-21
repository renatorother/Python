#\r\n <--- quebra de linha do windows (CRLF)
#\n <--- quebra de linha de sistemas baseados em Unix (LF)
print(12, 34, 1011, sep='-', end='\r\n')
print(56, 78, sep='-', end='##')
print(56, 78, sep='-', end='##\n')
print(9, 10, sep='-', end='\n')

#caractere de escape (\)
print('Renato \'Rother\'')

print('Renato "Rother"') #aspas invertidas para serem exibidas
print("Renato 'Rother'")

