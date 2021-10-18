'''
Estrutura condicional simples possui apenas if, composta possui if e else.
Estruturas condicionais aninhadas possuem if, elif e else
'''

print('Vamos descobrir se você consiguirá um empréstimo para compra de uma casa: ')
casa = float(input('Digite o valor total da casa: R$ '))
sal = float(input('Digite o valor do seu salário: R$ '))
ano = int(input('Em quantos anos você deseja pagar a casa: '))
meses = ano * 12
prestacao = casa / meses
parcial = sal * 0.3
print(parcial)
if prestacao <= parcial:
    print('Parabéns! Seu empréstimo foi aprovado. As parcelas serão de R$ {:.2f}.'.format(prestacao))
else:
    print('O valor das prestações seriam de R$ {:.2f}, porém ultrapassa 30% do seu salário. Infelizmente seu empréstimo foi negado.'.format(prestacao))




