from tkinter import * #importar libreria tkinter
from tkinter import ttk
from tkinter import messagebox as mb
class MuestraWidgetsActividad:
    def __init__(self, raiz):
        #init sirve como constructor de la clase(), self que hace referencia a los elementos de la misma clase.
        raiz.title("Muestra Widgets")
        #la raiz es nuestra ventana base #self da a conocer los atributos.
        self.Nombre = StringVar()
        self.ApellidoPaterno = StringVar()
        self.ApellidoMaterno = StringVar()
        self.Correo = StringVar()
        self.Movil = StringVar()
        estado = StringVar()
        
        
        mainFrame=ttk.Frame(raiz, padding="10 10 20 10") #Widgets transparentes #Instancia de raiz
        mainFrame.grid(column=0, row=0, padx=10)
        Frame1=ttk.Frame(mainFrame, padding="20 10 10 10", borderwidth=3,relief="raised") #Widgets transparentes #Instancia de raiz
        Frame1.grid(column=0, row=0, pady=15)
        Frame2=ttk.Frame(mainFrame, padding="10 10 10 10",borderwidth=3,relief="raised")
        Frame2.grid(column=0, row=1, sticky=(W),pady=15)
        Frame3=ttk.Frame(mainFrame, padding="10 10 10 10")
        Frame3.grid(column=1, row=0,padx=10)
        
        NombreEntry = ttk.Entry(Frame1, width=25)
        NombreEntry.grid(column=2,row=1)
        
        
        ApellidoPaternoEntry = ttk.Entry(Frame1, width=25)
        ApellidoPaternoEntry.grid(column=2,row=2, pady=12)
        
        ApellidoMaternoEntry = ttk.Entry(Frame1, width=25)
        ApellidoMaternoEntry.grid(column=2,row=3)
        
        CorreoEntry = ttk.Entry(Frame1, width=25)
        CorreoEntry.grid(column=2,row=4)
        
        MovilEntry = ttk.Entry(Frame1, width=25)
        MovilEntry.grid(column=2,row=5)
        
        estudiante=ttk.Radiobutton(Frame3, text="Estudiante")
        estudiante.grid(column=4,row=2, sticky=(W), padx=12)
        empleado=ttk.Radiobutton(Frame3, text="Empleado")
        empleado.grid(column=4,row=3, sticky=(W), padx=12)
        desempleado=ttk.Radiobutton(Frame3, text="Desempleado")
        desempleado.grid(column=4,row=4, sticky=(W),padx=12)
        
        ttk.Label(Frame2, text="Aficiones").grid(column=0, row=1, pady=12)
        leer=ttk.Checkbutton(Frame2,text="Leer")
        leer.grid(column=0,row=2,sticky=(W),pady=12)
        musica=ttk.Checkbutton(Frame2,text="Musica")
        musica.grid(column=2,row=2,sticky=(W),pady=12)
        videojuegos=ttk.Checkbutton(Frame2,text="Videojuegos                   ")
        videojuegos.grid(column=3,row=2,sticky=(W),pady=12)


        Comboestados= ttk.Combobox(mainFrame, textvariable=estado)
        Comboestados.grid(column=1,row=1)
        
        Comboestados['values'] = ("Jalisco", "Nayarit","Colima", "Michoacan")
    
        
        ttk.Label(Frame1, text="Nombre").grid(column=0, row=1, pady=12) #sticky=(N,W,E,S)) #Objeto
##        ttk.Label(mainFrame, textvariable=self.usuario).grid(column=1, row=0)
        ttk.Label(Frame1, text="ApellidoPaterno").grid(column=0, row=2, pady=12)
        ttk.Label(Frame1, text="ApellidoMaterno").grid(column=0, row=3, pady=12)
        ttk.Label(Frame1, text="Correo").grid(column=0, row=4, pady=12)
        ttk.Label(Frame1, text="Movil").grid(column=0, row=5)
       
        ttk.Button(mainFrame, text="Guardar", command=self.acerca).grid(column=0, row=5,  sticky=(W))
        ttk.Button(mainFrame, text="Cancelar", command=self.acerca).grid(column=0, row=5,  sticky=(N))

    
    def acerca(self):
        mb.showinfo("Información", "Este usuario fue ingresado con exito.: ")
            
if __name__=="__main__":
    print("Nada mas se mostrara si es el principal.")     
    print("Nada mas se mostrara esto si es el principal.")
    
 