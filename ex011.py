print('Descubra a quantidade de tinta necessária para pintar sua parede: \nLevando em consideração que 1L pinta 2m² \nObs: Utilize ponto para separar casas decimais.')
al = float(input('Digite a altura de sua parede em metros: '))
lg = float(input('Digite a largura da sua parede em metros: '))
a = al * lg
li = a / 2
print('Para pintar uma parede de {:.2f}m² você precisará de {:.1f} litros de tinta.'.format(a, li))
