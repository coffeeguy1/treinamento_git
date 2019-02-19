import random

num_random = random.randint(0,5)

num_user = int(input('Digite um número entre 0 e 5: '))

if num_user == num_random:
    print('Você acertou!!!!')
else:
    print('Você errou!!!')

print('O número que a máquina escolheu foi: {}'.format(num_random))
