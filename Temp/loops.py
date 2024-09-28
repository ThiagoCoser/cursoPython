#%%
import time

tempo = 10

while (tempo>0):
    tempo-=1
    print(tempo)
    time.sleep(1)

print ("Terminou")


#%%
nome = ""

while (nome != "seu nome"):
    print("Por favor, digite seu nome")
    nome = input()

print("Obrigado!")

#%%

for i in range(0, 10, 2):
    print(i)


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
