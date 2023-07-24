
import tkinter as tk
import presentacion.personalizacion.ImagenPersonajeComponent as personaje
import presentacion.constants as cons
class SelectionView():
    def __init__(self,root) -> None:
        self.root=root
        # Main canvas
        self.backgroundImage=tk.PhotoImage(file="images/fondo_login.gif")
        self.bgWidth = self.backgroundImage.width()
        self.bgHeight = self.backgroundImage.height()
        self.canvas=tk.Canvas(self.root, width=self.bgWidth, height=self.bgHeight,bd=0,borderwidth=0,highlightthickness=0, bg="black")
        # Marco canvas
        self.marcoImage=tk.PhotoImage(file="images/marco-398X231.png")
        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.x = (self.bgWidth - self.ancho_marco) // 2
        self.y = (self.bgHeight - self.alto_marco) // 2

        # Frames
        self.mainFrame=tk.Frame(self.canvas,bg="#8f563b", width=650, height=370)
        self.upperTopFrame=tk.Frame(self.mainFrame)
        self.topFrame=tk.Frame(self.mainFrame, bg="#8f563b",width=650, height=260)
        self.bottomFrame=tk.Frame(self.mainFrame, bg="#8f563b", width=650, height=20)

        # Top content
        self.firstCharacterFrame=tk.Frame(self.topFrame, bg="pink")
        self.secCharacterFrame=tk.Frame(self.topFrame, bg="red")
        self.thirdCharacterFrame=tk.Frame(self.topFrame, bg="blue")
        self.fourthCharacterFrame=tk.Frame(self.topFrame, bg="green")

        self.customLabel=tk.Label(self.upperTopFrame,text="Elige a tu personaje", font=cons.FONT_FAMILY2, bg="#8f563b", fg=cons.COLOR_AMARILLO)

        
        self.characterSelectionImage=tk.PhotoImage(file="images/selectionFrameS.png")
        self.characterSelectionImageOver=tk.PhotoImage(file="images/selectionFrameSOVER.png")
        
        self.characterList=None
        self.characterImageList={}
        self.positionList=["FIRST","SECOND","THIRD","FOURTH"]
        self.characterFrameDict={}
        self.canvasDict={}
        for i in range(4):
            self.characterFrameDict[self.positionList[i]]=tk.Frame(self.topFrame)
            self.canvasDict[self.positionList[i]]=tk.Canvas(self.characterFrameDict[self.positionList[i]])
            self.canvasDict[self.positionList[i]].config(width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)
            self.characterImageList[self.positionList[i]]=personaje.imagenPersonaje(self.characterFrameDict[self.positionList[i]],False,self.canvasDict[self.positionList[i]])
        print("asds",self.characterFrameDict,self.canvasDict,self.characterImageList)
        # First selection 
        personaje.COORDS_X=90
        self.firstCharacterCanvas=tk.Canvas(self.firstCharacterFrame,width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)
        self.firstCharacterImage=personaje.imagenPersonaje(self.firstCharacterFrame,False,self.firstCharacterCanvas)
        # self.firstCharacterImage.canvas.config(width=110,height=100)
        # Second selection
        self.secCharacterCanvas=tk.Canvas(self.secCharacterFrame,width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)
        self.secCharacterImage=personaje.imagenPersonaje(self.secCharacterFrame,False,self.secCharacterCanvas)
        # Third Selection
        self.thirdCharacterCanvas=tk.Canvas(self.thirdCharacterFrame,width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)
        self.thirdCharacterImage=personaje.imagenPersonaje(self.thirdCharacterFrame,False,self.thirdCharacterCanvas)
        # Fourth selection
        self.fourthCharacterCanvas=tk.Canvas(self.fourthCharacterFrame,width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)
        self.fourthCharacterImage=personaje.imagenPersonaje(self.fourthCharacterFrame,False,self.fourthCharacterCanvas)
        
        
    
        # Bottom content
        self.contBtn=tk.Button(self.bottomFrame, text="Continuar", font=cons.FONT_FAMILY1, state="disabled")
        self.createCharacterBtn=tk.Button(self.bottomFrame, text="Crear personaje",font= cons.FONT_FAMILY1,state="disabled")
        self.backSelectionBtn=tk.Button(self.bottomFrame, text="Volver", font=cons.FONT_FAMILY1)


        # Variables
        self.isSelected=None
        self.characterReferenceDict={}
        self.relateCanvasPersonaje={}
        self.selectedCharacter=None
        # for positionStr in self.positionList:
        #     # self.characterImageList[positionStr].construirPersonaje()
        #     self.characterReferenceDict[positionStr]=self.canvasDict[positionStr].create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")
        
        # self.firstCharacterImage.setCanvas=self.firstCharacterCanvas
        # self.firstCharacterImage.construirPersonaje()
        # self.firstSelectionCanvasReference=self.firstCharacterCanvas.create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")
        
        # # self.secCharacterImage.setCanvas=self.secCharacterCanvas
        # self.secCharacterImage.construirPersonaje()
        # self.secSelectionCanvasReference=self.secCharacterCanvas.create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")
        
        # # self.thirdCharacterImage.setCanvas=self.thirdCharacterCanvas
        # self.thirdCharacterImage.construirPersonaje()
        # self.thirdSelectionCanvasReference=self.thirdCharacterCanvas.create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")
        
        # self.fourthCharacterImage.construirPersonaje()
        # self.fourthSelectionCanvasReference=self.fourthCharacterCanvas.create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")
        # self.fourthCharacterImage.setCanvas=self.fourthCharacterCanvas
        
        
        

        # self.firstCharacterCanvas.tag_bind(self.firstSelectionCanvasReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        # self.firstCharacterCanvas.tag_bind(self.firstSelectionCanvasReference, "<Leave>", self.restore_image)
        # self.firstCharacterCanvas.tag_bind(self.firstSelectionCanvasReference, "<Button-1>", self.selectCharacter)

        # self.secCharacterCanvas.tag_bind(self.secSelectionCanvasReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        # self.secCharacterCanvas.tag_bind(self.secSelectionCanvasReference, "<Leave>", self.restore_image)
        # self.secCharacterCanvas.tag_bind(self.secSelectionCanvasReference, "<Button-1>", self.selectCharacter)

        
        
        # self.thirdCharacterCanvas.tag_bind(self.thirdSelectionCanvasReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        # self.thirdCharacterCanvas.tag_bind(self.thirdSelectionCanvasReference, "<Leave>", self.restore_image)
        # self.thirdCharacterCanvas.tag_bind(self.thirdSelectionCanvasReference, "<Button-1>", self.selectCharacter)

        # self.fourthCharacterCanvas.tag_bind(self.fourthSelectionCanvasReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        # self.fourthCharacterCanvas.tag_bind(self.fourthSelectionCanvasReference, "<Leave>", self.restore_image)
        # self.fourthCharacterCanvas.tag_bind(self.fourthSelectionCanvasReference, "<Button-1>", self.selectCharacter)

    def show(self):
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.backgroundImage)
        self.canvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)

        # Frames
        self.mainFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.upperTopFrame.pack()
        self.topFrame.pack()
        self.bottomFrame.pack(pady=5)

        # Top content
        self.customLabel.grid(row=0,column=1, columnspan=2)
        self.characterFrameDict["FIRST"].grid(row=1,column=0, padx=5)
        self.characterFrameDict["SECOND"].grid(row=1,column=1, padx=5, pady=5)
        self.characterFrameDict["THIRD"].grid(row=1,column=2, padx=5)
        self.characterFrameDict["FOURTH"].grid(row=1,column=3, padx=5)
        
        # self.firstCharacterImage.canvas.pack()
        for positioStr in self.positionList:
            self.canvasDict[positioStr].pack()
        # self.firstCharacterCanvas.pack()
        # self.secCharacterCanvas.pack()
        # self.thirdCharacterCanvas.pack()
        # self.fourthCharacterCanvas.pack()

        # Bottom content
        self.contBtn.pack(side="left", **cons.BUTTON_LAYOUT,padx=10)
        self.createCharacterBtn.pack(side="left", **cons.BUTTON_LAYOUT,padx=10)
        self.backSelectionBtn.pack(side="left", **cons.BUTTON_LAYOUT,padx=10)
    def showPlayerCharacters(self,numChars,colorsList):
        for i in range(numChars):
            self.characterImageList[self.positionList[i]].construirPersonaje()
            self.characterImageList[self.positionList[i]].cambiarColorParte(self.characterImageList[self.positionList[i]].getOjosId(), personaje.imagenPersonaje.RUTA_IMAGEN_OJOS,colorsList[i]["EYECOLOR"])
            self.characterImageList[self.positionList[i]].cambiarColorParte(self.characterImageList[self.positionList[i]].getCuerpoId(), personaje.imagenPersonaje.RUTA_IMAGEN_CUERPO,colorsList[i]["SKINCOLOR"])
            self.characterImageList[self.positionList[i]].cambiarColorParte(self.characterImageList[self.positionList[i]].getPeloId(), personaje.imagenPersonaje.RUTA_IMAGEN_PELO,colorsList[i]["HAIRCOLOR"])
            
            # Cambiar colores aqui
            self.characterReferenceDict[self.positionList[i]]=self.canvasDict[self.positionList[i]].create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")
        
            self.canvasDict[self.positionList[i]].tag_bind(self.characterReferenceDict[self.positionList[i]], "<Enter>", lambda event:self.change_image(event,i))
            self.canvasDict[self.positionList[i]].tag_bind(self.characterReferenceDict[self.positionList[i]], "<Leave>", self.restore_image)
            self.canvasDict[self.positionList[i]].tag_bind(self.characterReferenceDict[self.positionList[i]], "<Button-1>", self.selectCharacter)
            
            self.relateCanvasPersonaje[self.canvasDict[self.positionList[i]]]=self.characterList[i]

        for i in range(4-numChars):
            self.characterFrameDict[self.positionList[3-i]].grid_forget()
        print(self.relateCanvasPersonaje)
        

        
        

    def change_image(self,event, value):
        print(value)
        canvas=event.widget
        print(self.isSelected, "asdasd")
        if(self.isSelected):
            canvas.configure(cursor="hand2")
            return None
        
        canvas.itemconfigure(canvas.find_withtag("image_tag")[0], image=self.characterSelectionImageOver)  # Cambiar a la segunda imagen
        canvas.configure(cursor="hand2")
  

    def restore_image(self,event):
        canvas=event.widget
        if self.isSelected:
            canvas.configure(cursor="")
            return None
        
        canvas.itemconfigure(canvas.find_withtag("image_tag")[0], image=self.characterSelectionImage)
        canvas.configure(cursor="")
        

    def selectCharacter(self, event):
        if(self.isSelected):
            canvas=self.isSelected[0]
            idImage=self.isSelected[1]
            canvas.itemconfigure(idImage,image=self.characterSelectionImage)
        canvas=event.widget
        canvas.itemconfigure(canvas.find_withtag("image_tag")[0], image=self.characterSelectionImageOver) 
        self.isSelected=(canvas,canvas.find_withtag("image_tag")[0])
        print("Hey you!!")
        self.selectCharacter=self.relateCanvasPersonaje[canvas]
        self.contBtn.config(state="normal")
    def setCharacters(self,characterList):
        self.characterList=characterList
        
        


if __name__=="__main__":
    root = tk.Tk()
    s1=SelectionView(root)
    s1.show()
  
    s1.showPlayerCharacters()
    root.mainloop()