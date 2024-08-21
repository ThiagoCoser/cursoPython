# Instalar a biblioteca keyboard
# pip install keyboard

import keyboard

# Inicializa a variável booleana
estado = False

def alternar_estado(evento):

    global estado
    estado = not estado

    if estado:
        print("Ligado")

    else:
        print("Desligado")

# Registra o evento de pressionar a barra de espaço
keyboard.on_press_key('space', alternar_estado)


# Mantém o script em execução para escutar eventos
print("Pressione a barra de espaço para alternar o estado. Pressione 'ESC' para sair.")
keyboard.wait('esc')  # Mantém o script em execução até que a tecla 'ESC' seja pressionadai
