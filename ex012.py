print('Descubra quanto vale um produto com 5% de desconto: \nObs: Utilize ponto para separar casas decimais.')
pr = float(input('Digite o valor integral do produto desejado: '))
npr = pr - (pr * 5 / 100)
print('O valor do produto com desconto de 5% será de {:.2f}'.format(npr), '\n')

# Exercício extra:
print('Descubra quanto vale um produto com seu desconto: \nObs: Utilize ponto para separar casas decimais.')
pr = float(input('Digite o valor integral do produto desejado: '))
prc = int(input('Digite o valor do desconto: '))
npr = pr - (pr * prc / 100)
print('O valor do produto com desconto de {}% será de {:.2f}'.format(prc, npr))
