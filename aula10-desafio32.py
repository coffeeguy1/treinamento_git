year = int(input('Digite o ano(Sem caracter especial entre os números: )'))

if year%4 == 0 and year%400 == 0:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')
