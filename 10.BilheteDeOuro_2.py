# Solução dos exercícios contidos no arquivo 09

#%%
#1) Criação de um um dicionário dos números

numerosMegaSena ={}

numero=1

#Cria uma chave str par ao número a associa o valor 0, ou seja
# cada valor saiu 0 vezes ainda

while numero<61:
   numerosMegaSena[str(numero)] = 0
   numero+=1

print (numerosMegaSena)
print(type(numerosMegaSena))

with open('TXTS/dadosMegaSena.TXT', 'r', encoding='utf-8') as reader:
    for linha in reader:
        listaRetornada = linha.split()

        for i in listaRetornada :
            # Verifica se o elemento 'i' está no dicionário
            if i in numerosMegaSena:
                numerosMegaSena[i] += 1  # Incrementa o valor correspondente

print(numerosMegaSena)
print(max(numerosMegaSena))
print(sorted(numerosMegaSena.items(), key=lambda valor: valor[1], reverse=True))
