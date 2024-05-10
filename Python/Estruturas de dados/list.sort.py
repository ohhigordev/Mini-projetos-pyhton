"""list.sort()"""
'''
Em Python, 'list.sort()' é metodo ultilizado para ordenar os elementos de uma lista em ordem crescente
ou decrescente.Este método modifica a própria lista, reorganizando os elementos com base em uma função de
comparação. 
'''
'''
SINTAXE:
list.sorte(key = None, Reverse = False)
'''

'''
key: é um parametro opcional que especifica uma funcção de chave para ser aplicada a cada elemento antes
de fazer a comparação.Se não for fornecido, os elementos serão comparados diretamente.

Reverse: é um parametro opcional que especifica se a lista deve ser ordenada  em decrescente ('True') ou não
('False').O valor padrão é 'False', ou seja, a lista será ordenada em ordem crescente.
'''

lista = [1, 5, 9, 3, 10, 2, 4, 8, 0]

# Ordenar a lista em ordem CRESCENTE.
lista.sort()
print(lista)

# Ordenar a lista em ordem DECRESCENTE.
lista.sort(reverse=True)
print(lista)

'''
Se quisermos ordenar uma lista com base em uma função  de chave, podemos passar a função com o argumento
'Key'.Por exemplo, para ordernar a lista a com base na distância dos elementos do número '4', podemos fazer
o seguinte.
'''
lista1 = [5, 3, 6, 9]


def chave_de_ordem(lista1):
    return abs(lista1 - 4)


lista1.sort(key=chave_de_ordem(lista1))
print(lista1)
#NAOOOOOOOOOOOOOOOO SEI FAZER.
