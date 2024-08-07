# Este algoritmo ordena dois números

def obter_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))  # Tenta converter a entrada para float
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

# Solicita ao usuário para digitar dois números
a = obter_numero("Digite o número A: ")
b = obter_numero("Digite o número B: ")

# Compara os dois números e imprime o resultado
if a > b:
    print("A é maior que B")
elif a < b:
    print("B é maior que A")
else:
    print("A e B são iguais")
