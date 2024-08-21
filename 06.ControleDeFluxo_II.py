#%%
# Este algoritmo cria uma contagem regressiva
import time

tempo = 1

while (tempo>0):
    tempo-=1
    print(tempo)
    time.sleep(1)

print ("Terminou")


#%%
# Pequeno Puzzle
nome = ""

while (nome != "seu nome"):
    print("Por favor, digite seu nome")
    nome = input()

print("Obrigado!")


#%%
# Este algoritmo ordena dois números
# com checagem de erro de exceção

def obter_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))  # Tenta converter a entrada para int
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

# Solicita ao usuário para digitar dois números
a = obter_numero("Digite o número inteiro A: ")
b = obter_numero("Digite o número inteiro B: ")

# Compara os dois números e imprime o resultado
if a > b:
    print("A é maior que B")
elif a < b:
    print("B é maior que A")
else:
    print("A e B são iguais")


#%%
# Cria números aleatórios com a função range
for i in range(0, 10, 2):
    print(i)


#%%
for i in [0, 1, 2, 5]:
    if i == 5:
        print(i)


idades = [0,2,4,8]

if 8 in idades:
    print("encontrei")


# %%

nome = input("Digite seu nome ")
eco= input("Digite o valor do eco ")

for i in range(int(eco)):
    print(nome + str(i))


# %%


nome = input("Digite seu nome: ")
ultimas_duas_letras = nome[-2:]  # Pega as duas últimas letras da string

print(nome, end="")
for i in range(10):

    print(ultimas_duas_letras, end="")

#print("As duas últimas letras são:", ultimas_duas_letras)
# %%
