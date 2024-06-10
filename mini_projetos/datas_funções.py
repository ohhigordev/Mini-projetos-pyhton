from função import *


print('=====================')
print('Qual a data de vencimento')
print('=====================\n')
print('Use o formato dd-mm-aaaa')
due_data = input('')

if len(due_data) == 10:
    print(verify_due(due_data))

else:
    print('Entrada invalida!')

