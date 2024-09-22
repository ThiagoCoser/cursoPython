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

#%%
with open('teste.txt', 'r') as reader:
    print(reader.readline(10))

with open('teste.txt', 'r') as reader:
    print(reader.readlines(5))

#%%
# Escrevendo um novo arquivo olaMundo


file = open("olaMundo.txt",'w')
file.write("Olá mundo!")

with open('olaMundo.txt', 'r') as reader:
    print(reader.read())
