n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = 0

if n1 > n2 and n1 > n3:
    print('O primeiro número é o maior número: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O segundo número é o maior número: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O segundo número é o maior número: {}'.format(n3))

