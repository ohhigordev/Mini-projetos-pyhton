
lista = ([1, 2, 3, 4, 5, 6])
s1 = {1, 2, 3, 4, 5, 6}  # Automaticamente você mostra pro Python que isso é um set
s1.add(7)  # Adicona 1 item ao final do seu Set.

s1.update([8], [9], [10], [11])  # Adiciona mais de um item ao seu Set.

s1.remove(10)  # Remove o 10 do Set e gera um erro se o item que você remover não estiver no seu Set.

s1.discard(90)  # Diferente do remove ele não gera um erro se o item não estiver no Set.



print(s1)
