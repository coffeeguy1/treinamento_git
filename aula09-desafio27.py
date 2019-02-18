name = str(input('Digite o seu nome: '))

name_list = name.split()
length = len(name_list)

print('{}'.format(name))
print('Primeiro: {}'.format(name_list[0]))
print('Ultimo: {}'.format(name_list[length-1]))
