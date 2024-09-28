
#%%
numeros=list(range(1,101))
print (numeros)
sum(numeros)

#%%
numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


#%%
numero = int(input("Digite um número: "))
for i in range(1, numero + 1):
    print(i)

# %%
