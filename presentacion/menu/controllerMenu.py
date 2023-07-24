from pubsub import pub
import tkinter as tk
from presentacion.menu.menuView import MenuView
from presentacion.menu.SelectionView import SelectionView
from presentacion.menu.tiendaView import TiendaView
from presentacion.menu.libroView import LibroView
from presentacion.menu.clanView import ClanView
from tkinter import messagebox
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
        self.oClanView=ClanView(self.window.root)

        # Eventos
        self.oSelectionView.backSelectionBtn.config(command=lambda:self.toLogin("SELECTION"))
        self.oSelectionView.contBtn.config(command=lambda:self.toMenu("SELECTION"))
        self.oMenuView.salirBtn.config(command=lambda:self.toLogin("MENU"))
        self.oMenuView.canvas.tag_bind(self.oMenuView.tiendaImageReference, "<Button-1>", self.changeView)
        self.oMenuView.libroBtn.config(command=self.toLibro)
        self.oLibroView.viewDict["User"].backBtn.configure(command=lambda:self.toMenu("LIBRO"))
        self.oTiendaView.counterComponent.backBtn.config(command=lambda:self.toMenu("TIENDA"))
        self.oMenuView.clanBtn.config(command=self.toClan)
        self.oClanView.viewDict["Clan"].backBtn.configure(command=lambda:self.toMenu("CLAN"))
        self.oSelectionView.createCharacterBtn.config(command=self.toCustomCharacter)
        # Otros
        self.getCanvasList()
        self.selectedItem=None
    def show(self):
        self.oMenuView.show()
        # pass
    def toCustomCharacter(self):
        # print(self.jugadorHandler.getJugadorObject().getId())
        if len(self.jugadorHandler.getJugadorObject().getPersonajes()) >=4:
            messagebox.showerror("Personajes máximos alcanzados","No puedes crear más personajes")
        else:
            
            self.oSelectionView.canvas.pack_forget()
            msg=self.jugadorHandler
            self.oSelectionView.isSelected=None
            pub.sendMessage("SELECT-PERSONALIZACION",msg=msg)
    def toClan(self):
        self.oMenuView.canvas.pack_forget()
        self.oClanView.show()
    def toLibro(self):
        
            self.oMenuView.canvas.pack_forget()
            self.oLibroView.show()
        
    def toLogin(self,location):
        self.oSelectionView.isSelected=None
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
            
            self.jugadorHandler.setSelectedCharacter(self.oSelectionView.selectedCharacter)

            # print(vars(self.jugadorHandler.getSelectedCharacter()))
            self.oSelectionView.isSelected=None
    
            self.oSelectionView.canvas.pack_forget()
            print("Personaje seleccionado: ",self.oSelectionView.selectedCharacter)
        elif location=="TIENDA":
            # self.oTiendaView.hide()
            self.oTiendaView.canvas.pack_forget()
            # self.oTiendaView.counterComponent.hide()
            # self.oTiendaView.mainFrame.pack_forget()
        elif location=="LIBRO":
            self.oLibroView.canvas.pack_forget()
        elif location == "CLAN":
            self.oClanView.canvas.pack_forget()
            

        self.oMenuView.canvas.pack()
        self.oMenuView.show()
        
    def eventSubInicio(self,msg):
        print("CONTROLADOR-MENU: SEÑAL RECIBIDA")
    
    def receiveNewPlayers(self,msg):
        print("CONTROLADOR-MENU: HE RECIBIDO EL MENSAJE PARA NUEVOS JUGADORES")
        self.show()
        self.jugadorHandler=msg
        

    def receiveNoNewPlayers(self,msg):
        # print("CONTROLADOR-MENU: HE RECIBIDO EL MENSAJE PARA NO NUEVOS JUGADORES")
        print(self.oSelectionView.selectedCharacter)
        print(self.oSelectionView.characterList)
        # print(self.oSelectionView.s)
        self.oSelectionView.show()
        self.jugadorHandler=msg
        self.oSelectionView.setCharacters(self.jugadorHandler.getJugadorObject().getPersonajes())
        colors=self.getCharacterColors(self.oSelectionView.characterList)
        self.oSelectionView.showPlayerCharacters(len(self.oSelectionView.characterList),colors)
        print("ASOCIACIONES: ",self.oSelectionView.relateCanvasPersonaje)
        # print(vars(self.jugadorHandler.getJugadorObject()))
        

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
    def setExp(self):
        self.oMenuView.leftBarFrame()


    # TIENDA
    def getCanvasList(self):
        objectComList=self.oTiendaView.managerFrame.objectCompList
        for elem in objectComList:
            for canvasElem in (objectComList[elem].canvasList):
                
                canvasElem.bind("<Button-1>", self.on_canvas_click)
                canvasElem.bind("<Enter>", self.on_canvas_enter)
                canvasElem.bind("<Leave>", self.on_canvas_leave)
            print()
        print("PRUEBA:",objectComList["Todos"].canvasList[0] is objectComList["Armas"].canvasList[1])
            
        
    def on_canvas_click(self,event):
        print(f"Clic en el canvas {event.widget}")
        self.selectedItem=event.widget
        self.show_clicked_canvas()
        

    def on_canvas_enter(self,event):
        event.widget.config(cursor="hand2")

    def on_canvas_leave(self,event):
        event.widget.config(cursor="")
    def show_clicked_canvas(self):
    # Obtener la imagen del canvas pulsado
        # image = self.selectedItem.create_image(0, 0, anchor="nw", image=self.imageList[index])

        # Crear un nuevo canvas en otro lugar y mostrar la imagen del canvas pulsado
        self.oTiendaView.canvasObject = self.selectedItem
       
        self.oTiendaView.canvasObject.pack()


