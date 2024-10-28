#%%
# A função open() leva dois parâmetros; nome do arquivo e modo.
# Existem métodos diferentes para abrir um arquivo:

# "w" - Write - Abre um arquivo para escrita, cria o arquivo se ele não exista, sobrescrevendo qualquer conteúdo do arquivo
# "x" - Create - Cria o arquivo especificado, retorna um erro se o arquivo existir
# "a" - Append - Cria um arquivo e permite adicionar conteúdo após a última linha

# Exemplo
# Isto criará um arquivo de texto vazio, chamado teste
open("teste.txt", "w")


#%%
meuArquivo = open("teste.txt", "a")
meuArquivo.write("Adicionando conteudo\n")
meuArquivo.close()

# Abre o arquivo e lê o conteúdo
meuArquivo = open("teste.txt", "r")
print(meuArquivo.read())


#%%
# Exemplo 3
# Escrevendo variáveis em um arquivo, com a declaração "with"

minhaLista = ["João\n", "Maria \n", "Pedro\n"]
# minhaListaStr= [str(num) for num in minhaLista]

# Escrevendo no arquivo
with open("teste.txt", "w") as meuArquivo:
    # Escreve dados no arquivo
    meuArquivo.write("Olá Mundo! \n")
    meuArquivo.write("\n")
    meuArquivo.writelines(minhaLista) # escreve os valores de um iterável, como uma lista, contendo strings


# Lê os dados do arquivo
with open("teste.txt", "r") as meuArquivo:
    print(meuArquivo.read())


#%%
# Estrutura de fluxo com repetição para escrita em um arquivo

# Dados de uma lista de strings para serem adicionados no arquivo
minhaLista = ["Linha 1", "Linha 2", "Linha 3"]

# Escrita no arquivo
with open('teste.txt', 'w') as meuArquivo:
    for linha in minhaLista:
        meuArquivo.write(linha + '\n')  # Escreve cada elemento + o parâmetro indicado

# O Arquivo é fechado automaticamente quando o bloco da declaração "with" termina

#%%
# Outro exemplo
import random

numeroSorteado=0
contador = 0

with open('teste.txt', 'w', encoding='utf-8') as meuArquivo:
    meuArquivo.write("Números Sorteados\n")

while contador<10:

    numeroSorteado=random.randrange(0,10)
    contador+=1
    with open('teste.txt', 'a') as meuArquivo:
        meuArquivo.write(str(numeroSorteado))
        meuArquivo.write("\n")

# Lê os dados do arquivo
with open("teste.txt", "r", encoding='utf-8') as meuArquivo:
    print(meuArquivo.read())

#%%
# Erro de exceção
# Lembre-se que podemos levantar erros de exceção

nomeDoArquivo = input("Digite um nome de um arquivo para criar")

try:
    with open(nomeDoArquivo + ".txt", "x") as meuArquivo:
        meuArquivo.write("Arquivo criado!\n")

except FileExistsError:
    print("O arquivo já existe!")


#%%
# Exercícios

# 1) Crie e escreva em um arquivo com modo 'w'
# Crie um arquivo chamado exercicio1.txt e escreva "Hello, World!" nele

# 2) Leia o Conteúdo de um arquivo
# Leia e imprima o conteúdo do arquivo exercicio1.txt criado

#3) Manipule uma lista e escreva o conteúdo em um arquivo
# Solicite ao usuário 3 frutas, crie uma lista e adicione para um arquivo frutas.txt

#4) Verifique se o arquivo frutas.txt existe com modo 'x'
# Tente criar um arquivo chamado frutas.txt.  Se ele já existir, capture o erro

#5) Contagem de palavras em um arquivo
# Crie um arquivo chamado texto.txt e adicione uma frase. Depois, leia o arquivo e conte o número de palavras

#6) Gere números aleatórios e salve em arquivo
# Gere 100 números aleatórios e salve-os em numeros.txt, um em cada linha
