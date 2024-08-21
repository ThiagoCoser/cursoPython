# Este algoritmo ordena dois números

# Solicita ao usuário para digitar dois números
a = float(input("Digite o número A: "))  # Converte a entrada para float
b = float(input("Digite o número B: "))  # Converte a entrada para float

if a > b:
    print("A é maior que B")
elif a < b:
    print("B é maior que A")
else:
    print("A e B são iguais")
