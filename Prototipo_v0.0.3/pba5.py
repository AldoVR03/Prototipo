import tkinter as tk
from loginView import *
from signInView import *
from passwordView import *
from controllerInicio import *


# Obtener las dimensiones de la imagen del marco

class App():
    def __init__(self) -> None:
        self.root=tk.Tk()
        self.root.config(bg="black")
        self.contentFrame=None
        self.root.resizable(False,False)
        # Main canvas
        self.backgroundImage=tk.PhotoImage(file="./img/fondo_login.gif")
        self.bgWidth = self.backgroundImage.width()
        self.bgHeight = self.backgroundImage.height()
        self.mainCanvas=tk.Canvas(self.root, width=self.bgWidth, height=self.bgHeight,bd=0,borderwidth=0,highlightthickness=0)
        
        self.marcoImage=tk.PhotoImage(file="./img/marco-27X34.png")
        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.x = (self.bgWidth - self.ancho_marco) // 2
        self.y = (self.bgHeight - self.alto_marco) // 2
        self.marcoFrame=tk.Frame(self.mainCanvas,width=100,height=100,bg="black",bd=0)

p1=App()
# p1.showLoginFrame()
oControllerInicio=ControllerInicio(p1)
oControllerInicio.showLoginFrame()
# p1.showSignInFrame()
p1.root.mainloop()