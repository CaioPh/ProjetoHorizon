#Horizon Bank - Sistema de Atendimento Terminal
#Sa2 - Situação de Aprendizagem

import datetime
import random  #random é utilizada para gerar automaticamente o número da conta.

clientes = [
    ["11111111111", "José da Silva", 1500.0],
    ["22222222222", "Maria da silva", 350.0]
]

# Dicionário para armazenar dados extras da conta
contas = {
    "11111111111": {"agencia": 1001, "numero": random.randint(10000, 99999)},
    "22222222222": {"agencia": 1001, "numero": random.randint(10000, 99999)}
}

def exibicao_banner():
    print("====================================================")
    print("                \033[32m HORIZON BANK \033[0m       ")
    print(" Um banco que está com você em todos os momentos.")
    print("====================================================")

def exibicao_rodape():
    print("====================================================")
    print(" Horizon Bank 2026 | Transparencia | Carreira | SAC 0800 3132 0080 ")
    print("====================================================")

def abrir_conta():
    print("\n--- ABRIR CONTA ---")
    cpf = input("Digite seu CPF: ")

    if len(cpf) == 11:
        nome = input("Digite seu nome: ")

        clientes.append([cpf, nome, 0.0])

        contas[cpf] = {
            "agencia": 1001,
            "numero": random.randint(10000, 99999)
        }

        print(f"[✓] Conta criada para {nome}!")

    else:
        print("[!] CPF invalido")

def mostrar_saldo(cliente):
    cpf = cliente[0]

    print(f"\n========================================")
    print(f" Bem-vindo(a), {cliente[1]}!")
    print(f" Agência: {contas[cpf]['agencia']}")
    print(f" Conta: {contas[cpf]['numero']}")
    print(f" Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f" SEU SALDO ATUAL: R$ {cliente[2]:.2f}")
    print(f"========================================")

    print("1 - Fazer um Depósito\n2 - Voltar ao Menu")
    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: R$ "))
        cliente[2] += valor
        print(f"[✓] Depósito realizado com sucesso! Novo saldo: R$ {cliente[2]:.2f}")

def menu_principal():
    while True:
        exibicao_banner()
        print("1 - Acessar Conta (Login por CPF)")
        print("2 - Abrir Nova Conta")
        print("3 - Sair")
        exibicao_rodape()

        opcao = input("Opção: ")

        if opcao == "1":
            cpf = input("Digite seu CPF: ")

            encontrado = None

            for c in clientes:
                if c[0] == cpf:
                    encontrado = c

            if encontrado:
                mostrar_saldo(encontrado)
            else:
                print("[!] CPF não encontrado.")

        elif opcao == "2":
            abrir_conta()

        elif opcao == "3":
            print("Até logo!")
            break

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    menu_principal()