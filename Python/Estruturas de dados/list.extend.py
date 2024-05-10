

# Criando duas litas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
'''Mesmo colocando números tudo que entra em uma lista é uma str. '''

# Usando o extend para adicionar os elementos da lista 2 ao final da lista1
lista1.extend(lista2)

print(lista1)

'''
Com essa propriedade alteramos apenas a lista1 adicionando a ela os dados da lista2,
porém a lista2 permaneceu inalterada.
'''

# list.extend em lista + tupla
lista = [1, 2, 3]
tupla = (4, 5, 6)

# Usando o extend com a tupla
lista.extend(tupla)

print(lista)

'''
Não é possival fazer o contrario pois as TUPLAS não tem a propriedade '.extend'.
'''
