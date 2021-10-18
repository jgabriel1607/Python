from datetime import date
print('Vamos descobrir a qual categoria de natação você pertence: ')
anonasc = int(input('Digite o ano em que nasceu: '))
anoatual = date.today().year
idade = anoatual - anonasc

print('Você possui {} anos.'.format(idade))

if idade <= 9:
    print('Sua categoria é: Mirim')
elif idade <= 14:
    print('Sua categoria é: Infantil')
elif idade <= 19:
    print('Sua categoria é: Júnior')
elif idade <= 25:
    print('Sua categoria é: Sênior')
else:
    print('Sua categoria é: Master')
