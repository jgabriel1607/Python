print('Conversor de Metros: ')
m = float(input('Obs: Utilize ponto para separar casas decimais \nDigite um número: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{:.1f} metros é igual a:'.format(m))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(km, hm, dam, dm, cm, mm))

