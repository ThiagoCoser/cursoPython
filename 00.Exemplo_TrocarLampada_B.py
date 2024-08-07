# Algoritmo para trocar uma lâmpada

# Função para verificar o estado da lâmpada
def trocar_lampada():

    # Verifica se a lâmpada está queimada
    if entrada == "s":
   # Alternativamente, podemos: if entrada.lower() == "s" or entrada =="S":
        print("A lâmpada está queimada.")
        print("Substituindo por uma nova lâmpada...")
        # Aqui poderia ter o código para substituir a lâmpada
        print("A nova lâmpada foi instalada.")

    else:
        print("A lâmpada está funcionando. Não é necessário trocá-la.")

# Exemplo de uso
entrada = input ("Digite 's' se a lâmpada estiver queimada")
trocar_lampada()
