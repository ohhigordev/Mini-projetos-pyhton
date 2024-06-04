from time import sleep

# Primeira vamos importar a bibioteca random para criarmos um sistema de randomização
import random

# Agora vamos criar a pontuação do jogador e do computador:
pontos_jogador = 0
pontos_computador = 0

opções = ['R', 'T', 'P']

# Vamos criar um While Loop para que o jogo fique sempre se repetindo até o usuário não querer mais jogar:
while True:
    escolha_usuário = input('Escolha R[Pedra]/T[Tesoura]/P[Papel] ou Q para sair.\nEscolha: ').strip().upper()
    print('Verificando...\n')
    sleep(1)

    if escolha_usuário == 'Q':
        break # Usuário não quer mais jogar e o loop acaba.

    # Verificando se o que o usuário digitou corresponde as opções do programa:
    if escolha_usuário not in opções:
        continue # Usando o continue ele vai ignonar as verificações e vai executar o While True novamente! 

    # Vamos fazer a randomização do computador:
    escolha_computador = random.randint(0,2)
    # 0 = R, 1 = T, 2 = P
    escolha_computador = opções[escolha_computador]
    print('===============')
    print('O computador escolheu ' + escolha_computador)

    # Vamos criar o sistema de pontuação:
    if escolha_usuário == escolha_computador:
        print('Empate!')
        print('===============')

    elif escolha_usuário == 'R' and escolha_computador == 'T':
        print('Você ganhou!')
        print('===============')
        pontos_jogador += 1

    elif escolha_usuário == 'P' and escolha_computador == 'R':
        print('Você ganhou!')
        print('===============')
        pontos_jogador += 1

    elif escolha_usuário == 'T' and escolha_computador == 'P':
        print('Você ganhou!')
        print('===============')
        pontos_jogador += 1

    else:
        print('Computador ganhou!')
        print('===============')
        pontos_computador +=1

# Vamos verificar as pontuações:
print('======== PONTUAÇÃO =======\n')
sleep(1)
print(f'Sua pontuação: {pontos_jogador}')
sleep(1)
print(f'Pontuação do computador: {pontos_computador}')
print('===============\n')
sleep(1)

# Verificando quem ganhou:
if pontos_computador > pontos_jogador:
    print('O computador venceu!')
elif pontos_jogador == pontos_computador:
    print('Empate!')
else:
    print('Derrota!')

sleep(2)

print('Programa acabou...')



