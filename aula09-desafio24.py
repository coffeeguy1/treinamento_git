city = str(input('Digite o nome da sua cidade: '))

splited_name = city.split()

first_name = splited_name[0]

first_name = first_name.upper()

test = first_name.find('SANTO')

if test != -1:
    print('A sua cidade começa com SANTO')
else:
    print('A sua cidade não começa com SANTO')
