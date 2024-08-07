import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    nome = entrada_nome.get()
    messagebox.showinfo("Saudação", f"Olá, {nome}!")

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")

# Definir o tamanho da janela (largura x altura)
root.geometry("300x150")  # Largura de 300 pixels e altura de 150 pixels

# Criar um rótulo e um campo de entrada
rotulo = tk.Label(root, text="Digite seu nome:", font=("Arial", 12))
rotulo.pack(pady=10)  # Adiciona espaçamento vertical

entrada_nome = tk.Entry(root, font=("Arial", 12), width=20)  # Ajusta a largura
entrada_nome.pack(pady=5)

# Criar um botão para mostrar a mensagem
botao = tk.Button(root, text="Enviar", command=mostrar_mensagem, font=("Arial", 12), width=10, height=2)
botao.pack(pady=10)

# Iniciar o loop principal da interface
root.mainloop()
