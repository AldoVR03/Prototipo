import tkinter as tk
import presentacion.constants as cons
from pubsub import pub
from presentacion.personalizacion.customView import CustomView
from logica.PersonalizacionBusinessDelegate import PersonalizacionBusinessDelegate
class ControllerPersonalizacion():

    def __init__(self,root) -> None:
        pub.subscribe(self.eventSubInicio, "INICIO-PERSONALIZACION")
        self.root=root
        self.marcoImage=tk.PhotoImage(file=cons.MARCO_PERSONALIZACION)
        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.x = (self.root.bgWidth - self.ancho_marco) // 2
        self.y = (self.root.bgHeight - self.alto_marco) // 2
        
        self.oCustomView=CustomView(self.root.marcoFrame)
        self.personalizacionBusinessDelegate=PersonalizacionBusinessDelegate()
        # Eventos
        self.oCustomView.customBackBtn.configure(command=self.publishEventPersonlizacion)

        # self.marcoFrame=tk.Frame(self.mainCanvas,width=100,height=100,bg="#8f563b",bd=0)
    def eventSubInicio(self,msg):
        print(f"CONTROLADOR-PERSONALIZACION: SEÑAL RECIBIDA DE {msg}")
        # self.root.setImage("images/marco-354x220_200%.png")
        # self.root.marcoFrame.config(width=500,height=500)
        self.show()

    def publishEventPersonlizacion(self):
        msg="CONTROLADOR-PERSONALIZACION"
        pub.sendMessage("PERSONALIZACION-INICIO",msg=msg)

    def show(self):
        self.root.mainCanvas.pack()
        self.root.mainCanvas.create_image(0, 0, anchor="nw", image=self.root.backgroundImage)
        self.root.mainCanvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)
        self.root.marcoFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.oCustomView.show()
        

    