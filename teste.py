biblioteca = {}

def adicionarLivro (codigo, titulo):

    if codigo in biblioteca:
        print(f'O livro {titulo} já existe na biblioteca')

    else:
        biblioteca[codigo] = titulo
        print(f'O livro {titulo}, com código {codigo} foi adicionado com sucesso!')

adicionarLivro('666', 'O senhor dos anéis')