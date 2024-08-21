# Importar bibliotecas

# pip install keyboard
# pip install pillow
# pip install playsound (em caso de erro: python -m pip install --upgrade setuptools wheel)

import keyboard
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

# Inicializa a variável booleana
estado = False

# Função para tocar o som
def tocar_som():
    playsound("Assets/lampada.mp3")  # Certifique-se de que o arquivo de som está no mesmo diretório

# Cria a janela principal
root = tk.Tk()
root.title("Lâmpada")

# Carrega as imagens
imagem_lampada_acesa = Image.open("Assets/LampadaA.jpg")
imagem_lampada_apagada = Image.open("Assets/LampadaB.jpg")

# Converte as imagens para o formato Tkinter
foto_lampada_acesa = ImageTk.PhotoImage(imagem_lampada_acesa)
foto_lampada_apagada = ImageTk.PhotoImage(imagem_lampada_apagada)

# Cria um label para mostrar a imagem
label_imagem = tk.Label(root, image=foto_lampada_apagada)
label_imagem.pack()

def alternar_estado(evento):
    global estado
    estado = not estado

    if estado:
        label_imagem.config(image=foto_lampada_acesa)
        tocar_som()
        print("Ligado")

    else:
        label_imagem.config(image=foto_lampada_apagada)
        print("Desligado")


# Registra o evento de pressionar a barra de espaço
keyboard.on_press_key('space', alternar_estado)

# Mantém o script em execução para escutar eventos
print("Pressione a barra de espaço para alternar o estado. Pressione 'ESC' para sair.")
root.mainloop()
keyboard.wait('esc')  # Mantém o script em execução até que a tecla 'ESC' seja pressionada
