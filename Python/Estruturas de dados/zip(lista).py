# função zip
"""
Em python, 'zip' é um função embutida que permite combinar interáveis, como listas, tuplas ou outros
tipos de sequências, em pares ordenados.Isso significa que ela agrupa os elementos correspondentes do mesmo
índice que várias sequências em tuplas.Aqui está um exemplo básico de como você pode usar o 'zip':
"""

#  exemplo:
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

# Usando zip para combinar as listas
resultado = zip(lista1, lista2)  # Criando o zip
resultado_lista = list(resultado)  # Converteu o zip em uma lista novamente
print(resultado_lista)

'''
Neste exemplo,'zip' combina os elementos correspondentes das duas listas('lista1' e 'lista2') e cria uma lista
de tuplas, onde o primeiro elemento  de cada tupla é da 'lista1' e o segundo é da 'lista2', mantendo a ordem
dos elementos.
'''
