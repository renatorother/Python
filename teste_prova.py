lista_livros = []

def cadastrar_livro():
	nome = input('Digite o nome do livro: ')
	escritor = input('Digite o nome do livro: ')
	editora = input('Digite o nome do livro: ')
	ibsn = input('Digite o nome do livro: ')

	livro = {
	'nome': nome,
	'escritor': escritor,
	'editora': editora,
	'ibsn': ibsn,
	}
	
	lista_livros.append(livro.copy())
	print('Cadastrado com sucesso!')

cadastrar_livro()