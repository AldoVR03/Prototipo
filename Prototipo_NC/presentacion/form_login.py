import tkinter as tk 
from PIL import ImageTk, Image

#import (metodos)
from form_cambio_pass import *
from form_registro import *

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("inicio de sesion")#Nombre de la ventana
        ##self.ventana.attributes("-fullscreen", True)
        self.ventana.geometry("1200x500")#Tamaño de la ventana
        self.ventana.config(bg='#fcfcfc')#Color de la ventan 
        self.ventana.resizable(width=0, height=0)#Bloqueo de maximizar ventana

        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        print(screen_width)
        print(screen_height)
        window_width = 1200
        window_height = 478
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")


        imagen_sesion = ImageTk.PhotoImage(Image.open("./img/fondo_login.png"))
        label_sesion = tk.Label(image=imagen_sesion)
        label_sesion.pack(side="right")

        titulo = tk.Label(text="Inicio de sesión", bg="#FFFFFF",font=("Times", 14))
        titulo.pack(padx=5,pady=40)

        etiqueta_usuario = tk.Label(text="Usuario",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_usuario.pack(pady=5)
        self.usuario = tk.Entry(font=("Times",14))
       
        self.usuario.pack()

        etiqueta_contraseña = tk.Label(text="Contraseña",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_contraseña.pack()
        self.contraseña = tk.Entry(font=("Times",14))
        self.contraseña.pack()
        self.contraseña.config(show="*")

        cambiar_contraseña = tk.Button(text="Cambiar contraseña", font=("Times",10), bg="red", command=lambda:cambioClave().cambio_clave(self.ventana))
        cambiar_contraseña.pack(pady=15)

        inicio = tk.Button(text="Entrar", font=("Times",14), fg="#fcfcfc", bg="#8A169E") 
        inicio.pack(pady=15)

        registro=registro_jugador()
        print(registro)

        registrarse = tk.Button(text="Registrarse", font=("Times",14), bg="#FFFFFF", command=lambda:registro.registro(self.ventana))
        registrarse.pack(pady=15)

        salida = tk.Button(text="Salir",font=("Times",14), bg="#FFFFFF", command=self.ventana.destroy)
        salida.pack()

        self.ventana.mainloop()



if __name__=="__main__":
    app=App()   