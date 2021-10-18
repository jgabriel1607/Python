def dados(msg):
    while True:
        print('=' * 60)
        print(f'{"MENU PRINCIPAL":^60}')
        print('=' * 60)
        print('\033[0;33m1\033[m - \033[0;34mPessoas Cadastradas\033[m')
        print('\033[0;33m2\033[m - \033[0;34mCadastrar Nova Pessoa\033[m')
        print('\033[0;33m3\033[m - \033[0;34mSair do Sitema\033[m')
        print('-' * 60)
        x = input(msg)
        while True:
            try:
                x = int(x)
            except (ValueError, TypeError):
                print(f'\033[0;31mErro: Digite uma opção válida.\033[m')
                x = input(msg)
                continue
            else:
                if x < 0 or x > 3:
                    print(f'\033[0;31mErro: Digite uma opção válida.\033[m')
                    x = input(msg)
                    continue
            break
        if x == 1:
            print('=' * 60)
            print(f'{"Opção 1 - Pessoas Cadastradas":^60}')
            print('=' * 60)
            continue
        if x == 2:
            print('=' * 60)
            print(f'{"Opção 2 - Cadastrar Nova Pessoa":^60}')
            print('=' * 60)
            continue
        if x == 3:
            print('=' * 60)
            print(f'{"Opção 3 - Sair do Sistema":^60}')
            print('=' * 60)
            print('Saindo...')
            break
    return x


def leiaint(i):
    while True:
        try:
            i = int(i)
        except (ValueError, TypeError):
            print('\033[0;31mErro: Digite uma opção válida.\033[m')
            i = input('Sua Opção: ')
        else:
            break
    return i


def linha(tam=60):
    print('=' * tam)


def cabecalho(txt):
    linha()
    print(txt.center(60))
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[0;33m{cont}\033[m - \033[0;34m{item}\033[m')
        cont += 1
    linha()
    opc = leiaint(input('Sua Opção: '))
    return opc







