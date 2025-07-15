menu = '''
[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while(True):
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Insira o valor do depósito: "))
        if(valor > 0):
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação cancelada. O valor é inválido.")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Insira o valor a ser sacado: "))

        if(valor <= saldo):
            if(valor <= limite):
                if(numero_saques < LIMITE_SAQUES):
                    if(valor > 0):
                        saldo -= valor
                        numero_saques += 1
                        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                        extrato += f"Saque: R$ {valor:.2f}\n"
                    else:
                        print("Operação cancelada. O valor é inválido.")
                else:
                    print(f"Operação cancelada. O limite máximo de saques é {LIMITE_SAQUES}.")
            else:
                print(f"Operação cancelada. O valor é maior que o limite de R$ {limite:.2f}")
        else:
            print("Operação cancelada. O saldo é insuficiente.")


    elif opcao == "e":
        print("Extrato")
        print("\n======= EXTRATO =======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")