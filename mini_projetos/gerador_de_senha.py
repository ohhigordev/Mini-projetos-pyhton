import random
import string


def gerador_de_senhas(len_senha = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    senha_usuario = ''

    for i in range(0, len_senha):
        digit = random.choice(options)
        senha_usuario += digit

    return senha_usuario

resposta_usuario = input('Quantos digitos na senha? ')

# Verificando se o usuário digitou um dado compativel para o funcionamento do programa:
if resposta_usuario.isdigit():
    resposta_usuario = int(resposta_usuario)

else:
    print('Reposta invalida!')
    quit()

resposta = gerador_de_senhas(len_senha= resposta_usuario)
print(f'Senha gerada:\n{resposta}')


    