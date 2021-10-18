print('Descubra quanto deve pagar pelo carro alugado:')
d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
t = (d * 60) + (km * 0.15)
print('Pela quantidade de {} dias alugados e {} Km rodados, o total a pagar é de R$ {:.2f}'.format(d, km, t))


