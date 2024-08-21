#%%
import random

def funcaoPrincipal():

    numeroJogador = input("Digite um número")
    d6 = random.randint(1,6)

    print("o numero sorteado foi", d6)

    if (d6==int(numeroJogador)):
        print("Venceu")
    else:
        funcaoPrincipal()


funcaoPrincipal()

#%%

import random

while True:
    try:
        numeroDoJogador = int(input("Digite um número entre 1 e 6: "))
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue  # Volta ao início do loop

    d6 = random.randint(1, 6)
    print("O número sorteado foi", d6)

    if d6 == numeroDoJogador:
        print("Venceu")
        break  # Sai do loop se o jogador vencer
    else:
        print("Tente novamente.")


# %%

import random

# Cria uma lista de números de 0 a 200
numeros = list(range(0, 201))

# Escolhe um número aleatório da lista
numero_aleatorio = random.choice(numeros)
print(numero_aleatorio)

# %%
