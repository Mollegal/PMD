import tkinter
import customtkinter
from PIL import Image, ImageTk
import Ajuda


#Definindo tema

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

#criando janela#
App = customtkinter.CTk()
App.geometry("880x480")
App.title("Testes Cheio")

#-----Criando frames-----#//

App.grid_columnconfigure(1, weight=1)
App.grid_rowconfigure(0, weight=1)

#Esquerda
left_frame = customtkinter.CTkFrame(master=App, width=200, corner_radius=0)
left_frame.grid(column=0, row=0, sticky="nswe")
left_frame.columnconfigure((0, 1), weight=1)
left_frame.rowconfigure(6, minsize=30) #linha fantasma com espaçamento
left_frame.rowconfigure(8, minsize=50) #linha fantasma com espaçamento

#frame direita
right_frame = customtkinter.CTkFrame(master=App)
right_frame.grid(column=1, row=0, padx=10, pady=10, sticky="nswe")

#-----def-----#//

#Créditos--
def creditos():
    
    j_creditos = customtkinter.CTkToplevel(App)
    j_creditos.geometry("240x130")
    j_creditos.title("Créditos") 
    
    label_creditos1 = customtkinter.CTkLabel(master=j_creditos, text="Criado por:")
    label_creditos1.grid(column=0, row=0, padx=50, pady=20)
    label_creditos2 = customtkinter.CTkLabel(master=j_creditos, text="Gabriel Rodrigues Mol", text_font=("Arial", 12))
    label_creditos2.grid(column=0, row=1, padx=20)
    
#App de Ajuda--
def ajudaapp():
    
    Ajuda.ajudapp()

#Calcular--


#-----Frame Esquerda-----#

#Seleção de aço e concreto#
label_concreto = customtkinter.CTkLabel(master=left_frame, text="Concreto")
label_concreto.grid(column=0, row=0, padx=20, pady=12)
menu_concreto = customtkinter.CTkComboBox(master=left_frame, values=["20", "25", "30"])
menu_concreto.grid(column=0, row=1, padx=10, pady=0)

label_aco = customtkinter.CTkLabel(master=left_frame, text="Aço")
label_aco.grid(column=1, row=0, padx=20, pady=12)
menu_aco = customtkinter.CTkComboBox(master=left_frame, values=["25", "50", "60"])
menu_aco.grid(column=1, row=1, padx=10, pady=10)

#entry valores#
#h
label_h = customtkinter.CTkLabel(master= left_frame, text="h")
label_h.grid(column= 0, row= 2, padx=10, pady=10)
entry_h = customtkinter.CTkEntry(master= left_frame, justify="center")
entry_h.grid(column= 0, row = 3, padx=10, pady=10)

#bw
label_bw = customtkinter.CTkLabel(master= left_frame, text="bw")
label_bw.grid(column= 1, row= 2, padx=10, pady=10)
entry_bw = customtkinter.CTkEntry(master= left_frame, justify="center")
entry_bw.grid(column= 1, row= 3, padx=10, pady=10)

#c
label_c = customtkinter.CTkLabel(master= left_frame, text="Cobrimento")
label_c.grid(column= 0, row= 4, padx=10, pady=10)
entry_c = customtkinter.CTkEntry(master= left_frame, justify="center")
entry_c.grid(column=0, row= 5, padx=10, pady=10)

#mk
label_mk = customtkinter.CTkLabel(master= left_frame, text="Mk")
label_mk.grid(column=1, row=4, padx=10, pady=10)
entry_mk = customtkinter.CTkEntry(master= left_frame, justify="center")
entry_mk.grid(column=1, row=5, padx=10, pady=10)

#botões#
#resultado
button_resultado = customtkinter.CTkButton(master= left_frame, text="Resultado", command="")
button_resultado.grid(column=0, columnspan= 2, row= 7, padx= 10, pady=10)

#ajuda
button_ajuda = customtkinter.CTkButton(master= left_frame, text="Ajuda", command=ajudaapp)
button_ajuda.grid(column=0, row= 9, padx=10, pady=10)

#creditos#
button_creditos = customtkinter.CTkButton(master= left_frame, text="Créditos", command=creditos)
button_creditos.grid(column=1, row= 9)



App.mainloop()