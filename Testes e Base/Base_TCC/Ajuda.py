import tkinter
import customtkinter
from PIL import ImageTk, Image

def ajudapp():
    
    #Definindo Tema
    
    #Criando janela
    ajuda = customtkinter.CTk()
    ajuda.geometry("400x400")
    ajuda.title("Ajuda")
    
    #Paramentros Imagens
    photo = Image.open("Teste.jpg")
    imgteste = ImageTk.PhotoImage("Teste.jpg")
    
    #adicionando imagem
    label = customtkinter.CTkLabel(master=ajuda, image=imgteste)
    label.image= imgteste
    label.pack()


    ajuda.mainloop()