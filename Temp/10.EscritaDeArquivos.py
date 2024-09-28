#%%
# Lendo e escrevendo arquivos

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
# Escrevendo um novo arquivo olaMundo


file = open("olaMundo.txt",'w')
file.write("Olá mundo!")

with open('olaMundo.txt', 'r') as reader:
    print(reader.read())

# Extra, abrindo arquivos de url

# pip install requests

import requests

url = "https://raw.githubusercontent.com/ThiagoCoser/cursoPython/main/teste.txt"

dadoOnline= requests.get(url)


meuArquivo = dadoOnline.text
print(type(meuArquivo))  # Agora será uma string
print(meuArquivo)        # Conteúdo do arquivo
