salary = float(input('Digite o seu salário: '))

if salary >= 1250.00:
    print('O seu novo salário com aumento de 10% é: {}'.format(salary + (salary*(10/100))))
elif salary < 1250.00:
    print('O seu novo salário com aumento de 15% é: {}'.format(salary + (salary*(15/100))))
