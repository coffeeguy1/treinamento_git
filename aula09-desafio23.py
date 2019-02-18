number = str(input('Digite um número: '))

length = len(number)



if length == 1:
    print('Unidade: {}'.format(number[0]))

if length == 2:
    unidade = number[1]
    dezena = number[0]
    print('Unidade: {}'.format(unidade))
    print('Dezena: {}'.format(dezena))

if length == 3:
    unidade = number[2]
    dezena = number[1]
    centena = number[0]
    print('Unidade: {}\nDezena: {}\nCentena: {}'.format(unidade, dezena, centena))

if length == 4:
    unidade = number[3]
    dezena = number[2]
    centena = number[1]
    milhar = number[0]
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))

