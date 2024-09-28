import random

# Caminho do arquivo de nomes
arquivoTXT = r'C:\Users\thiag\OneDrive\Documentos\GitHub\cursoPython\Testes\nomes.txt'

# Carregar a lista de nomes do arquivo
def carregarNomes(arquivo):
    with open(arquivo, 'r') as f:
        nomes = f.read().splitlines()
    return nomes

# Sortear um nome aleatório
def sorteaiaNome(nomes):
    return random.choice(nomes)

# Carregar os nomes do arquivo
nomes = carregarNomes(arquivoTXT)

# Sortear um nome aleatório
nome_sorteado = sorteaiaNome(nomes)

# Exibir o nome sorteado
print(f'O nome sorteado foi: {nome_sorteado}')

# # Contar o número de nomes
# numero_de_nomes = len(nomes)

# # Exibir o número de nomes
# print(f'O número de nomes no arquivo é: {numero_de_nomes}')

# # Imprimir a posição (índice) e o nome de cada item na lista
# for indice, nome in enumerate(nomes):
#     print(f'Índice: {indice}, Nome: {nome}')
