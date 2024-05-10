""" Em python, list.count(x) é um metodo ultilizado para contar o número de ocorrências
de um elemento em uma lista.A sintaxe básica é a seguinte."""
'''
lista.count(elemento)
'''
'''
Onde 'lista' é a lista na qual você quer contar as ocorrências e 'elemento' é o valor cujas
ocorrências você deseja contar.
'''

lista = [1, 2, 3, 1, 1, 4, 5, 6, 1]

contagem = lista.count(1)
print(contagem)

'''
É importante notar que o método 'count' só conta as ocorrências exatas do elemento da lista.
Se você quiser contar as ocorrências de elementos que são listas ou tuplas, você precisa fazer
isso de forma separada.O método 'count' só conta as ocorrencias do elemento fornecido  diretamentre na lista,
não em elementos aninhados detro de outras estruturas de dados.
'''
