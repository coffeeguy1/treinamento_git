name = str(input('Digite o seu nome completo: '))

print('{}'.format(name.upper()))
print('{}'.format(name.lower()))
print('{}'.format(len(name)))

name_nobar = name.replace(' ', '')
length = len(name_nobar)
print('{}'.format(length))

name_list = name.split()
first_name = name_list[0]

print('{}'.format(len(first_name)))


