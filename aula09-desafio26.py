frase = str(input('Digite uma frase: '))

frase_upper = frase.upper()
amount = frase_upper.count('A')

find_result = frase_upper.find('A')



print('A quantidade de A que tem na frase é {}'.format(amount))
print('O primeira A aparece na posição {}'.format(find_result))  #Nesse caso o find mostra somente a posição da primeira letra encontrada"i
print('A ultima ocorrencia de A aparece na posição {}'.format(frase_upper.rfind('A')))
