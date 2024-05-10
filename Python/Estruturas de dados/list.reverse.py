"""Em Python, método list.reverse() é ultilizado para inverter a ordem dos elementos em uma lista.
Ele altera a lista original, modificando-a para que seus elementos fiquem em ordem inversa. """


'''
SINTAXE:
list.reverse()
'''
# lista na ordem normal.
lista = [1, 2, 3, 4, 5]
print(lista)

# lista invertida sem o uso de uma variavel.
lista1 = [1, 2, 3, 4, 5]
lista1.reverse()
print(lista1)

'''
É importante notar que o método 'list.reverse()' modifica a lista original e não retorna uma 
nova lista invertida.Se você precisar de uma cópia invertida da lista sem modificar a original,
pode criar uma cópia da lista e então reverter essa cópia, como por exemplo:
'''

# Lista invertida com o uso de variavel.
lista = [1, 2, 3, 4, 5]
copia_invertida = lista[::-1]
print(copia_invertida)


