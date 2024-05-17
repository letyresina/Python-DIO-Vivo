'''
    Autora: Leticia Resina
    Desafio: Sistema Bancário - Versão 1.0
'''

# Declarando as variáveis principais 

saldo = 0
LIMITE_SAQUE = 3 # constante -> por conveniência em python
limite_valor = 500
saques_realizados = 0

# Programa principal

print("Seja bem vindo(a) ao nosso Banco!")

# Looping infinito para deixar em aberto para quando o usuário desejar parar

while True:
    print("Como podemos te ajudar hoje?")
    print("\n1 - Depositar; \n2 - Sacar; \n3 - Extrato; \n4- Encerrar.")
    opcao = int(input("Digite a opção desejada (em números!): "))
    
    if opcao == 1:
        # opção de depósito
        valor_depositado = float(input("Digite o valor a ser depositado: "))
        if valor_depositado > 0:
            saldo += valor_depositado
            print(f"O valor atual em sua conta é de: R$ {saldo:.2f}")
        else:
            print("Não é possível depositar valores negativos! Tente novamente")

    if opcao == 2:
        # opção de saque
        print("Em construção...")

    if opcao == 3:
        # opção de extrato
        print("Em construção...")

    if opcao == 4:
        # opção de encerrar
        print("Obrigada por utilizar nosso Banco! É um prazer te ter como nosso cliente! :)")
        break