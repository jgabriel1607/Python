print('Vamos verificar qual é o primeiro e último nome: ')
nome = str(input('Digite o seu nome completo: ')).strip()
nomes = nome.split()
print('Seu primeiro nome é: {}'.format(nomes[0]))
print('Seu útlimo nome é: {}'.format(nomes[len(nomes) - 1]))
