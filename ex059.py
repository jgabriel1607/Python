print('Vamos analisar alguns números: ')
n1 = int(input('Digite o 1ª número: '))
n2 = int(input('Digite o 2º número: '))
r = 0
maior = 0
print('Agora selecione uma opção: ')
opcao = 0
while opcao != 5:
    opcao = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do Programa  \n'))
    if opcao == 1:
        r = n1 + n2
        print('Você selecionou SOMA: ')
        print('A soma do valores é igual a: {} \n'.format(r))
    elif opcao == 2:
        r = n1 * n2
        print('Você selecionou MULTIPLICAÇÃO: ')
        print('O produto dos valores é igual a: {} \n'.format(r))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Você selecionou MAIOR: ')
        print('O maior valor digitado foi: {} \n'.format(maior))
    elif opcao == 4:
        print('Você selecionou NOVOS NÚMEROS: ')
        n1 = int(input('Digite o 1ª número: '))
        n2 = int(input('Digite o 2º número: '))
    elif opcao == 5:
        print('Você selecionou SAIR DO PROGRAMA.')
    else:
        print('Escolha uma opção válida.')
        opcao = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do Programa  \n'))
print('FIM!')
