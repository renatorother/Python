biblioteca = {}

def adicionar_livro(codigo, titulo):

    if codigo in biblioteca:
        print(f'O livro {titulo} já existe na biblioteca')

    else:
        biblioteca[codigo] = titulo
        print(f'Sucesso! O livro "{titulo}" foi adicionado com o código {codigo}')


adicionar_livro('666', 'O Senhor dos Anéis')