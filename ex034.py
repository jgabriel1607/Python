print('Vamos verificar os reajustes de salários: ')
sal = float(input('Digite o valor do seu salário: R$ '))
if sal <= 1250.00:
    salr = sal + (sal * 0.15)
else:
    salr = sal + (sal * 0.10)
print('Seu salário de R$ {:.2f} será reajustado para R$ {:.2f}.'.format(sal, salr))
