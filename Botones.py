from tkinter import *
from tkinter import ttk

raiz = Tk()
boton = ttk.Button(raiz, text="Boton solo texto")
boton.grid()

imagen = PhotoImage(file="hasbullita.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image'] = imagen

btnCombinada = ttk.Button(raiz, text="Boton Combinado", compound="bottom")
btnCombinada.grid()
btnCombinada['image'] = imagen

chkBoton = ttk.Checkbutton(raiz, text="Opcion1")
chkBoton.grid()

raiz.mainloop()