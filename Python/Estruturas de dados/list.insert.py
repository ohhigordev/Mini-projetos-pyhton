
# O metodo `insert()` em Python é usado para inserir um elemento em um posição especifica em uma lista.
# sintaxe:
""" lista.insert(posição, elemento)"""

# Posição = é a posição na lista onde o elemento será inserido.
# elemento = é o elemento que será inserido na lista.

lista = [1, 2, 3, 4, 5]
'''index 0  1  2  3  4 '''
print(lista)


# Inserir o número 10 na posição 2.
lista.insert(2, 10)
print(lista)
'''
Nesse exemplo o número '10' foi inserido na posição '2' da lista, deslocando os elementos
subsequentes para a direita.
'''

# Inserindo o elemento no final da lista.
lista2 = [1, 2, 3]
''' index 0  1  3'''
print(lista2)


# Inserir o número 4 na posição 10.
lista2.insert(10, 4)
print(lista2)

'''
Nesse exemplo o objeto ficou no final da lista pois a sua posição era maior que 
o número total de index da lista.
'''

