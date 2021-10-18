from random import randint
print('Vamos jogar PAR ou ÍMPAR.')
pc = randint(0, 10)
cont = 0
while True:
    jogador = int(input('Digite um número: '))
    opcao = ' '
    soma = jogador + pc
    resultado = ' '
    while opcao not in 'PI':
        opcao = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    if soma % 2 == 0:
        resultado = 'P'
    if soma % 2 == 1:
        resultado = 'I'
    if opcao == resultado:
        print('=' * 20)
        print(f'PC escolheu {pc}')
        print(f'{soma} é {resultado}')
        print('Jogador Ganhou.')
        print('=' * 20)
    if opcao != resultado:
        print('=' * 20)
        print(f'PC escolheu {pc}')
        print(f'{soma} é {resultado}')
        print('PC Ganhou.')
        print('=' * 20)
        if cont == 0:
            print('Você não ganhou nenhuma vez.')
        else:
            print(f'Você venceu {cont} vezes.')
            print('=' * 20)
        break
    cont += 1