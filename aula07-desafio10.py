choose = int(input('1 - Dollar\n2 - Euros\n3 - Pesos\n:'))

real = float(input('Digite o valor em reais: '))

dollar = 3.74
euro = 4.23
peso = 0.096

if choose == 1:
    dollares = real/dollar
    print('O valor em dollar é: {:.2f}'.format(dollar))

elif choose == 2:
    euros = real/euro
    print('O valor em euros é: {:.2f}'.format(euros))

elif choose == 3:
    pesos = real/peso
    print(f"O valor em pesos é: {pesos:.2f}")
    

