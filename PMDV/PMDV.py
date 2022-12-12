import tkinter
import customtkinter
import math


'''#---Def's'''

#Créditos
def creditos():
    
    j_creditos = customtkinter.CTkToplevel(pmdv)
    j_creditos.geometry("290x130")
    j_creditos.title("Créditos")
    
    label_creditos1 = customtkinter.CTkLabel(master=j_creditos, text="Criador por:", text_font=("Arial", 12))
    label_creditos1.grid(column=0, row=0, padx=50, pady=20)
    label_creditos2 = customtkinter.CTkLabel(master=j_creditos, text="Gabriel Rodrigues Mol", text_font=("Arial", 18))
    label_creditos2.grid(column=0, row=1, padx=20)

#Resultado seco
def resolver():
    
    #concreto e aço
    fck = float(cbox_concreto.get())
    fyk = float(cbox_aco.get())
    fyk_mpa = fyk*10
    fcds = (fck/10)/1.4 #concreto FCD
    fyds = (fyk_mpa/10)/1.15 #Aço Fyd
    #outras entry
    h = float(entry_h.get())
    bw = float(entry_bw.get())
    c = float(entry_c.get())
    mk = float(entry_mk.get())
    #aredondamento
    fcd = round(fcds, 2)
    fyd = round(fyds, 2)
    
    '''equações'''
    
    mds = mk*1.4*100 #100 para transformar em Kn.cm
    md = round(mds, 2)
    d = h - c
    
    xs = 1.25*d*(1-(math.sqrt((1-(md/(0.425*bw*(d**2)*fcd))))))
    x = round(xs, 2)
    aaço = (md/((d-0.4*x)*(fyd)))
    
    
    #resultado na label
    label_resultado.config(text=round(aaço, 2))




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
lframe.rowconfigure(6, minsize=50) #linha fantasma com tamanho 30

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

#Entry's

#h
label_h = customtkinter.CTkLabel(master= lframe, text="h (cm)")
label_h.grid(column=0, row=2, padx=10, pady=10)
entry_h = customtkinter.CTkEntry(master= lframe, justify="center")
entry_h.grid(column=0, row=3, padx=10, pady=10)

#bw
label_bw = customtkinter.CTkLabel(master= lframe, text="bw (cm)")
label_bw.grid(column=1, row=2, padx=10, pady=10)
entry_bw = customtkinter.CTkEntry(master= lframe, justify="center")
entry_bw.grid(column=1, row=3, padx=10, pady=0)

#c
label_c = customtkinter.CTkLabel(master=lframe, text="c (cm)")
label_c.grid(column=0, row =4, padx=10, pady=10)
entry_c = customtkinter.CTkEntry(master=lframe, justify="center")
entry_c.grid(column=0, row=5, padx=10, pady=10)

#Mk
label_mk = customtkinter.CTkLabel(master=lframe, text="Mk (N.m)")
label_mk.grid(column=1, row=4, padx=10, pady=10)
entry_mk = customtkinter.CTkEntry(master= lframe, justify="center")
entry_mk.grid(column=1, row=5, padx=10, pady=10)

#Botões

#Resultado
button_resolver = customtkinter.CTkButton(master=lframe, text="Resolver", command=resolver)
button_resolver.grid(column=0, columnspan=2, row=7, padx=10, pady=10)

#Resultado--mostrado
label_resultado = customtkinter.CTkLabel(master=lframe, text="")
label_resultado.grid(column=0, columnspan=2, row=8, padx=10, pady=10)

#Ajuda
button_ajuda = customtkinter.CTkButton(master=lframe, text="Ajuda", command="")
button_ajuda.grid(column=0, row=9, padx=10, pady=10)

#Créditos
button_creditos = customtkinter.CTkButton(master=lframe, text="Créditos", command=creditos)
button_creditos.grid(column=1, row=9, padx=10, pady=10)



pmdv.mainloop()