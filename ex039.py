from datetime import date
print('Vamos descobrir se está na hora de se alistar: ')
anonasc = int(input('Digite o ano em que nasceu: '))
anoatual = date.today().year
idade = anoatual - anonasc

print('Você tem {} anos.'.format(idade))
if idade < 18:
    saldo = 18 - idade
    anoalist = anoatual + saldo
    print('Você ainda não precisa se alistar no serviço militar. Faltam {} anos. E seu ano de alistamento será em {}'.format(saldo, anoalist))
elif idade > 18:
    saldo = idade - 18
    anoalist = anoatual - saldo
    print('Já passou o tempo de se alistar no serviço militar. Passaram {} anos. E seu ano de alistamento foi em {}.'.format(saldo, anoalist))
else:
    print('Você deve se alistar no serviço militar esse ano.')


