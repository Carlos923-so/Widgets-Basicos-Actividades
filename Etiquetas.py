from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label(raiz, text="Etiqueta solo texto")
etqTexto.grid()

imagen = PhotoImage(file="hasbullita.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="EtqCombinada", compound="right")
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()
