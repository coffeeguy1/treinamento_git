import math

cateto = float(input('Digite o valor do cateto: '))
cateto_oposto = float(input('Digite o valor do cateto oposto: '))


hipotenuse = math.sqrt(math.pow(cateto, 2) + math.pow(cateto_oposto, 2))

print('O valor da hipotenusa é {}'.format(hipotenuse))
