import tkinter as tk
from tkinter import messagebox
from pubsub import pub
from presentacion.inicio.loginView import *
from presentacion.inicio.signInView import *
from presentacion.inicio.passwordView import *
import re
from logica.userHandler import JugadorHandler
from logica.businessDelegate import InicioBusinessDelegate
class ControllerInicio():
    def __init__(self,p1) -> None:
        pub.subscribe(self.selectionToLogin, "SELECCION-INICIO")
        pub.subscribe(self.eventSubPersonalizacion, "PERSONALIZACION-INICIO")
        self.jugadorHandler=JugadorHandler()
        self.businessDelegate=InicioBusinessDelegate()
        self.marcoFrame=p1.marcoFrame
        # self.contentFrame=p1.contentFrame
        self.mainCanvas=p1.mainCanvas
        self.backgroundImage=p1.backgroundImage
        # self.marcoImage=p1.marcoImage
        # self.x=p1.x
        # self.y=p1.y

        self.oLogin=LoginView(self.marcoFrame)
        self.oRegistro=SignInView(self.marcoFrame)
        self.oPassword=PasswordView(self.marcoFrame)

        style=ttk.Style()
        style.configure("TRadiobutton",
                    background="#8f563b")
        
        self.marcoImage=tk.PhotoImage(file=consts.MARCO_INICIO)
        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.x = (p1.bgWidth - self.ancho_marco) // 2
        self.y = (p1.bgHeight - self.alto_marco) // 2
        # self.marcoFrame=tk.Frame(self.mainCanvas,width=100,height=100,bg="#8f563b",bd=0)
        
        # Login
        self.oLogin.loginBtn.configure(command=self.publishEventInicio)
        self.oLogin.loginSignInBtn.configure(command=lambda:self.changeMainView("R"))
        self.oLogin.loginPasswordBtn.configure(command=lambda:self.changeMainView("P"))
        # SignIn
        self.oRegistro.signInBtn.configure(command=self.registerUser)
        self.oRegistro.signInBackBtn.configure(command=lambda:self.changeSecondaryViews("R"))
        # Password
        self.oPassword.passwordBackBtn.configure(command=lambda:self.changeSecondaryViews("P"))
        self.contentFrame=self.oLogin.loginFrame


        

    def showLoginFrame(self):
        self.hideFrames()
        self.mainCanvas.pack()
        self.mainCanvas.create_image(0, 0, anchor="nw", image=self.backgroundImage)
        self.mainCanvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)
        self.marcoFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.contentFrame.pack()
        self.oLogin.show()     

    def showSignInFrame(self):
        self.hideFrames()
        # self.contentFrame.pack()
        self.oRegistro.show()

    def showPasswordFrame(self):
        self.hideFrames()
        # self.contentFrame.pack()
        self.oPassword.show()

    def hideFrames(self):
        self.oLogin.loginFrame.pack_forget()
        self.oRegistro.signInFrame.pack_forget()
        self.oPassword.passwordFrame.pack_forget()

    def changeMainView(self,view):
        
            
        if(view=="R"):
            # self.contentFrame.pack_forget()
            # self.contentFrame=self.oRegistro.signInFrame
            self.oLogin.hide()
            self.showSignInFrame()
        elif(view=="P"):
            # self.contentFrame.pack_forget()
            # self.contentFrame=self.oPassword.passwordFrame
            self.showPasswordFrame()
            
    def changeSecondaryViews(self,view):
        if(view=="R"):
            self.contentFrame.pack_forget()
            self.contentFrame=self.oLogin.loginFrame
            self.showLoginFrame()
        elif(view=="P"):
            self.contentFrame.pack_forget()
            self.contentFrame=self.oLogin.loginFrame
            self.showLoginFrame()

    def publishEventInicio(self):
        userType=self.oLogin.radioVar.get()
        username=self.oLogin.usernameEntry.get()
        password=self.oLogin.passwordEntry.get()

        if(username == "" or password == ""):
            return
        if(self.validarDatos(self.oLogin.usernameEntry.get(),self.oLogin.passwordEntry.get())):
            # print("este",self.autenticarDatos(username,password,userType))
            if( self.autenticarDatos(username,password,userType)):
                if(userType==2):
                     pass
                    # Va directamente al menu
                    
                else:
                    #  si tiene como mínimo un personaje va directo al menu
                    #  si tiene cero personajes se le lleva a crear un personaje
                    if(self.hasCharacter()):
                        
                        print("Selección de personajes")  #Jugador con un personaje como mínimo
                        self.mainCanvas.pack_forget()
                        pub.sendMessage("NO-NEW-PLAYER",msg=self.jugadorHandler)                        
                    else:
                        print("Personalización del primer personaje") #Jugador con cero personajes
                        msg=["CONTROLADOR-INICIO",self.jugadorHandler]
                        self.oLogin.loginFrame.pack_forget()
                        self.mainCanvas.pack_forget()
                        pub.sendMessage("INICIO-PERSONALIZACION", msg=msg)
                        
            else:
                messagebox.showwarning("Advertencia","Nombre de usuario o contraseña incorrecta")
        else:
                messagebox.showerror("Error","No se cumplen las restricciones")
                return False

    def eventSubPersonalizacion(self, msg):
         print(f'CONTROLADOR-INICIO: SEÑAL RECIBIDA DE {msg}')
         self.jugadorHandler=None
         self.showLoginFrame()
         
    def validarDatos(self,username,password):
            pattern= r'^[a-zA-Z0-9_]*$'
            if(re.match(pattern,username) is not None and re.match(pattern,password) is not None ):
                return True
            return False
    
    def autenticarDatos(self,username, password,userType):
            if userType==2: 
                self.businessDelegate.setServiceType("GM")
            else:
                self.businessDelegate.setServiceType("JUGADOR")
            # print(self.businessDelegate.serviceType)
            return self.businessDelegate.checkUser(username, password)
    
    def hasCharacter(self):
         return self.businessDelegate.hasCharacter()
    
    def registerUser(self):
        print("JAJA")
        username=(self.oRegistro.signInUsernameEntry.get())
        nickname=(self.oRegistro.signInNicknameEntry.get())
        password=(self.oRegistro.signInPasswordEntry.get())
        userType=(self.oRegistro.radioVar.get())
        if(username == "" or password == "" or nickname == "" or len(username) <7 or len(nickname) <7 or len(password) <7):
            return
        if(self.validarDatosRegistro(username,nickname,password)):
            if(self.autenticarDatosRegistro(username,nickname,userType)):
                messagebox.showinfo("Info", "El usuario ya existe")
            else:
                print(":)")
                if(self.businessDelegate.registerUser(username,nickname,password)):
                    messagebox.showinfo("Info", "Registro éxitoso!!!")
    def validarDatosRegistro(self,username,nickname, password):
        pattern= r'^[a-zA-Z0-9_]*$'
        if(re.match(pattern,username) is not None and re.match(pattern,password) is not None and re.match(pattern,password) is not None ):
            return True
        return False
    def autenticarDatosRegistro(self, username, nickname,userType):
        if userType ==2:
            self.businessDelegate.serviceType="GM"
        else:
            self.businessDelegate.serviceType="JUGADOR"
        return self.businessDelegate.checkRegisterUser(username,nickname)
    


    def selectionToLogin(self,msg):
        self.showLoginFrame()

    
         
         
            