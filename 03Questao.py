def input_texto(mensagem):
    while True:
        texto = input(mensagem)
        if texto.isalpha():  # Verifica se contém apenas letras
            return texto
        else:
            print("Entrada inválida. Por favor, digite apenas texto (letras).")


def input_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            if numero >= 0:  # Verifica se o número é não-negativo
                return numero
            else:
                print("Entrada inválida. Por favor, digite um número não-negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")


saldo_individual = {}
fim = True

while fim:
    print("\nMenu:")
    print("1. DEPOSITAR")
    print("2. SACAR")
    print("3. VER SALDO")
    print("4. ENCERRAR")
    escolha = input("Escolha uma opção: ")

    match escolha:
        case '1':  # Depositar
            identidade = input_texto("Qual usuário que irá depositar? ")
            valor = input_numero("Digite o VALOR a ser depositado: ")
            saldo_individual[identidade] = saldo_individual.get(identidade, 0) + valor
            print(f"Saldo atualizado: {saldo_individual}")
        case '2':  # Sacar
            identidade = input_texto("Qual usuário que irá sacar? ")
            if identidade not in saldo_individual:
                print("Nenhum usuário cadastrado.")
                continue
            valor = input_numero("Digite o valor a ser sacado: ")
            if valor > saldo_individual.get(identidade, 0):
                print("Saldo não disponível, sugiro depositar.")
            else:
                saldo_individual[identidade] -= valor
            print(f"Saldo atualizado: {saldo_individual}")
        case '3':  # Ver saldo
            identidade = input_texto("Qual usuário que irá ver o saldo? ")
            if identidade not in saldo_individual:
                print("Nenhum usuário cadastrado.")
                continue
            print(f"Saldo de {identidade}: {saldo_individual[identidade]}")
        case '4':  # Encerrar
            fim = False
            print("Programa encerrado.")
        case _:  # Opção inválida
            print("ESCOLHA UMA OPÇÃO VÁLIDA")
