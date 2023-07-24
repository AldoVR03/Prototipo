from tkinter import *
from PIL import ImageTk,Image
from tkinter.colorchooser import askcolor
import presentacion.constants as cons

# def buttonEventHandler(pj):
#     colorNuevo=askcolor()
#     print(colorNuevo)
#     pj.cambiarColorParte(pj.getOjosId(),imagenPersonaje.RUTA_IMAGEN_OJOS, colorNuevo[0]+(255,))

# def buttonEventHandler2(pj):
#     colorNuevo=askcolor()
#     pj.cambiarColorParte(pj.getPeloId(),imagenPersonaje.RUTA_IMAGEN_PELO, colorNuevo[0]+(255,))
COORDS_X=69
COORDS_Y_CUERPO=150
COORDS_Y_PELO=90
COORDS_Y_OJOS=100
COORDS_Y_ROPA=225
class imagenPersonaje():

    #Variables estáticas: son variables que pueden ser accedidas por cualquier objetos
    #También se les conoce como variables de clase
    RUTA_IMAGEN_PELO = ("images/pelo2-removebg-preview.png")
    RUTA_IMAGEN_CUERPO = ("images/cuerpo.png")
    RUTA_IMAGEN_OJOS = ("images/ojos.png")
    RUTA_IMAGEN_ROPA = ("images/ropa.png")
    # 150X
    COORDS_X=90
    COORDS_Y_CUERPO=150
    COORDS_Y_PELO=90
    COORDS_Y_OJOS=100
    COORDS_Y_ROPA=225

    SKIN_COLORS=[{"colorHead":(238,195,154,255),"colorNeck":(231,169,111,255),"colorHand":(231,169,111,255)},
                 {"colorHead":(217,160,102,255),"colorNeck":(203,144,83,255),"colorHand":(203,144,83,255)},
                 {"colorHead":(223,113,38,255),"colorNeck":(186,91,26,255),"colorHand":(186,91,26,255)},
                 {"colorHead":(143,86,59,255),"colorNeck":(125,70,44,255),"colorHand":(125,70,44,255)},
                 {"colorHead":(48,27,23,255),"colorNeck":(72,42,36,255),"colorHand":(72,42,36,255)}]
    #Método constructor
    def __init__(self, frame=None,build=True,canvas=None) -> None:
        if(canvas is  None):
            self.canvas=Canvas(frame,width=130,height=300, bg="#8f563b",bd=0,  highlightthickness=0)
        else:
            self.canvas=canvas
        #Variables donde se encuentran los elementos del canvas. 
        #Estas en uno de sus argumentos hacen referencia a las variables ref de abajo
        #Podemos referirnos a ellos como identificadores. 
        #Por ejemplo, el canvas de esta clase puede tener los siguientes identificadores:
        #Si se llama al metodo canvas.find_all(), se obtiene (1,2,3)
        self.__peloId=None        #|
        self.__cuerpoId=None      #|
        self.__ojosId=None        #|
        self.__ropaId=None        #v
        

        self.coordsx=imagenPersonaje.COORDS_X

        # Referencias a los objetos ImageTk.Photoimage 
        # para que no sean eliminados por el Garbage Collector
        self.__refPelo=None
        self.__refCuerpo=None
        self.__refOjo=None
        self.__refRopa=None

        self.__colorActualPelo=(0,0,0,255)
        self.__colorActualCabeza=(238,195,154,255)
        self.__colorActualCuello=(217,160,102,255)
        self.__colorActualManos=(217,160,102,255)
        self.__colorActualOjos=(0,0,0,255)

        if build:
            self.construirPersonaje()

        self.__colorPelo=(0,0,0,255)
        self.__colorOjos=(0,0,0,255)
        self.__colorPiel=(238,195,154,255)

    def resetColors(self):
        self.__colorPelo=(0,0,0,255)
        self.__colorOjos=(0,0,0,255)
        self.__colorPiel=(238,195,154,255)

        self.construirPersonaje()

    def setColorPelo(self,hairColor):
        self.__colorPelo=hairColor
    
    def setColorOjos(self,eyesColor):
        self.__colorOjos=eyesColor
    
    def setColorPiel(self,skinColor):
        self.__colorPiel=skinColor
    

    def setCanvas(self,canvas):
        self.canvas=canvas
    def getCurrentColors(self):
        return {"PELO":self.__colorPelo,"OJOS":self.__colorOjos,
                "PIEL":self.__colorPiel}
    def setRopa(self,ropaImage=None):
        if(ropaImage is None):
            ropaImage=Image.open(cons.RUTA_IMAGEN_ROPA)
        self.__refRopa=ImageTk.PhotoImage(ropaImage)
        self.__ropaId=self.canvas.create_image(COORDS_X,
                                             COORDS_Y_ROPA,
                                             image=self.__refRopa)
    def setPelo(self,peloImage=None):
        if(peloImage is None):
            peloImage=Image.open(cons.RUTA_IMAGEN_PELO)
        self.__refPelo=ImageTk.PhotoImage(peloImage)
        self.__peloId=self.canvas.create_image(COORDS_X,
                                             COORDS_Y_PELO,
                                             image=self.__refPelo)

    def setCuerpo(self,cuerpoImage=None):
        if(cuerpoImage is None):
            cuerpoImage=Image.open(cons.RUTA_IMAGEN_CUERPO)
        
        self.__refCuerpo=ImageTk.PhotoImage(cuerpoImage)
        self.__cuerpoId=self.canvas.create_image(COORDS_X,
                                               COORDS_Y_CUERPO,
                                               image=self.__refCuerpo)

    def setOjos(self,ojosImage=None):
        if(ojosImage is None):
            ojosImage=Image.open(cons.RUTA_IMAGEN_OJOS)

        self.__refOjo=ImageTk.PhotoImage(ojosImage)
        self.__ojosId=self.canvas.create_image(COORDS_X,
                                             COORDS_Y_OJOS,
                                             image=self.__refOjo)

    def construirPersonaje(self):
        #Adición de imagenes al canvas de la instancia u objeto
        #CAPA INFERIOR-cuerpo
        self.setCuerpo()
        #CAPA MEDIA-ojos
        self.setOjos()
        #CAPA SUPERIOR-pelo
        self.setPelo()
        #CAPA 4
        self.setRopa()

    def getPeloId(self):
        return self.__peloId
    def getOjosId(self):
        return self.__ojosId
    def getCuerpoId(self):
        return self.__cuerpoId
    def getRefOjos(self):
        return self.__refOjo
    
    def determineImage(self, pathImage):
        if(pathImage == cons.RUTA_IMAGEN_OJOS):
            return self.__colorActualOjos
        elif(pathImage == cons.RUTA_IMAGEN_CUERPO):
            return {"cabeza":self.__colorActualCabeza,"cuello":self.__colorActualCuello,"manos": self.__colorActualManos}
        elif(pathImage == cons.RUTA_IMAGEN_PELO):
            return self.__colorActualPelo
        
    def determineSetOfColors(self, colorNuevo):
        for index in range(len(imagenPersonaje.SKIN_COLORS)):
            if(imagenPersonaje.SKIN_COLORS[index]["colorHead"] == colorNuevo):
                return imagenPersonaje.SKIN_COLORS[index]
            
            
    def cambiarColorParte(self,imagenNuevaId:int,pathImage,colorNuevo:tuple):
        # El parametro pathImage debe contener una de las variables de clase
        objectImage= Image.open(pathImage)
        if(pathImage == cons.RUTA_IMAGEN_CUERPO):
            setOfColors=self.determineSetOfColors(colorNuevo)
            print(setOfColors["colorNeck"])
        modifiedImage= objectImage.copy()
        pixels=modifiedImage.load()
        eyeWidthImage, eyeHeightImage= modifiedImage.size
        actualColor=self.determineImage(pathImage)

        for x in range(eyeWidthImage):
            for y in range(eyeHeightImage):
                pixel=modifiedImage.getpixel((x,y))
                # print(pixel)
                # print(pixel ==(0,0,0,255))
                if(type(actualColor) == tuple):
                    if(pixel ==(0,0,0,255)):
                        modifiedImage.putpixel((x,y),colorNuevo)
                if(type(actualColor)==dict):
                    if(pixel == actualColor['cabeza']):
                        modifiedImage.putpixel((x,y),setOfColors["colorHead"])
                    elif(pixel == actualColor['cuello']):
                        
                        modifiedImage.putpixel((x,y),setOfColors["colorNeck"])

                    elif(pixel == actualColor['manos']):
                        modifiedImage.putpixel((x,y),setOfColors["colorHand"])
                    


        modifiedTk= ImageTk.PhotoImage(modifiedImage)

        # Aquí se hace el cambio, es decir, la imagen antigua es cambiada por la nueva
        self.canvas.itemconfig(imagenNuevaId, image=modifiedTk)
  
        if(pathImage == cons.RUTA_IMAGEN_OJOS):
            # print("hola")
            self.__refOjo=modifiedTk
        elif(pathImage == cons.RUTA_IMAGEN_PELO):
            self.__refPelo =modifiedTk
        elif(pathImage == cons.RUTA_IMAGEN_CUERPO):
            self.__refCuerpo=modifiedTk
    def show(self):
        self.canvas.pack()
    
    

