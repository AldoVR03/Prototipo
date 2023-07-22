import tkinter as tk
import presentacion.constants as consts
# from presentacion.inicio.loginView import *
# from presentacion.inicio.signInView import *
# from presentacion.inicio.passwordView import *
from presentacion.inicio.controllerInicio import *
from presentacion.personalizacion.controllerPersonalizacion import *



# Obtener las dimensiones de la imagen del marco

class App():
    def __init__(self) -> None:
        self.root=tk.Tk()
        self.root.config(bg="black")
        
        self.contentFrame=None
        self.root.resizable(False,False)
        # Main canvas
        self.backgroundImage=tk.PhotoImage(file=consts.FONDO_INICIO)
        self.bgWidth = self.backgroundImage.width()
        self.bgHeight = self.backgroundImage.height()
  
        self.mainCanvas=tk.Canvas(self.root, width=self.bgWidth, height=self.bgHeight,bd=0,borderwidth=0,highlightthickness=0)
        # Marco canvas
        # self.marcoImage=tk.PhotoImage(file=consts.MARCO_INICIO)
        # self.ancho_marco = self.marcoImage.width()
        # self.alto_marco = self.marcoImage.height()
        # self.x = (self.bgWidth - self.ancho_marco) // 2
        # self.y = (self.bgHeight - self.alto_marco) // 2
        self.marcoFrame=tk.Frame(self.mainCanvas,width=100,height=100,bg="black",bd=0)
        self.pos_x = (self.root.winfo_screenwidth() // 2) - (self.bgWidth // 2)
        self.pos_y = (self.root.winfo_screenheight() // 2) - (self.bgHeight // 2)
        self.root.geometry(f"{self.bgWidth}x{self.bgHeight}+{self.pos_x}+{self.pos_y}")
    def setImage(self,a):
        self.marcoImage=tk.PhotoImage(file=a)
        self.ancho_marco=self.marcoImage.width()
        self.alto_marco=self.marcoImage.height()
        self.x = (self.bgWidth - self.ancho_marco) // 2
        self.y = (self.bgHeight - self.alto_marco) // 2
        
    
p1=App()
# p1.showLoginFrame()
oControllerInicio=ControllerInicio(p1)
oControllerPersonalizacion=ControllerPersonalizacion(p1)
oControllerMenu=None
oControllerInicio.showLoginFrame()
# p1.showSignInFrame()
p1.root.mainloop()