import tkinter as tk
import tkinter.ttk as ttk
from constants import RAZAS, CLASES, PIEL
from tkinter.colorchooser import askcolor
import main

widthOp=100
heightOp=100

widthFrame=500
heightFrame=500
class PersonalizacionView():
    def __init__(self, ventana) -> None:
        #Ventana
        self.ventana = ventana
        #Frame opciones
        self.frameOpcion = tk.Frame(self.ventana,bg="purple",width=widthFrame,height=heightFrame)
        self.frameOpcion1 = tk.Frame(self.frameOpcion, bg="green",width=widthOp, height=heightOp)
        self.frameOpcion2 = tk.Frame(self.frameOpcion,bg="blue",width=widthOp, height=heightOp)
        #Personaje
        self.framePersonaje = tk.Frame(self.ventana, bg="red",width=widthFrame,height=heightFrame)
        self.imgPersonaje = main.imagenPersonaje(self.framePersonaje)
        #Lables
        self.Lable_nombrePersonaje = tk.Label(self.frameOpcion1,text="Nombre del personaje")
        self.Lable_raza = tk.Label(self.frameOpcion1, text="Raza")
        self.LableClase = tk.Label(self.frameOpcion1, text="Clase")
        self.Lable_colorPelo = tk.Label(self.frameOpcion2, text="Color de pelo")
        self.Lable_colorOjo = tk.Label(self.frameOpcion2,text="Color de ojo")
        self.Lable_colorPiel = tk.Label(self.frameOpcion2, text="Color de piel")
        #Entrys
        self.Entry_NombrePersonaje = tk.Entry(self.frameOpcion1)
        #Button
        self.Button_colorPelo = tk.Button(self.frameOpcion2, text="Color de pelo", command=lambda:self.CambiarColorParteCuerpo("PELO"))
        self.Button_colorOjo = tk.Button(self.frameOpcion2, text="Color de ojo", command=lambda:self.CambiarColorParteCuerpo("OJO"))
        self.Button_salir = tk.Button(self.frameOpcion2, text="Volver")
        self.Button_guardar = tk.Button(self.frameOpcion2, text="Guardar")
        #Combobox
        self.Combobox_raza = ttk.Combobox(self.frameOpcion1, values=RAZAS)
        self.Combobox_clase = ttk.Combobox(self.frameOpcion1, values=CLASES)
        self.Combobox_colorPiel = ttk.Combobox(self.frameOpcion2, values=PIEL)
        #Evento
        self.Combobox_clase.bind("<<ComboboxSelected>>",self.display_raza_clase)
    def show(self):
        #frames
        self.frameOpcion.pack(side="left")
        self.frameOpcion1.pack()
        self.frameOpcion2.pack()
        self.framePersonaje.pack(side="right")
        self.imgPersonaje.canvas.pack()
        #Contenido del frame 1
        self.Lable_nombrePersonaje.pack(pady=5)
        self.Entry_NombrePersonaje.pack(pady=5)
        self.Lable_raza.pack(pady=5)
        #Combobox de la raza
        self.Combobox_raza.pack(pady=5)
        self.LableClase.pack(pady=5)
        #Combobox de la clase
        self.Combobox_clase.pack(pady=5)
        #Contenido del frame 2
        self.Lable_colorPelo.pack(pady=5)
        self.Button_colorPelo.pack(pady=5)  
        self.Lable_colorOjo.pack(pady=5)
        self.Button_colorOjo.pack(pady=5)
        self.Lable_colorPiel.pack(pady=5)
        self.Combobox_colorPiel.pack(pady=5)
        self.Button_salir.pack(pady=5)
        self.Button_guardar.pack(pady=5)

    def display_raza_clase(self,*args):
        raza = self.Combobox_raza.get()
        clase=self.Combobox_clase.get()
        print(f"Seleccionaste esta clase {clase}")
        print(f"Seleccionaste esta raza {raza}")
        print(args)

    def CambiarColorParteCuerpo(self, parteCuerpo):
        if(parteCuerpo=="PELO"):
            color = askcolor()
            self.imgPersonaje.cambiarColorParte(self.imgPersonaje.getPeloId(),self.imgPersonaje.RUTA_IMAGEN_PELO, color[0]+(255,))
        elif(parteCuerpo=="OJO"):
            color = askcolor()
            self.imgPersonaje.cambiarColorParte(self.imgPersonaje.getOjosId(),self.imgPersonaje.RUTA_IMAGEN_OJOS, color[0]+(255,))
    

root = tk.Tk()
app = PersonalizacionView(root)
app.show()
root.mainloop()