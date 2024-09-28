# Solução dos exercícios contidos no arquivo 09

# Exercício, em duplas.

# O BILHETE DE OURO

# A mega sena é a maior modalidade de loteria do Brasil. Para jogar da
# maneira mais simples, você escolhe 6 números de 1 a 60 e precisa acertar
# todas as escolhas. A probabilidade matemática de acerto é 1:50.063.860!
# Ou seja, é quase impossível acertar, melhor aprender a programar em
#Python!

# A partir da importação dos dados dos resultados de todos os sorteios,
# converse com seu par e crie 2 scripts que façam o seguinte:

# 1) Crie um bilhete aleatório com 6 números (não pode haver números
# repetidos). Verifique se este bilhete está presente no histórico dos
# resultados. Este pode ser um bom bilhete?

# 2) Faça uma lista da quantidade que cada número saiu em todos os jogos,
# verificando assim se há um equilíbrio na distribuição dos números.
# Transforme o resultado de cada número em porcentagem,
# liste os números que mais sairam e crie assim
# O BILHETE DE OURO, contendo apenas os números com maior probabilidade
# de sair.

# Página oficial contendo todos os resultados para download
# https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx

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
