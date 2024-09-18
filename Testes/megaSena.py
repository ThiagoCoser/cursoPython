
import random

contagem=0
numeroAleatorio=0
listaNumerosSorteados=[]

while contagem < 6:
    contagem+=1
    numeroAleatorio=random.randint(1,60)
    listaNumerosSorteados.append(numeroAleatorio)




print (f"O bilhete premiado contém os números{listaNumerosSorteados}")
