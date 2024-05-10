"""
Em python, 'list.index()' é um método usado para encontrar o índice de um determinado
elemnto de uma lista.Aqui está uma explicação detalhada:
"""
'''
list : Este é o nome da lista na qual você deseja encontar o índice do elemento.
index() : Este é o método que você chama na lista para encontrar o índice do elemento desejado. 
'''
'''
O método 'index()' eceita um argumento obrigatório, que é o elemento que você deseja localizar na lista.
Ele retorna o índice da primeira ocorrência desse elemento na lista.Se o elemento não estiver na lista,
o Python levantará uma excessão 'ValueErro'.
'''

lista = ['a', 'b', 'c', 'd', 'e']

# Encontrando o índice do elemento 'c' na lista:
index_of_c = lista.index('c')
print('Índice de "c" na lista:', index_of_c)

'''
Neste exemplo, o método 'index()' é chamado na lista 'lista' com o argumento 'c',
retornando o índice da primeira ocorrência do elemento 'c', que é 2.
'''
