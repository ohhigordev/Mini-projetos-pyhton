# Menu inicial
print('Olá, bem vindo ao seu banco!')
operacao = input('Deseja fazer uma operação: [S/N]').upper().strip()

while operacao == 'S':
    print('Escolha uma das opções abaixo: ')

    # Escolhas que o usuário pode fazer no banco
    menu = """
    [1] - Sacar
    [2] - Depositar
    [3] - Consultar extrato
    """
    print(menu)
    opcao = int(input('Qual operação você deseja fazer hoje: '))

    # Parametros
    saldo = 0
    limite_saque = 500
    numero_de_saques = 0
    extrato = ''
    LIMITE_SAQUES = 3

    # Saque
    while opcao == 1:
        print(f'Seu saldo é de R${saldo:.2f} .')
        saque = int(input('Quanto você deseja sacar: R$ '))
        if saque <= 500:
            exceceu_saldo = saque > saldo
            excedeu_limite = saque > limite_saque
            excedeu_saques = numero_de_saques > LIMITE_SAQUES
            if exceceu_saldo:
                print('Operação falhou! Não tem saldo suficiente!')
            elif excedeu_limite:
                print('Operação invalida! Não tem limite suficiente!')
            elif excedeu_saques:
                print('Operação invalida! Não pode mais realizar saques!')

        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            numero_de_saques += 1
        else:
            print('Operação falhou! O valor informado é invalido.')

    # Deposito
    while opcao == 2:
        deposito = int(input('Quanto você deseja depositar: R$'))
        if deposito > 0:
            saldo += deposito
            extrato += f'deposito: R$ {saldo:.2f}\n'
            print(f'Deposito realizado com sucesso! Seu novo saldo é de R${saldo:.2f} .')
            break
        else:
            print('Valor invalido! Tente novamente.')
        # Extrato
    if opcao == 3:
        print('\n======== EXTRATO ========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\n Saldo: R${saldo:.2f}\n')
        print('===========================')




    nova_operacao = input('Deseja fazer uma nova operação: [S/N]').upper().strip()
    if nova_operacao == 'S':
        continue
    else:
        break




print('Obrigado por ultilizar nosso banco!')
