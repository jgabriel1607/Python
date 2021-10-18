print('Descubra quantos dólares você pode comprar, levando em conta a cotação do dólar à 3,27: ')
d = float(input('Digite quantos reais você possui na carteira: R$ '))
cd = d // 3.27
rd = d % 3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f} e sobrarão R$ {:.2f}'.format(d, cd, rd))