# #Creación de la ventana
# root=Tk()

    

# personaje1= imagenPersonaje(root)
# personaje1.canvas.pack()

# colorNuevo= (255,0,255,255)


# # personaje1.cambiarColorParte(personaje1.getOjosId(),imagenPersonaje.RUTA_IMAGEN_OJOS, colorNuevo)

# # colorNuevo= (255,0,0,255)
# # personaje1.cambiarColorParte(personaje1.getPeloId(),imagenPersonaje.RUTA_IMAGEN_PELO, colorNuevo)
# # colorNuevo= (0,255,0,255)

# # personaje1.cambiarColorParte(personaje1.getOjosId(),imagenPersonaje.RUTA_IMAGEN_OJOS, colorNuevo)

# # colorNuevo= (223,113,38,255)

# # personaje1.cambiarColorParte(personaje1.getCuerpoId(),imagenPersonaje.RUTA_IMAGEN_CUERPO, colorNuevo)


# # button= Button(root, text="Eyes color", command=lambda:buttonEventHandler(personaje1))
# # button.pack()
# # button2=Button(root,text="Hair color", command=lambda:buttonEventHandler2(personaje1))
# # button2.pack()

# # canvas = Canvas(root,width=300,height=300)
# # canvas.pack()

# # #Hair image
# # eyeImage=Image.open('ojos.png')
# # eyeTk= ImageTk.PhotoImage(eyeImage)

