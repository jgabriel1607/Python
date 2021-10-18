def leiaint(num):
    while not num.isnumeric():
        print('Erro! Digite um número inteiro válido.')
        num = input('Digite um número: ')
    return num


n = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}.')
