"""Em python, o método 'list.copy()' é ultilizado para criar uma cópia superficial (shallow copy)
de uma lista.Uma cópia superficial cria um novo objeto lista,mas os elementos dentro da lista são
referenciados pelo memos objetivos  que estão na lista original.Isso significa que se os elementos
na lista original forem mutáveis( por exemplo, lista aninhadas, dicionários, etc.) as alterações nesses
elementos reflitarão tanto na lista original quanto na cópia."""

'''
SINTEXE:
copia_lista = lista_original.copy()
'''

lista_original = [1, 2, 3, 4, 5]
copia_da_lista = lista_original.copy()
'''
Agora 'copia_da_lista' é uma cópia de 'lista_original', contendo os mesmo elementos.Porém, é importante notar
que 'copia_da_lista' e 'lista_original' refrenciam objetos diferentes no espaço da memória.Portanto,se você
modificar os elementos dentro de uma lista, as alterações não afetarm a outra lista.
'''
copia_da_lista[0] = 5  # '0' é posição do index e '5' é elemento que deve ser trocado com base na posição.
print(copia_da_lista)
print(lista_original)

'''
Aqui apenas a 'copia_da_lista' foi modificada.A 'lista_original' permaneceu inalterada.Por outro lado, se os
elementos nessa lista forem multáveis,as alterações nesses elementos serão feitos tanto na lista orginal
quanto na sua cópia. 
'''
lista1 = [[1], [2], [3]]
lista1_copia = lista1.copy()

lista1_copia[0][0] = 5
print(lista1)
print(lista1_copia)

'''
Aqui, a modificação do elemento '[1]' dentro da 'lista1_copia' também altera o elemento correspondente na 
'lista1'.Isso ocorre porque ambas as listas estão compartilhando referências para os mesmos objetos.
'''
