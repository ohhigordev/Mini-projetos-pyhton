"""
Em uma loja de tintas temos 4 cores em estoque, como verificar se o cliente fez o pedido de
uma cor e essa cor bate com as cores que estão no estoque da loja.
"""
cliente = input('Olá, qual cor você deseja:').strip().lower()

cores = ['amarelo', 'verde', 'azul', 'vermelho']

'''
FORMA BURRA DE FAZER!
if cliente == 'amarelo':
    print('Sim, temos essa cor.')
elif cliente == 'verde':
    print('Sim, temos essa cor.')
elif cliente == 'azul':
    print('Sim, temos essa cor.')
elif cliente == 'vermelho':
    print('Sim, temos essa cor.')
else:
    print('Infelizmente não temos essa cor.')
    '''


if cliente in cores:
    print('Sim, temos está cor em estoque.')
else:
    print('Desculpe, mas não temos essa cor.')
