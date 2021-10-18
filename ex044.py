print('Vamos calcular o valor de um produto de acordo com a forma de pagamento: ')
produto = float(input('Digite o valor do produto: R$ '))
print('Escolha a forma de pagamento: ')
metodo = int(input('1. À vista ou Cheque. \n2. À vista no Cartão de Débito. \n3. Cartão de Crédito. \n'))

if metodo == 1:
    produto = produto - (produto * 0.10)
    print('Pagando à vista ou com cheque você tem 10% de desconto. O valor a ser pago será de R$ {:.2f}.'.format(produto))
elif metodo == 2:
    produto = produto - (produto * 0.05)
    print('Pagando à vista no cartão de débito você tem 5% de desconto. O valor a ser pago será de R$ {:.2f}.'.format(produto))
elif metodo == 3:
    parcelado = int(input('Escolha uma opção de parcelamento: \n1. Para pagar em 2x. \n2. Para pagar em 3x ou mais. \n'))
    if parcelado == 1:
        parcela = produto / 2
        print('Pagando em 2x no cartão de crédito o valor a ser pago será de 2x R$ {:.2f} Sem Juros.'.format(parcela))
    elif parcelado == 2:
        vezes = int(input('Digite em quantas parcelas deseja pagar: \n'))
        if vezes >=3 and vezes <=12:
            produto = produto + (produto * 0.20)
            parcela = produto / vezes
            print('Pagando em 3x no cartão de crédito terá juros de 20%. O valor a ser pago será de 3x R$ {:.2f}. O total da compra será de R$ {:.2f}'.format(parcela, produto))
        else:
            print('Nessa opção você deve escolher no mínimo 3 e no máximo 12 parcelas. Digite uma opção válida.')
    else:
        print('Digite uma oção válida.')
else:
    print('Digite uma opção válida.')