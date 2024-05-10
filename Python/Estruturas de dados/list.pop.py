""" em Python, 'list.pop[i]' é um método ultilizado para remover e retornar um elemento
 de um alista em determinada posição. Aqui está uma explicação mais detalhada:"""

'''
list : Este é o nome da lista a qual você deseja remover um elemento.
pop : É o metodo utilizado para remover o elemento.Quando você chama 'list.pop()', o último
elemento da lista é removido e retornado. Se você especificar um indice entre parêntese, como
'list.pop(i)', o elemento na posição 'i' é removido e retornado.
[i] : é um parametro opcional.Se você fornecer um valor i, 
isso indicará a posição na lista do elemento que você deseja remover. 
Se você não fornecer um valor, o método pop() removerá e retornará o último elemento da lista.
'''

my_list = [1, 2, 3, 4, 5]

# removendo e retornando o elemento na posição 2
element_remove = my_list.pop(3)
print('Elemento removido:', element_remove)
print('Lista após a remoção:', my_list)

'''
Neste exemplo, o elemento na posição 2( que é o número 3) é removido da lista e atribuido à variavel 
'element.remove'. Em seguida, a lista é impressa após a remoção.
'''
