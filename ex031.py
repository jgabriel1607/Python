print('Vamos ver quanto custará a viagem: ')
km = float(input('Digite a distância total em Km: '))
if km <= 200.0:
    print('Para percorrer {}Km, sua viagem custará R$ {:.2f}'.format(km, km * 0.5))
else:
    print('Para percorrer {}Km, sua viagem custará R$ {:.2f}'.format(km, km * 0.45))

