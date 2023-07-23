import tkinter as tk
from tkinter import ttk


class characterLevelComponent():
    def __init__(self,root) -> None:
        self.barra = ttk.Progressbar(root, orient='horizontal', length=200,mode='determinate', maximum=200)
        
        # barra["value"]=100
        # Configurar el estilo personalizado de la barra de progreso
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Seleccionar un tema compatible

        # Cambiar el color del fondo y agregar un borde a la barra de progreso
        self.style.configure("MiEstilo.Horizontal.TProgressbar",
                        background='yellow',
                        troughcolor='light gray',
                        troughrelief='flat',
                        bordercolor='black',
                        borderwidth=1)

        self.barra.style = "MiEstilo.Horizontal.TProgressbar"
        self.barra["style"] = self.barra.style


    def show(self):
        self.barra.pack()
    def setLevel(self,level):
        self.barra["value"]=level

    def aumentar_experiencia(self):
    
        valor = self.barra["value"] + 10
        self.barra["value"] = valor
        print(self.barra["value"])

# ventana = tk.Tk()

# # Crear una barra de progreso
# # barra = ttk.Progressbar(ventana, orient='horizontal', length=50,mode='determinate', maximum=200)
# # barra.pack(pady=20)
# # print(barra["value"])
# # # barra["value"]=100
# # # Configurar el estilo personalizado de la barra de progreso
# # style = ttk.Style()
# # style.theme_use('clam')  # Seleccionar un tema compatible

# # # Cambiar el color del fondo y agregar un borde a la barra de progreso
# # style.configure("MiEstilo.Horizontal.TProgressbar",
# #                 background='yellow',
# #                 troughcolor='light gray',
# #                 troughrelief='flat',
# #                 bordercolor='black',
# #                 borderwidth=1)

# # barra.style = "MiEstilo.Horizontal.TProgressbar"
# # barra["style"] = barra.style

# # # Función para aumentar la experiencia


# comp=characterLevelComponent(ventana)
# comp.show()

# boton_aumentar = tk.Button(ventana, text='Aumentar experiencia', command=comp.aumentar_experiencia)
# boton_aumentar.pack(pady=10)
# ventana.mainloop()