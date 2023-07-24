import tkinter as tk
from tkinter.colorchooser import askcolor
import presentacion.constants as cons
from pubsub import pub
from presentacion.personalizacion.customView import CustomView
from logica.PersonalizacionBusinessDelegate import PersonalizacionBusinessDelegate
class ControllerPersonalizacion():

    def __init__(self,window) -> None:
        pub.subscribe(self.eventSubInicio, "INICIO-PERSONALIZACION")
        pub.subscribe(self.fromSelection, "SELECT-PERSONALIZACION")
        self.window=window
        self.root=self.window.root
        self.canvas=tk.Canvas(self.root, width=self.window.bgWidth, height=self.window.bgHeight,bd=0,borderwidth=0,highlightthickness=0)
        
        self.marcoImage=tk.PhotoImage(file=cons.MARCO_PERSONALIZACION)
        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.x = (self.window.bgWidth - self.ancho_marco) // 2
        self.y = (self.window.bgHeight - self.alto_marco) // 2

        self.jugadorHandler=None
        self.oCustomView=CustomView(self.canvas)
        self.personalizacionBusinessDelegate=PersonalizacionBusinessDelegate()
        # Eventos
        self.oCustomView.saveBtn.configure(command=self.sendNewPlayerToMenu)
        self.oCustomView.customBackBtn.configure(command=self.publishEventPersonlizacion)
        self.oCustomView.changeHairColorBtn.configure(command=self.changeHairColor)
        self.oCustomView.changeEyesColorBtn.configure(command=self.changeEyeColor)
        self.oCustomView.radioComponent.radiobutton1.configure(command=self.changeSkinColor)
        self.oCustomView.radioComponent.radiobutton2.configure(command=self.changeSkinColor)
        self.oCustomView.radioComponent.radiobutton3.configure(command=self.changeSkinColor)
        self.oCustomView.radioComponent.radiobutton4.configure(command=self.changeSkinColor)
        self.oCustomView.radioComponent.radiobutton5.configure(command=self.changeSkinColor)
        # self.marcoFrame=tk.Frame(self.mainCanvas,width=100,height=100,bg="#8f563b",bd=0)
        # self.root.mainCanvas.create_image(0, 0, anchor="nw", image=self.root.backgroundImage)
        self.fondoImageReference=self.canvas.create_image(0, 0, anchor="nw", image=self.window.backgroundImage)
        self.marcoImageReference=self.canvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)
    

      
    def eventSubInicio(self,msg):
        print(f"CONTROLADOR-PERSONALIZACION: SEÑAL RECIBIDA DE {msg[0]}")
        # self.root.setImage("images/marco-354x220_200%.png")
        # self.root.marcoFrame.config(width=500,height=500)
        self.jugadorHandler=msg[1]
        print(vars(self.jugadorHandler.getJugadorObject()))
        self.show()
    def fromSelection(self,msg):
        self.jugadorHandler=msg
        self.canvas.pack()
        self.oCustomView.show()

    def publishEventPersonlizacion(self):
        msg="CONTROLADOR-PERSONALIZACION"
        # self.oCustomView.hide()
        self.canvas.pack_forget()
        self.jugadorHandler.setJugadorObject(None)
        self.oCustomView.personajeComponent.resetColors()
        pub.sendMessage("PERSONALIZACION-INICIO",msg=msg)
    
    def sendNewPlayerToMenu(self):
        nombrePersonaje=(self.oCustomView.nombrePersonajeEntry.get())
        raza=(self.oCustomView.razaPersonajeCombobox.get())
        clase=(self.oCustomView.clasePersonajeCombobox.get())
        currentColors=(self.oCustomView.personajeComponent.getCurrentColors())
        print(currentColors)
        print(self.jugadorHandler.getJugadorObject().getId())
        if(len(self.oCustomView.nombrePersonajeEntry.get())>=8):
            pub.sendMessage("NEW-PLAYER",msg=self.jugadorHandler)
            self.canvas.pack_forget()
            self.personalizacionBusinessDelegate.setServiceType("PERSONAJE")
            
            if(self.personalizacionBusinessDelegate.saveCharacter(self.jugadorHandler.getJugadorObject().getId(),nombrePersonaje,raza,clase,currentColors["PELO"],currentColors["PIEL"],currentColors["OJOS"])):
                print("Personaje guardado con éxito!!")
                # Enviar al menu
                # self.oCustomView.hide()
                # self.canvas.pack_forget(
                self.personalizacionBusinessDelegate.getCharacters(self.jugadorHandler.getJugadorObject().getId())
                
            else:
                print("No se ha podido guardar")

        else:
            print("Mínimo 8 caracteres")
    def changeHairColor(self):
        hairColor=askcolor()[0]
        if hairColor==None:
            return
        self.oCustomView.personajeComponent.setColorPelo(hairColor)
        print(hairColor)
        self.oCustomView.personajeComponent.cambiarColorParte(self.oCustomView.personajeComponent.getPeloId(),
                                                              self.oCustomView.personajeComponent.RUTA_IMAGEN_PELO,hairColor)
    def changeEyeColor(self):
        eyeColor=askcolor()[0]
        print(self.oCustomView.radioComponent.selection)
        if eyeColor==None:
            return
        self.oCustomView.personajeComponent.setColorOjos(eyeColor)
        
        self.oCustomView.personajeComponent.cambiarColorParte(self.oCustomView.personajeComponent.getOjosId(),
                                                              self.oCustomView.personajeComponent.RUTA_IMAGEN_OJOS,eyeColor)
        
    def changeSkinColor(self):
        skinColor=tuple([int(value) for value in self.oCustomView.radioComponent.selection.get().split(",")])
        print(skinColor)
        if skinColor==None:
            return
        
        self.oCustomView.personajeComponent.setColorPiel(skinColor)
        
        self.oCustomView.personajeComponent.cambiarColorParte(self.oCustomView.personajeComponent.getCuerpoId(),
                                                              self.oCustomView.personajeComponent.RUTA_IMAGEN_CUERPO,skinColor)
    
    def show(self):
        print("HOLA")
        self.canvas.pack()
        self.window.marcoFrame.place(relx=0.5, rely=0.5, anchor="center")
 
        self.oCustomView.show()
        

    