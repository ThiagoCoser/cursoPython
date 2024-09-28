# Solução dos exercícios contidos no arquivo 09

#%%
#1) Criação de um meuBilhete aleatório

import random

contador =0
meuBilhete = [] # Lista

while contador<6:
    numeroSorteado = random.randint(1,60)
    if numeroSorteado not in meuBilhete:
        meuBilhete.append(numeroSorteado)
        contador+=1

print (meuBilhete)
print (sorted(meuBilhete))
#%%
#2) Ler os dados e ver se meu bilhete está na lista
    # for ir´[a ler linha por linha. Podendo retornar cada linha
    # como uma string ou uma lista

#v1. Testando a leitura
with open('TXTS/dadosMegaSena.TXT', 'r', encoding='utf-8') as reader:
    for linhaString in reader:
        linhaString = linhaString.split() #retorna uma lista
        print (linhaString)
        print(type(linhaString))

#%%
#v2. Comparando as listas
# Há diferentes abordagens. Podemos ordenar as listas
# com o comando sorted() e comparar as listas com ==

# Outra abordagem é trasformar as listas em sets (conjuntos), porque
# a ordem dos elementos não importa. Porém, sets não contabiliza elementos
# duplicados. Neste caso, irá funcionar, pois os números das listas não
# são duplicados. Repare que precisamos converter cada elemento da lista
# do arquivo em numeros, por isso o comando type pode ser útil

import random

contador =0
meuBilhete = [] # Lista
bilheteEncontrado=False
#bilheteTestePremiado=[7,13,19,22,40,47]
bilheteDeOuro=[5,10,33,34,37,53]


while contador<6:
    numeroSorteado = random.randint(1,60)
    if numeroSorteado not in meuBilhete:
        meuBilhete.append(numeroSorteado)
        contador+=1

with open('TXTS/dadosMegaSena.TXT', 'r', encoding='utf-8') as reader:
    for linhaString in reader:
        linhaString = linhaString.split() #retorna uma lista de strings
        linhaStringInt = [int(num) for num in linhaString]

        print(set(linhaString))
        print(set(linhaStringInt))

        if set(linhaStringInt) == set(meuBilhete):
            print(f"Seu bilhete{meuBilhete}já saiu no jogo{linhaStringInt}")
            bilheteEncontrado=True
            break

        elif set(linhaStringInt) != set(meuBilhete):
           continue

if bilheteEncontrado ==False:
    print(f"Seu bilhete{meuBilhete} nunca saiu nos jogos!")
