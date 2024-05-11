menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500.00
extrato = "\nEXTRATO:\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Quanto você quer depositar? '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: + R$ {valor:.2f}\n'
        else:
            print('Apenas valores positivos!')

    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diário atingido! Tente novamente amanhã.')
        else:
            valor = float(input('Quanto você quer sacar?'))
            if valor > limite:
                print(f'Valor inválido, o limite de saque é de R$ {limite:.2f}')
            elif saldo-valor < 0:
                print(f'Você não possui saldo o suficiente. Seu saldo é de R$ {saldo:.2f}')
            elif valor <= 0:
                print(f'Valor inválido, o saque deve ser maior que R$ 0.00')
            else:
                saldo -= valor
                numero_saques+=1
                extrato += f'Saque: - R$ {valor:.2f}\n'
                print('Operação concluída!')

    elif opcao == 'e':
        print(extrato)
        print(f'Saldo Final = R$ {saldo:.2f}:')
    elif opcao == 'q':
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")