import tkinter as tk 
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from forms.form_menu_jugador import menu_jugador

class App:
    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("inicio de sesion")#Nombre de la ventana
        self.ventana.geometry("1250x480")#Tamaño de la ventana
        self.ventana.config(bg='#fcfcfc')#Color de la ventan 
        self.ventana.resizable(width=0, height=0)#Bloqueo de maximizar ventana

        imagen = ImageTk.PhotoImage(Image.open('./img/fondo_login.png'))
        label = tk.Label(image=imagen)
        label.pack(side="right")

        titulo = tk.Label(text="Inicio de sesión", bg="#FFFFFF",font=("Times", 14))
        titulo.pack(padx=5,pady=40)

        etiqueta_usuario = tk.Label(text="Usuario",font=("Times",14),height=3, bd=0,bg="#fcfcfc")
        etiqueta_usuario.pack(pady=5)
        self.usuario = tk.Entry(font=("Times",14))
        self.usuario.pack()

        etiqueta_contraseña = tk.Label(text="Contraseña",font=("Times",14),height=3,bg="#fcfcfc")
        etiqueta_contraseña.pack()

        self.contraseña = tk.Entry(font=("Times",14))
        self.contraseña.pack()
        self.contraseña.config(show="*")

        inicio = tk.Button(text="Entrar", font=("Times",14), fg="#fcfcfc", bg="#8A169E", command= self.verificar)
        inicio.pack(pady=25)


        self.ventana.mainloop()
    def verificar(self):
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
        if (usuario == "root" and contraseña == "1234"):
            self.ventana.destroy()
            menu_jugador
        
        else:
            messagebox.showerror(message="Usuario o contraseña incorrecta")