print('Vamos coletar alugns números e ver média, maior e menor: ')
soma = cont = media = 0
prosseguir = 'S'
while prosseguir == 'S':
    n = int(input('Digite um número inteiro: '))
    prosseguir = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    cont += 1
media = soma / cont
print('Você escolheu sair')
print('A média de todos os números informado é {:.2f}.'.format(media))
print('O maior número digitado foi {}.'.format(maior))
print('O menor número digitado foi {}.'.format(menor))
