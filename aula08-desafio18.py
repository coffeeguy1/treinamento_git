import math

angulo = float(input('Digite o valor do angulo: '))



seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno do angulo {} é {:.2f}'.format(angulo, seno))
print('O cosseno do angulo {} é {:.2f}'.format(angulo, cosseno))
print('A tangente do angulo {} é {:.2f}'.format(angulo, tangente))



