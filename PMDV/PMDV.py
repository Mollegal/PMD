import _tkinter
import customtkinter


'''#---Def's'''



'''Criando App'''

#Definindo Tema do App-->

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

#Criando App-->

pmdv = customtkinter.CTk()
pmdv.geometry("800x500")
pmdv.title("Programa Mol de Dimensionamento de Vigas")

'''Frames'''

#Definindo Frames-->

pmdv.grid_columnconfigure(1, weight=1)
pmdv.grid_rowconfigure(0, weight=1)

#Frame Esquerda

lframe = customtkinter.CTkFrame(master=pmdv, width=200, corner_radius=0)
lframe.grid(column=0, row=0, sticky="nswe")

#Frame Direita

dframe = customtkinter.CTkFrame(master=pmdv)
dframe.grid(column=1, row=0, padx=5, pady=5, sticky="nswe")


'''Frame Esquerda'''

#ComboBox Concreto e Aço

label_concreto = customtkinter.CTkLabel(master=lframe, text="Concreto")
label_concreto.grid(column=0, row=0, padx=10, pady=10)
cbox_concreto = customtkinter.CTkComboBox(master=lframe, values=["20", "25", "30"])
cbox_concreto.grid(column=0, row=1, padx=10, pady=10)

label_aco = customtkinter.CTkLabel(master=lframe, text="Aço")
label_aco.grid(column=1, row=0, padx=10, pady=10)
cbox_aco = customtkinter.CTkComboBox(master=lframe, values=["25", "50", "60"])
cbox_aco.grid(column=1, row=1, padx=10, pady=10)