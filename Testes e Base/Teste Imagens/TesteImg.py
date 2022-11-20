import tkinter
import customtkinter
import os
from PIL import ImageTk, Image

pastaApp = os.path.dirname(__file__)

app = customtkinter.CTk()

img = ImageTk.PhotoImage(Image.open(pastaApp+"\\teste.jpg"))

label = customtkinter.CTkLabel(master=app, image=img)
label.pack()




app.mainloop()