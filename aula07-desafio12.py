product = float(input('Digite o preço do produto: '))

descount = product * (5/100)

product_descounted = product - descount

print('O desconto de 5% sobre o preço original do produto, {}, foi {} e o novo preço é {}'.format(product, descount, product_descounted))


