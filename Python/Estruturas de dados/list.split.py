"""
A função '.split()' em Python é ultilizada para dividir uma string em uma lista de substrings, ultilizando
um caractere ou sequência de caracteres especifica como delimitador.Aqui está a sintaxe básica:
"""
'''
string.split(separador, maxsplit)
'''

'''
=> 'string': A String que você deseja dividir.
=> 'separador': (opcional) O caractere ou sequência  de caracteres pelos quais a string será dividida.
Se este argumento for omitido, os espaços em branco(espaços, tabulação, quebra de linha, etc.) serão usados
como separadores.
=> 'maxsplit'(opicional):O número máximo de divisões a serem realizadas.Se fornecido, a string será dividida
no máximo 'maxsplit' vezes.O restante da string não será dividido.Se este argumento for omitido ou negativo,
não há limite no número de divisões.
'''


#  Exemplo:
frase = 'Olá, mundo! Bem-vindo a programação.'
palavras = frase.split()  # dividir a frase por espaços em branco.
print(palavras)
'''
# Saida: ['Olá', 'mundo!','Bem-vindo', 'à', 'programação.'] 
'''


texto = 'banana,maçã,morango,uva'
frutas = texto.split(',')  # dividir o texto por virgulas
print(frutas)
'''
Saida: ['banana', 'maçã', 'morango', 'uva']
'''
