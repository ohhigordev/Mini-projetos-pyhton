# Codigos de cores:
GREEN = "\033[32m"
RED = "\033[31m"

# Impotando sleep:
from time import sleep

# Criando a pontuação:
pontos = 0


print('=-=-=-=-=-=-=-=-')
print('Seja muito bem vindo ao quiz do Higor!')
print('=-=-=-=-=-=-=-=-\n')
pergunta = input('Quer começar? [S/N]').strip().upper()

if pergunta != 'S':
    quit()

print('Começando...')
print('[PRIMEIRA PERGUNTA]')
print('Quem desenvolvel o jogo Grand Theft Auto [GTA]\n [A] Rockstar Games\n [B]Ubisoft\n [C] Actvision\n [D]EA')
resposta1 = input('Resposta:').strip().upper()
print('Analizando...')
sleep(1)

if resposta1 == 'A':
    pontos += 1
    print('\033[32mResposta correta!\033[m')
else:
    print('\033[31mResposta incorreta!\033[m')



print('[SEGUNDA PERGUNTA]')
print('Qual foi o primeiro videogame criado e em que ano foi lançado?\n [A] Pong, 1972\n [B]Super Mario Bros., 1985\n [C]Tetris, 1984\n [D]Space Invaders, 1978')
resposta1 = input('Resposta:').strip().upper()
print('Analizando...')
sleep(1)

if resposta1 == 'A':
    pontos += 1
    print('\033[32mResposta correta!\033[m')
else:
    print('\033[31mResposta incorreta!\033[m')

print(f'Quiz acabou!... Pontução: {pontos}')



