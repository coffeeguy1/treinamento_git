import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

"""
    Nesse caso o random.choice aceita que você ponha uma lista como ([n1,n2,n3,n4]) ou uma variavel com a lista dentro
"""

print('O aluno escolhido foi {}'.format(escolhido))
