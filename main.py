ARQUIVO = 'contatos.txt'


def salvar_contatos(contatos):
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        for contato in contatos:
            arquivo.write(contato + '\n')


def carregar_contatos():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return [linha.strip() for linha in arquivo]
    except FileNotFoundError:
        return []


def adicionar_contato(contatos):
    nome = input('Nome: ')
    telefone = input('Telefone: ')

    contato = f'{nome} - {telefone}'
    contatos.append(contato)

    salvar_contatos(contatos)
    print('Contato adicionado.')


def listar_contatos(contatos):
    if not contatos:
        print('Nenhum contato cadastrado.')
        return

    print('\n--- CONTATOS ---')
    for i, contato in enumerate(contatos, start=1):
        print(f'{i} - {contato}')
    print()


def remover_contato(contatos):
    if not contatos:
        print('Nenhum contato para remover.')
        return

    print('\n--- REMOVER CONTATO ---')
    for i, contato in enumerate(contatos, start=1):
        print(f'{i} - {contato}')

    try:
        indice = int(input('Número do contato: '))
        removido = contatos.pop(indice - 1)

        salvar_contatos(contatos)
        print(f'Contato "{removido}" removido.')

    except ValueError:
        print('Entrada inválida.')
    except IndexError:
        print('Contato não encontrado.')


def mostrar_menu():
    print('--- MENU ---')
    print('1 - Adicionar')
    print('2 - Listar')
    print('3 - Remover')
    print('4 - Sair')


def main():
    contatos = carregar_contatos()

    while True:
        mostrar_menu()
        opcao = input('Escolha: ')

        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            listar_contatos(contatos)
        elif opcao == '3':
            remover_contato(contatos)
        elif opcao == '4':
            print('Encerrando...')
            break
        else:
            print('Opção inválida.')

        print()


if __name__ == '__main__':
    main()