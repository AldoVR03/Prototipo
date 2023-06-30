import tkinter as tk

class registro_jugador:
    def registro(self, ventana):
        self.ventana = ventana
        #Destruye la ventana anterior
        self.ventana.destroy()

        #Generar ventana
        self.ventana_registro = tk.Tk()
        self.ventana_registro.title("Registro")
        self.ventana_registro.geometry("1200x800")
        self.ventana_registro.config(bg="#fcfcfc")

        #self.createProgressBar()
        
        
        #Titulo de la pestaña
        etiqueta_usuario = tk.Label(text="Registro",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_usuario.pack(padx=0)

        #Nombre de la etiqueta (Ingreso de nombre de usuario)
        etiqueta_usuario_registro = tk.Label(text="Ingrese nombre de usuario",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_usuario_registro.pack()
        self.usuario_registro = tk.Entry(font=("Times",14))
        self.usuario_registro.pack()
        
        #Nombre de la etiqueta (Ingreso de apodo del usuario)
        etiqueta_apodo_registro = tk.Label(text="Ingrese el apodo \n(Nombre dentro del juego)",font=("Times",14),height=2,bg="#fcfcfc")
        etiqueta_apodo_registro.pack()
        self.apodo_registro = tk.Entry(font=("Times",14))
        self.apodo_registro.pack()

        #Ingreso de contraseña (Ingreso de contraseña del usuario)
        etiqueta_contraseña_registro = tk.Label(text="Ingresar contraseña",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_contraseña_registro.pack()
        self.contraseña_registro = tk.Entry(font=("Times",14))
        self.contraseña_registro.pack()
        self.contraseña_registro.config(show="*")

        #Boton para termino de registro
        Registrars= tk.Button(text="Registrarse",
                               font=("Times",14),
                                bg="#FFFFFF")
        Registrars.pack(pady=15)
    
class registro_gm:
    def __init__(self):
        print("hola")
    