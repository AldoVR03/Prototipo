
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
        self.topFrame=tk.Frame(self.mainFrame, bg="#8f563b",width=650, height=260)
        self.bottomFrame=tk.Frame(self.mainFrame, bg="#8f563b", width=650, height=20)

        # Top content
        self.firstCharacterFrame=tk.Frame(self.topFrame, bg="pink", width=160,height=260)
        self.secCharacterFrame=tk.Frame(self.topFrame, bg="red", width=160,height=260)
        self.thirdCharacterFrame=tk.Frame(self.topFrame, bg="blue", width=160,height=260)
        self.fourthCharacterFrame=tk.Frame(self.topFrame, bg="green", width=160,height=260)

        self.customLabel=tk.Label(self.topFrame,text="Elige a tu personaje", font=cons.FONT_FAMILY2, bg="#8f563b", fg=cons.COLOR_AMARILLO)

        
        self.characterSelectionImage=tk.PhotoImage(file="images/selectionFrameS.png")
        self.characterSelectionImageOver=tk.PhotoImage(file="images/selectionFrameSOVER.png")
        
        self.characterList=None
        # First selection 
        personaje.COORDS_X=90
        self.firstCharacterCanvas=tk.Canvas(self.firstCharacterFrame,width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)

        self.firstCharacterImage=personaje.imagenPersonaje(self.firstCharacterFrame,False,self.firstCharacterCanvas)

        # self.firstCharacterImage.canvas.config(width=110,height=100)
        self.firstCharacterImage.setCanvas=self.firstCharacterCanvas
        self.firstCharacterImage.construirPersonaje()
        self.firstSelectionCanvasReference=self.firstCharacterCanvas.create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")

        self.firstCharacterCanvas.tag_bind(self.firstSelectionCanvasReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        self.firstCharacterCanvas.tag_bind(self.firstSelectionCanvasReference, "<Leave>", self.restore_image)
        self.firstCharacterCanvas.tag_bind(self.firstSelectionCanvasReference, "<Button-1>", self.selectCharacter)
        
        # Second selection
        self.secCharacterCanvas=tk.Canvas(self.secCharacterFrame,width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)
        self.secSelectionCanvasReference=self.secCharacterCanvas.create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")
        self.secCharacterCanvas.tag_bind(self.secSelectionCanvasReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        self.secCharacterCanvas.tag_bind(self.secSelectionCanvasReference, "<Leave>", self.restore_image)
        self.secCharacterCanvas.tag_bind(self.secSelectionCanvasReference, "<Button-1>", self.selectCharacter)
        
        # Third Selection
        self.thirdCharacterCanvas=tk.Canvas(self.thirdCharacterFrame,width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)
        self.thirdSelectionCanvasReference=self.thirdCharacterCanvas.create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")

        self.thirdCharacterCanvas.tag_bind(self.thirdSelectionCanvasReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        self.thirdCharacterCanvas.tag_bind(self.thirdSelectionCanvasReference, "<Leave>", self.restore_image)
        self.thirdCharacterCanvas.tag_bind(self.thirdSelectionCanvasReference, "<Button-1>", self.selectCharacter)
        # Fourth selection
        self.fourthCharacterCanvas=tk.Canvas(self.fourthCharacterFrame,width=self.characterSelectionImage.width(),bg="#8f563b", height=self.characterSelectionImage.height(), bd=0, borderwidth=0,highlightthickness=0)
        self.fourthSelectionCanvasReference=self.fourthCharacterCanvas.create_image(0,0,anchor="nw",image=self.characterSelectionImage,tags="image_tag")

        self.fourthCharacterCanvas.tag_bind(self.fourthSelectionCanvasReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        self.fourthCharacterCanvas.tag_bind(self.fourthSelectionCanvasReference, "<Leave>", self.restore_image)
        self.fourthCharacterCanvas.tag_bind(self.fourthSelectionCanvasReference, "<Button-1>", self.selectCharacter)


        # Bottom content
        self.contBtn=tk.Button(self.bottomFrame, text="Continuar", font=cons.FONT_FAMILY1, state="disabled")
        self.createCharacterBtn=tk.Button(self.bottomFrame, text="Crear personaje",font= cons.FONT_FAMILY1,state="disabled")
        self.backSelectionBtn=tk.Button(self.bottomFrame, text="Volver", font=cons.FONT_FAMILY1)


        # Variables
        self.isSelected=None

    def show(self):
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.backgroundImage)
        self.canvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)

        # Frames
        self.mainFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.topFrame.pack()
        self.bottomFrame.pack(pady=5)

        # Top content
        self.customLabel.grid(row=0,column=1, columnspan=2)
        self.firstCharacterFrame.grid(row=1,column=0, padx=5)
        self.secCharacterFrame.grid(row=1,column=1, padx=5, pady=5)
        self.thirdCharacterFrame.grid(row=1,column=2, padx=5)
        self.fourthCharacterFrame.grid(row=1,column=3, padx=5)
        
        # self.firstCharacterImage.canvas.pack()

        self.firstCharacterCanvas.pack()
        self.secCharacterCanvas.pack()
        self.thirdCharacterCanvas.pack()
        self.fourthCharacterCanvas.pack()

        # Bottom content
        self.contBtn.pack(side="left", **cons.BUTTON_LAYOUT,padx=10)
        self.createCharacterBtn.pack(side="left", **cons.BUTTON_LAYOUT,padx=10)
        self.backSelectionBtn.pack(side="left", **cons.BUTTON_LAYOUT,padx=10)
        

        

        
        

    def change_image(self,event):
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
    def setCharacters(self,characterList):
        self.characterList=characterList
        


if __name__=="__main__":
    root = tk.Tk()
    s1=SelectionView(root)
    s1.show()
    root.mainloop()