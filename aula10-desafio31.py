km = float(input('Digite a distância em quilometros: '))

if km <= 200:
    total = km * 0.50
    print('A sua viagem vai custar: {}'.format(total))
else:
    total = km * 0.45
    print('A sua viagem vai custar: {}'.format(total))
