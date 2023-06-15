import tkinter as tk 
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from db.data import *
from forms.form_menu_jugador import menu_jugador


class App:
    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("inicio de sesion")#Nombre de la ventana
        self.ventana.geometry("1250x480")#Tamaño de la ventana
        self.ventana.config(bg='#fcfcfc')#Color de la ventan 
        self.ventana.resizable(width=0, height=0)#Bloqueo de maximizar ventana

        imagen_sesion = ImageTk.PhotoImage(Image.open('./img/fondo_login.png'))
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

        cambiar_contraseña = tk.Button(text="Cambiar contraseña", font=("Times",10), bg="red")
        cambiar_contraseña.pack(pady=15)

        inicio = tk.Button(text="Entrar", font=("Times",14), fg="#fcfcfc", bg="#8A169E", command= self.verificar)
        inicio.pack(pady=15)

        Registrarse = tk.Button(text="Registrarse", font=("Times",14), bg="#FFFFFF", command=self.registrar)
        Registrarse.pack(pady=15)

        self.ventana.mainloop()
    def verificar(self):
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
        if (usuario == "root" and contraseña == "1234"):
            self.ventana.destroy()
            menu_jugador()
        
        else:
            messagebox.showerror(message="Usuario o contraseña incorrecta")
    
    def registrar(self):
        #Destruye la ventana anterior
        self.ventana.destroy()

        #Generar ventana
        self.ventana_registro = tk.Tk()
        self.ventana_registro.title("Registro")
        self.ventana_registro.geometry("1200x800")
        self.ventana_registro.config(bg="#fcfcfc")

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
        Registrars= tk.Button(text="Registrarse", font=("Times",14), bg="#FFFFFF", command=lambda:obj.nuevo_registro(self.usuario_registro.get(),self.apodo_registro.get(),self.contraseña_registro.get()))
        Registrars.pack(pady=15)
        


        #imagen_registro = ImageTk.PhotoImage(Image.open('./img/fondo_registro.png'))
        #lable_registro = tk.Label(image=imagen_registro)
        #lable_registro.pack()

        self.ventana_registro.mainloop()