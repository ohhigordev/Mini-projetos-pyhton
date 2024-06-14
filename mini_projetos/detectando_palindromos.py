# Vamos primeiro criar uma função interativa:
def is_palindrome(word):
    j = len(word)-1 
    for i in range(len(word)):
        if word[i] == word[j]:# Aqui nos precisamos saber se a primeira letra é igual a última.
             result = result + 1