import tkinter
import customtkinter
import os



'''Def's'''

def viga():
    pastaApp = os.path.dirname(__file__)
    os.system(pastaApp+"\\PMDV.py")

'''Criando App'''

#Criando App-->

pmdv = customtkinter.CTk()
pmdv.geometry("200x400")
pmdv.title("PMDV")

'''Frames'''
pmdv.grid_columnconfigure(0, weight=1)
pmdv.grid_rowconfigure(0, weight=1)

frame = customtkinter.CTkFrame(master=pmdv)
frame.grid(column=0, row=0, padx=5, pady=5, sticky="nswe")
frame.rowconfigure(1, minsize=30)

'''Label'''

title = customtkinter.CTkLabel(master=frame, text="PMDV", text_font=("Arial", 38), justify="center")
title.grid(row=0, padx=5, pady=20)

buttonviga = customtkinter.CTkButton(master=frame, text="VIGA", command=viga, text_font=("Arial", 22))
buttonviga.grid(row=2, padx=10, pady=10)
buttonlaje = customtkinter.CTkButton(master=frame, text="LAJE", command="", text_font=("Arial", 22))
buttonlaje.grid(row=3, padx=10, pady=10)
buttonpilar = customtkinter.CTkButton(master=frame, text="PILAR", command="", text_font=("Arial", 22))
buttonpilar.grid(row=4, padx=10, pady=10)
buttoncredito = customtkinter.CTkButton(master=frame, text="CRÉDITOS", command="", text_font=("Arial", 22))
buttoncredito.grid(row=5, padx=10, pady=10)




pmdv.mainloop()