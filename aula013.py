'''
Laçoes de repetição:
laço variável no intervalo(0,x) --> for variavel in range(0,x)
'''

'''
for a in range(0, 5):
    print('Oi')
print('Fim')
for b in range(1, 6): #Conta de 1 a 5, se colocar (0,6) conta de 0 a 6
    print(b)
print('Fim')
for c in range(5, 0, -1): #Para contar ao contrário.
    print(c)
print('Fim')
for d in range(0, 7, 2): #Para contar de 2 em 2.
    print(d)
print('Fim')
'''

n = int(input('Digite um número: '))
for mostre in range(0, n+1):
    print(mostre)
print('Fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for conta in range(i, f+1, p):
    print(conta)
print('Fim')
'''
for c in range(0, 3):
    n = int(input('Digite um número: '))
print('Fim') --> Vai receber um número 3 vezes.
'''
s = 0
for soma in range(0, 4):
    n = int(input('Digite um número: '))
    s += n # --> s = s + n
print('A soma dos números digitados é igual a {}'.format(s))



