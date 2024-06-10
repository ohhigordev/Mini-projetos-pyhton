import random


print('-=-=-=-=-=-=-=-')
print('Seja muito bem vindo ao Guess Nuber do Higor!')
print('-=-=-=-=-=-=-=-\n')

# Pedindo ao usuário o maximo de números que podem ser randomizados:
num = int(input('Digite o teto do desafio: '))

# Criando uma variavel para randomizar os números:
random_num = random.randint(0,num)

print('Qual número você acha que o computador pensou?')
resposta = int(input('Resposta: '))

# Verificando se o usuário acertou ou não:
if resposta == random_num:
    print('PARABÉNS VOCÊ VENCEU!')
else:
    print(f'VOCÊ ERROU! Reposta correta: {random_num}')