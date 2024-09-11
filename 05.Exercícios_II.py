#%%
#####1
import random
d6 = random.randint(1,6) # inclui ambos os valores
print (d6)

#%%
##### 2
import random
lista = range(1,100)
print(f"Meu número aleatório selecionado foi {random.choice(lista)}")

#%%
#####3
number=input("Por favor, digite um número inteiro")

if(int(number)%2>0):
    print ("O número digitado foi ímpar")

else:
    print ("O número digitado foi par")

#%%
#####4

number = 100

while(number>0):
    number-=1
    print (number)

print("Terminou")

#%%
######5
# Calcule a soma dos números de 1 a 100

lista = range(1,101)
soma = 0

for i in lista:
    soma +=i

print (soma)

# Outro método:

soma = sum(range(1, 101))

print(f"A soma dos números de 1 a 100 é: {soma}")

#%%
#####6

numero = int(input("Por favor, digite um número inteiro"))

# Exibe a tabuada usando um loop for
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#%%
######7
#Use um loop for e range e imprima todos os números pares de 1 a 100

for i in range(2,101,2):
    print(i)

#%%
#####8
#Use um loop for e range para somar todos os números
#ímpares de 1 a 300 e exiba a soma

for i in range(1,300,2):
    soma +=i

print (soma)

#%%
#####9

minhaLista = ["João", "Maria", "Ana"]

nomeParaChecar = input("Por favor, digite um nome")

if nomeParaChecar in minhaLista:
    print ("O nome está na lista")

else:
    print ("Nome não encontrado")

#%%
##### 10

# Define os dois primeiros números da sequência de Fibonacci

lista = [0,1]
# Exibe os primeiros 10 números da sequência
print("Os primeiros 10 números da sequência de Fibonacci são:")

contador=2
while contador<10:
    contador+=1
    numeroNovo = lista[-1] + lista[-2]
    lista.append(numeroNovo)

print(lista)


#%%
#####11
import random

d6 = random.randint(1,6) # inclui ambos os valores

while True:
    try:
        d6User = int(input("Por favor, digite um número inteiro: "))
        break  # Se o valor for válido, sair do loop
    except ValueError:
        print("Número inválido, tente novamente.")

print (f"O número do dado foi {d6}")

if d6==d6User:

    print(f"Parabéns você acertou")

else:
    print("Não foi dessa vez")

#%%
#####12

import time

number = 100

while(number>0):
    number-=1
    print (number)
    time.sleep(0.2)

print("Terminou")
