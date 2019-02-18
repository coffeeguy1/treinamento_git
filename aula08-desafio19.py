import random

first_name = input('Digite o primeiro nome: ')
second_name = input('Digite o segundo nome: ')
third_name = input('Digite o terceiro nome: ')

name = random.choice([first_name, second_name, third_name])

print('O nome escolhido foi {}'.format(name))
