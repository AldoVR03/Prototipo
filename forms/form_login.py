import tkinter as tk 
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from db.data import *
from forms.form_menu_jugador import menu_jugador
from forms.form_menu_gm import menu_gm
from tkinter.ttk import Progressbar



class App:
    def __init__(self):
        # self.ventana = tk.Tk()
        self.mostrarVentanaInicioSesion()
        
    def mostrarVentanaInicioSesion(self):

        self.ventana = tk.Tk()
        self.ventana.title("inicio de sesion")#Nombre de la ventana
        self.ventana.geometry("1200x500")#Tamaño de la ventana
        self.ventana.config(bg='#fcfcfc')#Color de la ventan 
        self.ventana.resizable(width=0, height=0)#Bloqueo de maximizar ventana

        self.createProgressBar()
        
        imagen_sesion = ImageTk.PhotoImage(Image.open('./img/fondo_login.png'))
        label_sesion = tk.Label(image=imagen_sesion)
        label_sesion.pack(side="right")

        titulo = tk.Label(text="Inicio de sesión", bg="#FFFFFF",font=("Times", 14))
        titulo.pack(padx=5,pady=20)

        etiqueta_usuario = tk.Label(text="Usuario",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_usuario.pack(pady=5)
        self.usuario = tk.Entry(font=("Times",14))
       
        self.usuario.pack()

        etiqueta_contraseña = tk.Label(text="Contraseña",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_contraseña.pack()
        self.contraseña = tk.Entry(font=("Times",14))
        self.contraseña.pack()
        self.contraseña.config(show="*")

        cambiar_contraseña = tk.Button(text="Cambiar contraseña", font=("Times",10), bg="red", command=self.cambio_clave)
        cambiar_contraseña.pack(pady=15)

        opcion = tk.IntVar()
        r1=tk.Radiobutton(text="jugador", variable=opcion, value=1, bg="#FFFFFF", font=("Times",14)).pack()
        r2=tk.Radiobutton(text="gm", variable=opcion, value=2,bg="#FFFFFF",font=("Times",14)).pack() 
        
        inicio = tk.Button(
                           text="Entrar", 
                           font=("Times",14), 
                           fg="#fcfcfc", 
                           bg="#8A169E", 
                           command=lambda:
                           self.verificarInicioSesion( self.usuario.get(),self.contraseña.get(), opcion.get()) 
                          )
        inicio.pack(pady=15)

        # opcion = tk.StringVar()

        #opcion = tk.IntVar()

        # tk.Radiobutton(text="jugador", variable=opcion, value=1, bg="#FFFFFF").pack()
        # tk.Radiobutton(text="gm", variable=opcion, value=2,bg="#FFFFFF").pack() 

        
        Registrarse = tk.Button(text="Registrarse", font=("Times",14), bg="#FFFFFF", command=self.registrar)
        Registrarse.pack(pady=15)

        salida = tk.Button(text="Salir",font=("Times",14), bg="#FFFFFF", command=self.ventana.destroy)
        salida.pack()

        self.ventana.mainloop()
        
    def verificarInicioSesion(self, usuario1, contraseña1,tipoUsuario):
        #existeUsuario = obj.existeUsuario(usuario1, contraseña1) #RETORNA UN BOOLEANO DEPENDIENDO DE LA EXISTENCIA DEL USUARIO EN LA BD
        if (tipoUsuario == 1):  #SI ES 1 ENTRA AQUI
            existeUsuario = obj.existeJugador(usuario1, contraseña1)
            print(existeUsuario)
            if( usuario1 == "" and contraseña1 == "" ):
                messagebox.showerror(message="Usuario o contraseña incorrecta")
            else:
                
                if(existeUsuario):
                    if (existeUsuario !=None):
                        self.ventana.destroy()
                        menu_jugador()
                    else:
                        messagebox.showerror(message="No existe el usuario proporcionado")
                else:
                    messagebox.showerror(message="No existe el jugador ingresado")

        elif (tipoUsuario==2):
            existeUsuario = obj.existeGm(usuario1, contraseña1)
            print(existeUsuario)
            if( usuario1 == "" and contraseña1 == "" ):
                messagebox.showerror(message="Usuario o contraseña incorrecta")
            else:
                
                if(existeUsuario):
                    if (existeUsuario !=None):
                        self.ventana.destroy()
                        menu_gm()
                    else:
                        messagebox.showerror(message="No existe el usuario proporcionado")
                else:
                    messagebox.showerror(message="No existe el GM ingresado")
        else:
            messagebox.showerror(message="Seleccione el tipo usuario")
            

        # 1-JUGADOR 2-GM
    def createProgressBar(self):
        xd = ttk.Style()
        xd.theme_use('clam')
        xd.configure("red.Horizontal.TProgressbar", foreground='red', background='blue')
        p = Progressbar(style="red.Horizontal.TProgressbar",orient="horizontal",length=500,mode="determinate",takefocus=True,maximum=1000)
        p.pack(padx=50, pady=50)            
        for i in range(1000):                
            p.step()            
            self.ventana.update()
        p.destroy()

        
    def verificarRegistro(self,usuario,apodo,clave, ventana):
        if( usuario == "" and apodo == "" and clave == "" ):
            messagebox.showerror(message="Datos no ingresados")
        else:
            obj.nuevo_registro(usuario,apodo,clave)
            ventana.destroy()   
            self.mostrarVentanaInicioSesion()
    
    def cambio_clave(self):

        #Destruye la ventana anterior
        self.ventana.destroy()
        #Generar ventana
        self.ventana_cambio_clave = tk.Tk()
        self.ventana_cambio_clave.title("Cambio de contraseña")
        self.ventana_cambio_clave.geometry("1200x500")
        # self.ventana_cambio_clave.config(bg="#fcfcfc")

        # frame1 = tk.Frame(self.ventana_cambio_clave, bg="#79E018", width=400,height=400).place( x=0,y=0)


        # imagen = Image.open("./img/fondo_login.png")  
        # imagen = imagen.resize((200, 200))  
        # imagen_tk = ImageTk.PhotoImage(imagen)


        # label_imagen = tk.Label(self.ventana_cambio_clave, image=imagen_tk)
        # label_imagen.pack()


        etiqueta_usuario_recuperar = tk.Label(text="Ingresa el nombre de usuario",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_usuario_recuperar.pack()
        self.usuario_recuperar = tk.Entry(font=("Times",14))
        self.usuario_recuperar.pack()

        etiqueta_clave_actual = tk.Label(text="Ingrese la clave anterior",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_clave_actual.pack()
        self.clave_actual = tk.Entry(font=("Times",14))
        self.clave_actual.pack()

        etiqueta_clavenueva = tk.Label(text="Ingrese la nueva clave",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_clavenueva.pack()
        self.clave_nueva = tk.Entry(font=("Times",14))
        self.clave_nueva.pack()

        cambiar= tk.Button(text="Cambiar contraseña",
                              font=("Times",14),
                              bg="#FFFFFF",
                              border=0,
                              command=lambda:obj.cambio_contraseña(self.usuario_recuperar.get(), 
                                                                    self.clave_actual.get(),
                                                                    self.clave_nueva.get() 
                                                                    ))
        cambiar.pack(pady=15)

        salida_cambio = tk.Button(text="Volver",font=("Times",14), bg="#FFFFFF", command=lambda:self.termino(self.ventana_cambio_clave))
        salida_cambio.pack()

        

    def registrar(self):


        #Destruye la ventana anterior
        self.ventana.destroy()
        #Generar ventana
        
        self.ventana_registro = tk.Tk()
        self.ventana_registro.title("Registro")
        self.ventana_registro.geometry("1200x500")
        self.ventana_registro.config(bg="#fcfcfc")

        self.createProgressBar()
        
        
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
                                bg="#FFFFFF",
                                command=lambda:self.verificarRegistro(self.usuario_registro.get(),
                                self.apodo_registro.get(),self.contraseña_registro.get(), self.ventana_registro))
        Registrars.pack(pady=15)

        salida_registro = tk.Button(text="Volver",font=("Times",14), bg="#FFFFFF", command=lambda:self.termino(self.ventana_registro))
        salida_registro.pack()
        #imagen_registro = ImageTk.PhotoImage(Image.open('./img/fondo_registro.png'))
        #lable_registro = tk.Label(image=imagen_registro)
        #lable_registro.pack()

        self.ventana_registro.mainloop()
    
    def termino(self,ventana):
        ventana.destroy()
        self.mostrarVentanaInicioSesion()