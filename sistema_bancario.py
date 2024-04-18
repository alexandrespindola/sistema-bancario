saldo = 1000
extrato = []
limite = 500
LIMITE_SAQUES = 3

def dados_extrato(extrato):
    return '\n'.join("R$ " + str(item) for item in extrato)

def mensagem(saldo, extrato):
    return f'''
##### Extrato #####
Saldo: {saldo}
Extrato: \n{dados_extrato(extrato)}
'''

print(f'\nSALDO INICIAL: {saldo}\n')

menu = '''1. Depósito
2. Saque
3. Extrato
4. Sair'''

numero_saques = 0

while (True):
    print(menu)
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        while True:
            deposito = int(input("Valor do depósito: "))
            if deposito > 0:
                break
            else:
                print("\nValor inválido. Por favor, deposite um valor positivo.")
        extrato.append(deposito)
        saldo += deposito
        print(mensagem(saldo, extrato))
    elif opcao == 2:
        saque = int(input("\nValor do saque: "))
        if saldo >= saque and numero_saques < LIMITE_SAQUES and saque <= limite:    
            extrato.append(saque * -1)
            saldo -= saque
            numero_saques += 1
            print(mensagem(saldo, extrato))
        elif saldo < saque:
            print("\nSaldo insuficiente para esta operação.\n")
        elif saque > limite:
            print("\nO valor máximo disponível para saque é de R$500.\n")          
        else:
            print("\nVocê excedeu o número de 3 saques diários.\n")
    elif opcao == 3:
        print(mensagem(saldo, extrato))
    elif opcao == 4:
        print("\nSaindo... Obrigado!")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")

