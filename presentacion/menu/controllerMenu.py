from pubsub import pub
import tkinter as tk
from presentacion.menu.menuView import MenuView
from presentacion.menu.SelectionView import SelectionView

class ControllerMenu():
    def __init__(self,root) -> None:
        pub.subscribe(self.receiveNewPlayers, "NEW-PLAYER")
        pub.subscribe(self.receiveNoNewPlayers, "NO-NEW-PLAYER")
        
        self.jugadorHandler=None
        self.window=root
        # self.canvas=tk.Canvas(self.window.root, width=self.window.bgWidth, height=self.window.bgHeight,bd=0,borderwidth=0,highlightthickness=0)
        self.bgImage=root.backgroundImage
    
        self.oMenuView=MenuView(self.window.root)
        self.oSelectionView=SelectionView(self.window.root)
        

        # Eventos
        self.oSelectionView.backSelectionBtn.config(command=self.toLogin)
        self.oSelectionView.contBtn.config(command=self.toMenu)
    
    def show(self):
        self.oMenuView.show()
        # pass
    def toLogin(self):
        self.oSelectionView.canvas.pack_forget()
        self.jugadorHandler=None
        msg="Hola"
        pub.sendMessage("SELECCION-INICIO",msg=msg)
    def toMenu(self):
        self.oSelectionView.canvas.pack_forget()
        self.oMenuView.canvas.pack()
        self.oMenuView.show()
        
    def eventSubInicio(self,msg):
        print("CONTROLADOR-MENU: SEÑAL RECIBIDA")
    
    def receiveNewPlayers(self,msg):
        print("CONTROLADOR-MENU: HE RECIBIDO EL MENSAJE PARA NUEVOS JUGADORES")
        self.show()
        self.jugadorHandler=msg
        

    def receiveNoNewPlayers(self,msg):
        print("CONTROLADOR-MENU: HE RECIBIDO EL MENSAJE PARA NO NUEVOS JUGADORES")
        self.oSelectionView.show()
        self.jugadorHandler=msg
        self.oSelectionView.setCharacters(self.jugadorHandler.getJugadorObject().getPersonajes())
        colors=self.getCharacterColors(self.oSelectionView.characterList)
        self.oSelectionView.showPlayerCharacters(len(self.oSelectionView.characterList),colors)
        print(vars(self.jugadorHandler.getJugadorObject()))
        

    def getCharacterColors(self,characterObjects):
        # print(vars(characterObjects[0]))
        colorDict={}
        colorList=[]
        for i,obj in enumerate(characterObjects):
            colorDict["HAIRCOLOR"]=obj.getHairColor()
            colorDict["SKINCOLOR"]=obj.getSkinColor()
            colorDict["EYECOLOR"]=obj.getEyeColor()
            colorList.append(colorDict)
            colorDict={}
        return colorList



