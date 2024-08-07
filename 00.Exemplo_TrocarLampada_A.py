# Algoritmo para trocar uma lâmpada

# Função para verificar o estado da lâmpada
def trocar_lampada(esta_queimada):

    # Verifica se a lâmpada está queimada
    if esta_queimada:
        print("A lâmpada está queimada.")
        print("Substituindo por uma nova lâmpada...")
        # Aqui poderia ter o código para substituir a lâmpada
        print("A nova lâmpada foi instalada.")
    else:
        print("A lâmpada está funcionando. Não é necessário trocá-la.")

# Exemplo de uso
esta_queimada = True  # True indica que a lâmpada está queimada
trocar_lampada(esta_queimada)
