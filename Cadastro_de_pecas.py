from cadastra_peca import cadastrarPeca

lista_pecas = []
codigo_produto = 0
nome = "Guilherme Mendonca Antunes"


def separador():
    print('-' * 50)


# ---Função que consulta peças
def consultarPeca():
    print('Bem vindo a consulta peças!')
    while True:
        try:
            separador()
            opcaoConsulta = int(input('''Escolha a opção desejada:
1-Consultar Todas as Peças
2-Consultar Peças por Código
3-Consultar Peças por Fabricante
4-Retornar
>> '''))

            separador()
            # consulta de todas peças
            if opcaoConsulta == 1:
                print('Bem-vindo a consulta de todas peças!')
                if len(lista_pecas) != 0:
                    print(f'CONSULTANDO...')
                    # pegando cada dicionário na lista
                    for peca in lista_pecas:
                        # pegando cada chave e valor de cada dicionario
                        for key, value in peca.items():
                            # printando chave e valor
                            print(f'{key}:{value}')
                        separador()
                else:
                    print('Nenhuma peça encontrada :(')

            elif opcaoConsulta == 2:
                print('Bem vindo a consulta de peças por código')
                separador()
                opcaoConsultaCodigo = int(input('Digite o código desejado: '))

                for peca in lista_pecas:
                    if peca['codigo'] == opcaoConsultaCodigo:
                        separador()
                        for key, value in peca.items():
                            print(f'{key} : {value}')
                        separador()

            elif opcaoConsulta == 3:
                print('Bem-vindo a consulta de peças por fabricante')

                consultaFabricante = input('Digite o fabricante desejado: ')
                separador()

                # recupera o dicionário
                for peca in lista_pecas:
                    # checa de o fabricante é igual ao digitado
                    if peca['fabricante'] == consultaFabricante:
                        # começa a recuperar as keys e values do dicionário
                        for key, value in peca.items():
                            # printa elas
                            print(f'{key} : {value}')
                        separador()
            elif opcaoConsulta == 4:
                return
            else:
                separador()
                print('Opção inválida. Tente novamente.')
                separador()
                continue
        except ValueError:
            separador()
            print('Você não digitou um número. Tente novamente.')
            separador()
            continue


# --Função que remove peças
def removerPeca():
    separador()
    print('Bem vindo a remoção de peças! ')
    separador()
    while True:
        opcaoRemover = int(input('Digite o código da peça que deseja remover: '))
        separador()
        for peca in lista_pecas:
            if peca['codigo'] == opcaoRemover:
                lista_pecas.remove(peca)
                print('Peça removida. Retornando...')
        separador()
        continuar = int(input('Digite 1 caso queira continuar e 0 caso não: '))
        if (continuar == 1):
            continue
        elif (continuar == 0):
            break


# ---------------------MENU---------------------------
while True:
    try:
        separador()
        print(f'Bem vindo ao Controle de Estoque da Bicicletaria de {nome}')
        print('Escolhe a opção desejada:')
        print('1-Cadastrar Peças')
        print('2-Consultar Peças')
        print('3-Remover Peças')
        print('4-Sair')

        opcaoSelecionada = int(input('>>'))
        separador()
        if opcaoSelecionada == 1:
            codigo_produto += 1
            cadastrarPeca(codigo_produto)
        elif opcaoSelecionada == 2:
            consultarPeca()
        elif opcaoSelecionada == 3:
            removerPeca()
        elif opcaoSelecionada == 4:
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')
            continue
    except ValueError:
        print('Você digitou um valor inválido. Tente novamente')
        continue
