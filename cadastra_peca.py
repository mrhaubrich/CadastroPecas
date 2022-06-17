from Cadastro_de_pecas import separador, lista_pecas
# ---Função cadastra peças
def cadastrarPeca(codigo):
    print('Bem vindo ao cadastro de peças!')
    print(f'Código da peça: {codigo}')
    separador()
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o nome do fabricante: ")
    valor = float(input("Digite o valor da peça"))
    separador()

    dicionario_peca = {'codigo': codigo,
                       'nome': nome,
                       'fabricante': fabricante,
                       'valor': valor}

    lista_pecas.append(dicionario_peca.copy())

    print('Peça Cadastrada!')