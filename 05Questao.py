import random

def gerador_senha():
    # Definição de caracteres
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    caracteres_especiais = "!@#$%^&*()_+"
    
    # Senha inicial
    senha_inicial = ""
    
    # Função para validar entradas S/N
    def validar_entrada(mensagem):
        while True:
            resposta = input(mensagem).strip().upper()
            if resposta in ["S", "N"]:
                return resposta == "S"
            print("Entrada inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
    
    # Loop para garantir uma entrada numérica válida para o tamanho da senha
    while True:
        try:
            num_caracteres = int(input("Quantos caracteres a senha deve ter? "))
            if num_caracteres > 0:
                break
            else:
                print("O número de caracteres deve ser maior que zero!")
        except ValueError:
            print("Entrada inválida! Você deve digitar um número inteiro.")
    
    # Loop para garantir que pelo menos uma categoria seja escolhida
    while not senha_inicial:
        print("Você precisa selecionar pelo menos uma categoria de caracteres!")
        incluir_maiusculas = validar_entrada("Incluir letras maiúsculas? (S/N): ")
        incluir_minusculas = validar_entrada("Incluir letras minúsculas? (S/N): ")
        incluir_numeros = validar_entrada("Incluir números? (S/N): ")
        incluir_especiais = validar_entrada("Incluir caracteres especiais? (S/N): ")
        
        # Construção do pool de caracteres
        if incluir_maiusculas:
            senha_inicial += letras_maiusculas
        if incluir_minusculas:
            senha_inicial += letras_minusculas
        if incluir_numeros:
            senha_inicial += numeros
        if incluir_especiais:
            senha_inicial += caracteres_especiais

    # Gerar senha
    senha = "".join(random.choice(senha_inicial) for _ in range(num_caracteres))
    print(f"Sua senha gerada é: {senha}")

# Chamada da função
gerador_senha()
