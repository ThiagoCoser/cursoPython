#%%
#1
nome = input("Input nome")
idade=input("Input idade")
altura = input("Altura")

print(f"Olá{nome}. Sua idade é{idade} e sua altura é {altura}")

#%%
#2
nota1 = float(input("Nota1"))
nota2 = float(input("Nota2"))
nota3 = float(input("Nota3"))
nota4 = float(input("Nota4"))

media = nota1+nota2+nota3+nota4

if media>=7:
    print(f"Aprovado com média{media/4}")

else:
    print(f"Não aprovado com média{media/4}")

#2 Extra, refinando

notas = []

while len(notas)<4:
    notaNumero=1
    nota=float(input(f"Digite a nota{notaNumero}"))

    try:
      notas.append(float(nota))
      notaNumero+=1

    except ValueError:
        print("Valor incorreto, tente novamente")

media = sum(notas)/len(notas)

if media>=7:
    print(f"Aprovado com média{media}")

else:
    print(f"Não aprovado com média{media}")

#%%
#3

import time

contador = 10

while contador>0:
    contador-=1
    time.sleep(1)
    print(contador)

print("Terminou")

#%%
#4
mensagem = "SEU NOME"
mensagemDigitada=""

while True:
   mensagemDigitada = input("Digite seu nome")
   if mensagemDigitada.lower()==mensagem or mensagemDigitada.upper()==mensagem:
      break

print("Obrigado!")
#%%
#5
import random

numeroUser = 0
d6=0


def checaNumero():
    d6 = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6
    return d6

while True:

    try:
        numeroUser = int(input("Digite um número de 1 a 6"))
        d6= checaNumero()

        if numeroUser==d6:
            break
        else:
            print(f"Seu número {numeroUser} não é igual ao dado {d6} sorteado. Tente outra vez")
            continue

    except ValueError:
        continue

print(f"Seu número {numeroUser} é igual ao dado {d6} sorteado. Parabéns!")
