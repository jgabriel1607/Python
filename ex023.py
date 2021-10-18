print('Vamos ver separadamente os algarismos de um número: ')
n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O número {} possui: \n{} milhar(es) \n{} centena(s) \n{} dezena(s) \n{} unidade(s)'. format(n, m, c, d, u))
