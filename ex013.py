print('Descubra Qual o valor do seu salário com 15% de aumento: \nObs: Utilize ponto para separar casas decimais.')
sl = float(input('Digite o valor de seu salário: '))
nsl = sl + (sl * 15 / 100)
print('O valor do salaário mais acréscimo de 15% é de {:.2f}'.format(nsl))
