#%%
# Explorando a Classe String

# As linhas 1 e 2 declaram variáveis do tipo String.
# Na primeira linha são usadas aspas duplas, e na segunda,
# aspas simples. A impressão dos tipos das variáveis feitas nas
# linhas 4 e 5 vão exibir str, ou seja, são objetos da classe String

nome_1 = "Thiago"
nome_2 = 'Joana da Silva'

print(type(nome_1)) # type 'str'
print(type(nome_2)) # type 'str'

#%%

# Strings são sequências de caracteres, constituindo um objeto iterável.
# Podemos, por exemplo, acessar o índice de de posição, ou utilizar
# funcções como len() ou procurar por determinada sequência com um for

nome = "Beagle"
print(nome[2]) # D
print (len(nome))

# %%
#Fatiamento
nome = "Thiago"
print(nome[1:4]) # hia


# %%

#Principais métodos
#find()
#Com o método find() podemos procurar uma substring dentro de
#uma string e retornar a posição onde ela foi encontrada

mensagem = 'Teste de procura de um valor'
print(mensagem.find('valor')) # 23
print(mensagem.find('abc')) # -1


# %%
# split()
#O método split() desmembramos uma string em múltiplas
#strings através de um separador passado no parâmetro,
# retornando todas numa lista.

mensagem = 'Teste de separação de uma mensagem'
nova_mensagem = mensagem.split(' ')
print(type(nova_mensagem)) # type 'list'
print(nova_mensagem)
print(f"\n{'\n'.join(nova_mensagem)}")

#%%
# replace()
# Substitui um texto por outro

preço = 100
txt = f"O preço é de {preço:.2f} reais".replace('.', ',')
print(txt)

# %%
# Método upper()

#Retorna todas as palavras em caixa alta

mensagem = 'Isto é um teste'
nova_mensagem = mensagem.upper()

print(nova_mensagem)
# %%
#Retorna todas as palavras em caixa baixa
# Método lower()
mensagem = 'ISTO É UM TESTE'
nova_mensagem = mensagem.lower()

print(nova_mensagem)
#%%
