
# List comprehension

"""
List comprehension em Python é uma forma consisa de criar listas.É uma maneira elegante e
eficiente de contruir uma lista aplicando uma expressão a cada item de um iterável e filtrando
os itens de acordo com a condição ,se necessário.
"""
'''
[exepressão for item in interável if condição]

Onde:
'expressão': é a expressão que será aplicada a cada item so iterável.

'item': é a variavel que representa cada elemento do iterável.

'iterável': é o iterável pelo o qual a lsit comprehension é iterada, como uma lista,
tupla, conjunto ou outra sequência.

'condição'(opicional): é uma condição que determina se o item será incluído na lista
restante ou não.Se a condição for verdadeira, o item será incluido. 
'''

numeros = [1, 2, 3, 4, 5, 6]
quadrados = [x ** 2 for x in numeros]

print(quadrados)  # Saida: [1, 4, 9, 16, 25, 36]

'''
    Neste exemplo, estamos criando uma lista chamada 'quadrados' que contém os quadrados 
de todos os números da lista 'numeros'.A expressão 'x ** 2' é aplicada a cada elemento 
'x' da lista 'numeros'.

    A list comprehension também pode ser incluida a cláusula 'if' para filtrar os itens.
Por exemplo:
'''

numeros1 = [1, 2, 3, 4, 5]
pares_quadrados = [x ** 2 for x in numeros1 if x % 2 == 0]

print(pares_quadrados)  # Saída [4, 16]
