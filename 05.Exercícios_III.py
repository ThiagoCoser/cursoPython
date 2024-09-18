#%%
#####1
# Crie um script ScriptA.py
# Crie um script ScriptB.py
# No script A, crie uma função ex:

def somaNumeros(a,b):
    c=a+b
    print(c)

# No scripitB, importe o módulo import ScriptA
# objetos deste script pod ser acessadas como ScriptA.nomeDafuncao

#%%
##### 2
nome=input("Digite seu nome")
print(f"OLÁ, {nome.upper()}! SEJA BEM-VINDO!")

#%%
#####3
#Você pode remover espaços extras no início e no fim de uma string em Python usando o método strip()

texto = "               Espaços extras             "
textoFormatado = texto.strip()
print(textoFormatado)

# Você pode usar lstrip() ou rstrip() para escolher apenas da
# esquerda ou direita

# Outro exemplo:
# Para remover espaços extras entre palavras dentro de uma string,
# você pode usar a função split() seguida de join().
# A função split() separa a string em uma lista de palavras,
# e join() junta as palavras novamente com um único espaço entre elas.

texto = "    Espaços    extras    neste     texto   "
textoFormatado = " ".join(texto.split())
print(textoFormatado)

#%%
#####4

texto = "O céu está azul"
print(f"{texto.replace('azul', 'nublado')}")

#%%
######5

meuTexto = "Esta lista contém muitos nomes"

print(f"{'Sim' if 'muitos' in meuTexto else 'Não'}. A variável contém a palavra 'muitos' ")


#%%
#####6

texto = "Python é incrível"
listaDePalavras = texto.split()

print (f"{listaDePalavras[0]}")
#ou
# print(f"A primeira palavra é: {texto.split()[0]}")


#%%
######7
#Use um loop for e range e imprima todos os números pares de 1 a 100

import math
piGerado = math.pi
print (piGerado)

piManual = 3.141592653
print(f"O valor de Pi com dois dígitos é: {piManual:.2f}".replace('.', ','))


#%%
#####8

frase = "O rato roeu  a roupa do rei de Roma"
print(f"A letra 'R' aparece {frase.upper().count('R')} vezes.")

# Outro método, lebrando que o objeto de texto é um iterável
contador = 0

for letra in frase.lower():
    if letra == 'r':
        contador += 1

print(f"A letra 'r' aparece {contador} vezes.")
