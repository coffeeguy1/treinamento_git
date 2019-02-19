km = float(input('Digite a velocidade em KM: '))

if km > 80.0:
    total = (km - 80.0) * 7
    print('Você foi multado e deve pagar: {}'.format(total))
