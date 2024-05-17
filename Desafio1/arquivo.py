'''
    Autora: Leticia Resina
    Desafio: Sistema Bancário - Versão 1.0
'''

# Declarando as variáveis principais 

saldo = 0
LIMITE_SAQUE = 3 # constante -> por conveniência em python
limite_valor_saque = 500
saques_realizados = 0
extrato = ""

# Programa principal

print("Seja bem vindo(a) ao nosso Banco!")

# Looping infinito para deixar em aberto para quando o usuário desejar parar

while True:
    print("Como podemos te ajudar hoje?")
    print("\n1 - Depositar; \n2 - Sacar; \n3 - Extrato; \n4- Encerrar.")
    opcao = int(input("Digite a opção desejada (em números!): "))
    
    if opcao == 1:
        # opção de depósito
        valor_depositado = float(input("Informe o valor a ser depositado: "))
        if valor_depositado > 0:
            saldo += valor_depositado
            print(f"O valor atual em sua conta é de: R$ {saldo:.2f}")
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        else:
            print("Não é possível depositar valores negativos! Tente novamente.")

    if opcao == 2:
        # opção de saque
        if saques_realizados == LIMITE_SAQUE:
            print("Você já excedeu o limite de saques diários! Tente novamente amanhã!")
        else:
            valor_saque = float(input("Informe o valor a ser sacado: "))
            if valor_saque > limite_valor_saque:
                print(f"O valor informado ultrapassa seu valor de saque! Seu limite de valor é de R$ {limite_valor_saque}")
            elif valor_saque > saldo:
                print(f"O valor informado ultrapassa seu valor total da conta! Atualmente, seu valor é de R$ {saldo} ")
            elif valor_saque < 0:
                print("Não é possível realizar saque de valores negativos! Tente novamente!")
            else:
                saldo -= valor_saque
                print(f"Saque realizado no valor de R$ {valor_saque:.2f}.")
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                saques_realizados += 1
    
    if opcao == 3:
        # opção de extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    if opcao == 4:
        # opção de encerrar
        print("Obrigada por utilizar nosso Banco! É um prazer te ter como nosso cliente! :)")
        break