from pubsub import pub
import tkinter as tk
from presentacion.menu.menuView import MenuView
from presentacion.menu.SelectionView import SelectionView
from presentacion.menu.tiendaView import TiendaView
from presentacion.menu.libroView import LibroView
import time

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
        self.oTiendaView=TiendaView(self.window.root)
        self.oLibroView=LibroView(self.window.root)

        # Eventos
        self.oSelectionView.backSelectionBtn.config(command=lambda:self.toLogin("SELECTION"))
        self.oSelectionView.contBtn.config(command=lambda:self.toMenu("SELECTION"))
        self.oMenuView.salirBtn.config(command=lambda:self.toLogin("MENU"))
        self.oMenuView.canvas.tag_bind(self.oMenuView.tiendaImageReference, "<Button-1>", self.changeView)
        self.oMenuView.libroBtn.config(command=self.toLibro)
        self.oLibroView.viewDict["User"].backBtn.configure(command=lambda:self.toMenu("LIBRO"))
        self.oTiendaView.counterComponent.backBtn.config(command=lambda:self.toMenu("TIENDA"))
        
    def show(self):
        self.oMenuView.show()
        # pass

    def toLibro(self):
        self.oMenuView.canvas.pack_forget()
        self.oLibroView.show()
    def toLogin(self,location):
        if(location=="SELECTION"):
            self.oSelectionView.canvas.pack_forget()
            time.sleep(1)
        elif(location=="MENU"):
            self.oMenuView.canvas.pack_forget()
            time.sleep(2)
        self.jugadorHandler=None
        msg="Hola"
        pub.sendMessage("SELECCION-INICIO",msg=msg)
    def toMenu(self, location):
        if location =="SELECTION":
            self.jugadorHandler.setSelectedCharacter(self.oSelectionView.selectCharacter)
            print(vars(self.jugadorHandler.getSelectedCharacter()))
            self.oSelectionView.canvas.pack_forget()
        elif location=="TIENDA":
            # self.oTiendaView.hide()
            self.oTiendaView.canvas.pack_forget()
            # self.oTiendaView.counterComponent.hide()
            # self.oTiendaView.mainFrame.pack_forget()
        elif location=="LIBRO":
            self.oLibroView.canvas.pack_forget()
            
            

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
    
    def changeView(self, event):
        # canvas=event.widget
        # canvas.itemconfigure(canvas.find_withtag("image_tag")[0], image=self.oMenuView.tiendaImageOver) 
        # self.oMenuView.isSelected=(canvas,canvas.find_withtag("image_tag")[0])
        self.oMenuView.canvas.pack_forget()


        self.oTiendaView.canvas.pack()
        self.oTiendaView.show()
        
        print("Hey you!!")



