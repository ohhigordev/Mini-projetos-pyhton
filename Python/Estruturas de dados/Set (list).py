"""
Set (Listas)
    # Similar a listas
    # Evitar itens duplicados
    # Não ultilizar index
"""
lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

num1 = set(lista1)
num2 = set(lista2)

print(num1)
print(num1 | num2)  # Union: ele unifica as duas listas retirando os valores repetidos.
print(num1 - num2)  # Difference: ele mostra todos os números que tem na lista1 que não tem na lista2.
print(num1 ^ num2)  # Symmtric Difference: ele mostra todos os valores das listas que não estão repetidos.
print(num1 & num2)  # And: Mostra os elementos que estão repetidos nas duas listas
print(len(num1))  # Tamanho da lista