# print(255,255,0,255)

# # #Hair image 2
# # hairImage=Image.open('pelo2-removebg-preview.png')
# # hairTk= ImageTk.PhotoImage(hairImage)


# # #Creación de imagenes en el canvas
# # eyeCanvas=canvas.create_image(150,150,image=eyeTk)


# # modifiedEyeImage=eyeImage.copy()
# # pixels=modifiedEyeImage.load()

# # print(pixels)
# # eyeWidthImage, eyeHeightImage= modifiedEyeImage.size
# # for x in range(eyeWidthImage):
# #     for y in range(eyeHeightImage):
# #         pixel=modifiedEyeImage.getpixel((x,y))
# #         print(pixel)
# #         if(pixel ==(0,0,0,255)):
# #             modifiedEyeImage.putpixel((x,y),(255,255,0,255))
            

# # modifiedEyeTk= ImageTk.PhotoImage(modifiedEyeImage)
# # print(eyeCanvas,modifiedEyeTk)
# # print(canvas.find_all())
# # canvas.itemconfig(eyeCanvas, image=modifiedEyeTk)

# # valor= cambiarColorParte(eyeImage,canvas=canvas)














# # print(canvas.find_all()[0])
# # input()
# # canvas.itemconfig(eyeCanvas, image=hairTk)

# # print(canvas.find_all()[0])





# #Mostrar ventana
# root.mainloop()