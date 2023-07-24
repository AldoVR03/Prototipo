import tkinter as tk
import presentacion.personalizacion.ImagenPersonajeComponent as personaje
import presentacion.menu.scrollObjectComponent as SOC
import presentacion.constants as cons

class EnemigoComponent:
    def __init__(self,root,rightRoot) -> None:
        self.leftContent=tk.Frame(root)
        self.rightContent=tk.Frame(rightRoot)

        self.topFrame=tk.Frame(self.leftContent,width=100,height=100, bg="red")
        self.bottomFrame=tk.Frame(self.leftContent,width=100,height=100, bg="blue")

        self.topSecFrame=tk.Frame(self.rightContent,width=100,height=100, bg="#cab9a1")
        self.bottomSecFrame=tk.Frame(self.rightContent,width=100,height=100, bg="#cab9a1")
        # personaje
        self.characterFrame=tk.Frame(self.topFrame)
        self.userCharacter=personaje.imagenPersonaje(self.characterFrame, build=False)
        self.userCharacter.setXCoords(60)
        self.userCharacter.setYCoord(-30)
        self.userCharacter.canvas.config(width=120,height=120, bg="#8f563b")
        self.userCharacter.construirPersonaje()

        # Datos personajes
        self.characterDataFrame=tk.Frame(self.topFrame, width=100, height=100, bg="brown")

        # Sec top frame content
        self.inventarioLabel=tk.Label(self.topSecFrame,text="Enemigos")
        # Sec bottom frame content
        self.objectContainer=SOC.ObjectFrameComponent(self.bottomSecFrame,100,[],4,False,tk.PhotoImage(file="images/espadawmarcoMini.png"))
        self.objectContainer.start()
    def show(self):
        self.leftContent.pack()
        self.topFrame.pack(side="top")
        self.bottomFrame.pack(side="bottom")
        
        self.rightContent.pack()
        self.topSecFrame.pack(side="top")
        self.bottomSecFrame.pack(side="bottom")
        self.userCharacter.show()
        self.characterFrame.pack(side="left")
        self.characterDataFrame.pack(expand=True,fill="y")

        
        self.objectContainer.show()

        self.inventarioLabel.pack()
        
class HabilidadComponent:
    def __init__(self, leftRoot, rightRoot) -> None:
        self.leftContent=tk.Frame(leftRoot)
        self.rightContent=tk.Frame(rightRoot)

        self.topFrame=tk.Frame(self.leftContent,width=100,height=100, bg="blue")
        self.bottomFrame=tk.Frame(self.leftContent,width=100,height=100, bg="red")

        self.topSecFrame=tk.Frame(self.rightContent,width=100,height=100, bg="#cab9a1")
        self.bottomSecFrame=tk.Frame(self.rightContent,width=100,height=100, bg="#cab9a1")
        # personaje
        self.characterFrame=tk.Frame(self.topFrame)
        self.userCharacter=personaje.imagenPersonaje(self.characterFrame, build=False)
        self.userCharacter.setXCoords(60)
        self.userCharacter.setYCoord(-30)
        self.userCharacter.canvas.config(width=120,height=120, bg="#8f563b")
        self.userCharacter.construirPersonaje()

        # Datos personajes
        self.characterDataFrame=tk.Frame(self.topFrame, width=100, height=100, bg="brown")

        # Sec top frame content
        self.inventarioLabel=tk.Label(self.topSecFrame,text="Habilidades")
        # Sec bottom frame content
        self.objectContainer=SOC.ObjectFrameComponent(self.bottomSecFrame,100,[],4,False,tk.PhotoImage(file="images/espadawmarcoMini.png"))
        self.objectContainer.start()
    def show(self):
        self.leftContent.pack()
        self.topFrame.pack(side="top")
        self.bottomFrame.pack(side="bottom")
        
        self.rightContent.pack()
        self.topSecFrame.pack(side="top")
        self.bottomSecFrame.pack(side="bottom")
        self.userCharacter.show()
        self.characterFrame.pack(side="left")
        self.characterDataFrame.pack(expand=True,fill="y")

        
        self.objectContainer.show()

        self.inventarioLabel.pack()
        
class MisionComponent:
    def __init__(self, leftRoot, rightRoot) -> None:
        self.leftContent=tk.Frame(leftRoot)
        self.rightContent=tk.Frame(rightRoot)

        self.topFrame=tk.Frame(self.leftContent,width=100,height=100, bg="green")
        self.bottomFrame=tk.Frame(self.leftContent,width=100,height=100, bg="yellow")

        self.topSecFrame=tk.Frame(self.rightContent,width=100,height=100, bg="#cab9a1")
        self.bottomSecFrame=tk.Frame(self.rightContent,width=100,height=100, bg="#cab9a1")
    def show(self):
        self.leftContent.pack()
        self.topFrame.pack(side="top")
        self.bottomFrame.pack(side="bottom")
        
        self.rightContent.pack()
        self.topSecFrame.pack(side="top")
        self.bottomSecFrame.pack(side="bottom")

class UserComponent():
    def __init__(self, leftRoot, rightRoot) -> None:
        self.leftContent=tk.Frame(leftRoot)
        self.rightContent=tk.Frame(rightRoot)

        self.topFrame=tk.Frame(self.leftContent,width=100,height=100, bg="pink")
        self.bottomFrame=tk.Frame(self.leftContent,width=100,height=100, bg="#d9a066")

        self.topSecFrame=tk.Frame(self.rightContent,width=100,height=80, bg="#cab9a1")
        self.bottomSecFrame=tk.Frame(self.rightContent,width=100,height=100, bg="#cab9a1")
        
        self.backBtn=tk.Button(self.bottomFrame,font=cons.FONT_FAMILY2,text="Volver",width=20)
        
        # personaje
        self.characterFrame=tk.Frame(self.topFrame)
        self.userCharacter=personaje.imagenPersonaje(self.characterFrame, build=False)
        self.userCharacter.setXCoords(60)
        self.userCharacter.setYCoord(-30)
        self.userCharacter.canvas.config(width=120,height=120, bg="#8f563b")
        self.userCharacter.construirPersonaje()

        # Datos personajes
        self.characterDataFrame=tk.Frame(self.topFrame, width=100, height=100, bg="brown")

        # Sec top frame content
        self.inventarioLabel=tk.Label(self.topSecFrame,text="Inventario")
        # Sec bottom frame content
        self.objectContainer=SOC.ObjectFrameComponent(self.bottomSecFrame,100,[],4,False,tk.PhotoImage(file="images/espadawmarcoMini.png"))
        self.objectContainer.start()

    def show(self):
        self.leftContent.pack()
        self.topFrame.pack(side="top")
        self.bottomFrame.pack(side="bottom", expand=True, fill="both")
        
        self.rightContent.pack()
        self.topSecFrame.pack(side="top", expand=True, fill="both")
        self.bottomSecFrame.pack(side="bottom")

        self.backBtn.pack()
        self.userCharacter.show()
        self.characterFrame.pack(side="left")
        self.characterDataFrame.pack(expand=True,fill="y")

        
        self.objectContainer.show()

        self.inventarioLabel.pack()
        



