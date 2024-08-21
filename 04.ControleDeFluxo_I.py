# Um dos super poderes de um código não é
# apenas executar uma instrução após a outra,
# mas com base em como as expressões são avaliadas,
# o programa pode tomar ações como pular instruções,
# repeti-las, ou executar outras ações.
# Instruções de controle de fluxo definem
# as condições para as tomadas de ações dentro do seu script
# em Python.

# If Elif Else

#%%
# Exemplo I
# Este algoritmo ordena dois números

a = 5
b = 7

if a > b:
    print("a é maior que b")
elif a < b:
    print("a é menor que b")
else:
    print("a e b são iguais")


#%%

# String
seuNome = input("Digite seu nome: ")

# Int
suaIdade = int(input("Digite sua idade: "))

# Bool
# Pergunta ao usuário e converte a resposta para minúscula para padronizar a comparação
resposta = input("Você já se formou? (s/n): ").strip().lower()

# Converte a resposta para booleano com base no valor
if resposta == "s":
    pergunta = True
elif resposta == "n":
    pergunta = False
else:
    # Tratar a entrada inválida ou definir um padrão
    print("Resposta inválida. Considerando como não.")
    pergunta = False

# Exibindo os resultados para verificação com F-Strings
print(f"Nome: {seuNome}")
print(f"Idade: {suaIdade}")
print(f"Já se formou: {pergunta}")
