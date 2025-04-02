menu = """
================ MENU DE OPERAÇÕES ================

[A] Depósito
[B] Saque
[C] Extrato
[D] Encerrar

===================================================

""" "Digite uma opção: " 

saldo = 200
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3

while True:

    opcao = input(menu)

    if opcao == "A":
        valor = float(input("Digite o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            
        else:
            print("A operação falhou! O valor informado é inválido.")
    
    elif opcao == "B":
        valor = float(input("Digite o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")

        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
    
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
    
        elif numero_de_saques >= limite_de_saques:
            print("Operação falhou! Você excedeu a quantidade máxima de saques.")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "C":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "D":
        print()
        print("Obrigado por ser nosso cliente! Tenho um ótimo dia!")
        break


    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        

    

