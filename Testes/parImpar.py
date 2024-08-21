#%%
# Usando o operador módulo
numero = input("Digite um numero inteiro")

if int(numero) % 2 == 0:

    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")


#%%
# Outra solução
numero = input("Digite um número: ")

numeroMetade = float(numero)/2

if numeroMetade.is_integer():  # Verifica se a divisão por 2 é exata
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")



# %%
# Outra solução, com checagem de erro de digitação
while True:
    numero = input("Digite um número: ")

    try:
        numeroMetade = float(numero) / 2

        if numeroMetade.is_integer():  # Verifica se a divisão por 2 é exata
            print(f"{numero} é par")
        else:
            print(f"{numero} é ímpar")
        break  # Sai do loop se a operação for bem-sucedida

    except ValueError:
        print("Erro: O valor digitado não é um número válido. Tente novamente.")

# %%
