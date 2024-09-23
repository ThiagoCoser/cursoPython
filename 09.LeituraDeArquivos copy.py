#%%
# Lendo arquivos

open("teste.txt")
open("teste.txt",'r')
#open("teste.txt", 'w')

#%% Classe
meuArquivo = open ('teste.txt')
print (type(meuArquivo))

#%% Certificando que o arquivo é de leitura e que será propriamente fechado

with open('teste.txt', 'r') as reader:
    print(reader.read())

with open('teste.txt', 'r') as reader:

    print(reader.readline())
    print(reader.readline())
    print(reader.readline())

with open('teste.txt', 'r') as reader:

    lista = reader.readlines()
    print(lista)
    print(lista[3])

# Métodos
# .read():
# Lê todo o conteúdo do arquivo de uma vez como uma única string.

#. readline():
# Lê uma linha de cada vez do arquivo e retorna como string, incluindo o caractere de nova linha \n, se houver.
# Melhor utilizado em grandes arquivos e volumes de dados, logs, datasets, etc

# .readlines()
# Lê todas as linhas do arquivo e retorna uma lista, onde cada elemento é uma linha do arquivo.

# Controle de fluxo

# Imprime todas as linhas
with open('teste.txt', 'r') as reader:
    for linha in reader:
        # Processa cada linha individualmente
        print(linha)

# Procura uma palavra-chave em cada linha
with open('teste.txt', 'r') as reader:
    while True:
        linha = reader.readline()
        if not linha:  # Fim do arquivo
            break
        if "teste" in linha:
            print(f"Palavra encontrada: {linha}")
            break
        else:
            print(f"Palavra não encontrada")

#%%
# Extra, abrindo arquivos de url

# pip install requests

import requests

url = "https://raw.githubusercontent.com/ThiagoCoser/cursoPython/main/teste.txt"

dadoOnline= requests.get(url)


meuArquivo = dadoOnline.text
print(type(meuArquivo))  # Agora será uma string
print(meuArquivo)        # Conteúdo do arquivo


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


# Dicas

# 1)    Considere pensar como formatar os dados para facilitar a manipulação
# 2)    Você pode utilizar um método como splitlines() e quebrar o arquivo
#       de texto em linhas
# 3)    O formato CSV permite separar os dados por vírgulas ou outros caracteres.
#       A biblioteca Pandas permite usar métodos para o uso de diversos tipos de
#       ados
