

import tkinter as tk

# from tkinter import *       
 
# Creating a tkinter window
meuApp = tk.Tk() 

contador=0

minhaImagem = tk.PhotoImage(file="minhaImagem.png")
minhaImagem2 = tk.PhotoImage(file="minhaImagem2.png")
meuTexto = "Olá mundo"  


meuApp.geometry('640x480')     
meuApp.title("Meu aplicativo")


meuApp.configure(bg='#4a4a4a')
 
 
def updateImage():

  global contador
  contador+=1

  if contador==1:
    myLabelText.configure(text="Segundo")
  
  if contador==2:
  
    myLabelText.configure(text="Terceiro")
    
  if contador==3:
  
    myLabelText.configure(text="Quarto")
    myLabel.configure(image=minhaImagem2)

# Creating a Button
btn = tk.Button(meuApp, text = 'Fechar', command = meuApp.quit, image="")
btn.place(x=10, y=10)

btn2 = tk.Button(meuApp, text = 'Continuar', command = updateImage, image="")
btn2.place(x=450, y=420)
#btn2.place(relx=0.1, rely=0.1, anchor="nw")

#myLabel = tk.Label(width=30, height=30, bg="black", image=minhaImagem)
myLabel = tk.Label(width=400, height=130, bg="black", image=minhaImagem)
myLabel.place(relx=0.5, rely=0.3, anchor="center")
#myLabel.place(x=5, y=300)


#myLabelText = tk.Label(text="Print", anchor=tk.CENTER, bg="lightblue", height=3, width=30,font=("Arial", 16, "bold"), justify=tk.CENTER)
myLabelText = tk.Label(text=meuTexto , anchor=tk.CENTER, bg="lightblue", height=3, width=30,font=("Arial", 16, "bold"), justify=tk.CENTER)

myLabelText.place(relx=0.5, rely=0.75, anchor="center" )
#myLabelText.place(x=5, y=100)


#myLabel.pack()

#updateImage()

meuApp.mainloop()
