#!/user/bin/python3


from tkinter import *
from tkinter import ttk

window = Tk()

window.title('Welcome to KeepCoding Demo app') #Titulo ventana
window.geometry("1250x570")  #Tamaño ventana

imagen = PhotoImage(file = "AAA.png")   # insertar imagen
etiqueta = Label(window, image = imagen).place(x = 0, y = 0)  #cargar imagen

window.mainloop()

