from time import sleep

# Pedindo o tempo ao usuário:
t = input('Digite o tempo (em segundos): ')

# Verificando se o que o usuário digitou é realmente um número:
if t.isdigit():
    t = int(t) # Tranformando ele em inteiro!
else:
    print('Entrada invalida!')
    quit()

while t != 0:
    # Chamando a divmod para separarmos os minutos dos segundos:
    minutos, segundos = divmod(t, 60)
    tempo = '{:02d}:{:02d}'.format(minutos, segundos) # 0: considera '0' a esquerda, 2: Quer dois números, d: Números inteiros
    sleep(1)
    t -= 1

    # Vamos imprimir o nosso timer mais sobrescrevendo as strings:
    print(tempo, end='\r')

print('Tempo acabou!')

