
"""O método 'remove()' em Python é usado para remover o primeiro elemento na lista
que corresponde a um valor especifico.Sua sintaxe é:
list.remove(valor)"""
'''Onde 'valor' é o elemnto que você deseja remover da lista.'''

lista = [1, 2, 3, 4, 3, 5, 6, 3]
'''index 0  1  2  3  4  5  6  7'''

# Remover um valor da lista acima:
lista.remove(3)
print(lista)

'''
No exemplo acima foi pedido para ser retirado um número repitido presente na lista
sendo assim o Python tirou o primero '3' que apareceu na lista.

'''

lista1 = [1, 2, 3, 4, 5]

# tente remover o número '6' da lista:
try:
    lista1.remove(6)
except ValueError:
    print('O valor execificado não está presente na lista.')
print(lista1)

'''
Neste caso o valor '6' não está presente na lista gerando a excessão 'ValueError'.
O programa trata da excessão e imprime uma mensagem indicando que o valor especificado
não está presente na lista.A lista permenece inalterada.
'''