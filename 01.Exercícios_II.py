
######5

soma = 0

for i in range(1, 11):  # Loop de 1 a 10 (incluindo 10)
    soma += i  # Adiciona o valor de i à soma

print(soma)  # Imprime o resultado final


######4

import time

# Contagem regressiva de 10 a 1
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # Pausa de 1 segundo entre cada número

print("Fim da contagem regressiva!")


######3

# Solicita ao usuário para inserir três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Encontra o maior número usando estruturas condicionais
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# Exibe o maior número
print("O maior número é:", maior)


######2

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

######1
import random

# Simula o lançamento de um dado d6
dado = random.randint(1, 6)

# Exibe o resultado
print("Você rolou um dado e o resultado foi:", dado)
