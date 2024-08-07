# Este algoritmo trabalha com variáveis simples e inputs

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
