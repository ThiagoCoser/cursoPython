#%%
import random

numeroSecreto = random.randint(1, 20)

print("Estou pensando em um número de 1 a 20.\nConsegues descobrir em 5 tentativas?")

# Pergunta para o jogador, em até 5 tentativas
for minhasTentativas in range(1, 6):
    print("Digite um número: ")
    tentativa = int(input())

    if tentativa < numeroSecreto:
        print(f"Seu palpite é muito baixo. \nEsta é sua {minhasTentativas}ª tentativa.")
    elif tentativa > numeroSecreto:
        print(f"Seu palpite é muito alto. \nEsta é sua {minhasTentativas}ª tentativa.")
    else:
        break  # Adivinhou o número corretamente!

# Mensagem final com o resultado
if tentativa == numeroSecreto:
    print(f'Bom trabalho! Você acertou o número em {minhasTentativas} tentativas!')
else:
    print(f'Não foi dessa vez. O número que eu estava pensando era {numeroSecreto}.')

# %%
