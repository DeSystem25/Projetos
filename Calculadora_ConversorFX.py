# Tabela de taxas de câmbio simuladas
taxas_cambio = {
    "USD": 5.10,  # Dólar
    "EUR": 6.00,  # Euro
    "GBP": 6.30,  # Libra
    "BRL": 1.00   # Real
}

# Função para converter moedas
def converter_moeda(valor, origem, destino):
    if origem in taxas_cambio and destino in taxas_cambio:
        taxa_origem = taxas_cambio[origem]
        taxa_destino = taxas_cambio[destino]
        
        valor_convertido = valor * (taxa_destino / taxa_origem)
        return valor_convertido
    else:
        return None

# Função principal
def iniciar_conversor():
    print("Bem-vindo ao Conversor de Câmbio!")

    while True:
        # Entrada do usuário
        origem = input("\nDigite a moeda de origem (USD, EUR, GBP, BRL): ").upper()
        destino = input("Digite a moeda de destino (USD, EUR, GBP, BRL): ").upper()
        try:
            valor = float(input("Digite o valor a ser convertido: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue

        # Conversão
        valor_convertido = converter_moeda(valor, origem, destino)

        # Exibição do resultado
        if valor_convertido is not None:
            print(f"\n{valor} {origem} é igual a {valor_convertido:.2f} {destino}.")
        else:
            print("\nMoeda não encontrada. Verifique se digitou corretamente (USD, EUR, GBP, BRL).")

        # Pergunta se quer continuar
        repetir = input("\nDeseja fazer outra conversão? (S/N): ").strip().lower()
        if repetir != "s":
            print("\nObrigado por usar o Conversor de Câmbio! Até a próxima.")
            break

# Executa o programa
iniciar_conversor()
