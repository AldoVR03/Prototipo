import tkinter as tk
import tkinter.ttk as ttk
import presentacion.constants as cons
import presentacion.personalizacion.frameComponent as frameComp
import presentacion.personalizacion.ImagenPersonajeComponent as personaje

class CustomView():
    def __init__(self,root) -> None:
        self.root=root
        # Main canvas
        # self.backgroundImage=tk.PhotoImage(file="fondo_login.gif")
        # self.bgWidth = self.backgroundImage.width()
        # self.bgHeight = self.backgroundImage.height()
        # self.mainCanvas=tk.Canvas(self.root, width=self.bgWidth, height=self.bgHeight,bd=0,borderwidth=0,highlightthickness=0)
        # # Marco canvas
        # self.marcoImage=tk.PhotoImage(file="marco-354x220_200%.png")
        # self.ancho_marco = self.marcoImage.width()
        # self.alto_marco = self.marcoImage.height()
        # self.x = (self.bgWidth - self.ancho_marco) // 2
        # self.y = (self.bgHeight - self.alto_marco) // 2
        self.container=tk.Frame(root)
        # Frames
        self.mainFrame=tk.Frame(self.container,width=500,height=300,bd=0, bg="brown")
        self.leftFrame=tk.Frame(self.mainFrame,width=320,height=360,bd=0, bg="#8f563b")
        self.rightFrame=tk.Frame(self.mainFrame,width=320,height=360,bg="#8f563b",bd=0)
        
        # Content Frame
        self.leftContentFrame=tk.Frame(self.leftFrame, bg="#8f563b")
        self.rightContentFrame=tk.Frame(self.rightFrame, bg="#8f563b")

        # Right Content

        self.customLabel=tk.Label(self.rightContentFrame,text="Personaliza a tu personaje", font=cons.FONT_FAMILY2, fg="#df7126", bg="#8f563b")
        ## Nombre de personaje
        self.nombrePersonajeLabel=tk.Label(self.rightContentFrame,text="Nombre del personaje", bg="#8f563b", font=cons.FONT_FAMILY1,fg=cons.COLOR_AMARILLO)
        self.nombrePersonajeEntry=tk.Entry(self.rightContentFrame, font=cons.FONT_FAMILY1)

        ## Raza
        self.razaPersonajeLabel=tk.Label(self.rightContentFrame,text="Raza",fg=cons.COLOR_AMARILLO, bg="#8f563b", font=cons.FONT_FAMILY1)
        self.razaPersonajeCombobox=ttk.Combobox(self.rightContentFrame, values=cons.RAZAS, font=cons.FONT_FAMILY1)
        self.razaPersonajeCombobox.current(1)
        ## Clase
        self.clasePersonajeLabel=tk.Label(self.rightContentFrame,text="Clase", bg="#8f563b", font=cons.FONT_FAMILY1,fg=cons.COLOR_AMARILLO)
        self.clasePersonajeCombobox=ttk.Combobox(self.rightContentFrame, values=cons.CLASES, font=cons.FONT_FAMILY1)
        self.clasePersonajeCombobox.current(1)
        # Button frame and content
        self.btnFrame=tk.Frame(self.rightContentFrame, bg="#8f563b")
        self.saveBtn=tk.Button(self.btnFrame,text="Guardar", font=cons.FONT_FAMILY1)
        self.customBackBtn=tk.Button(self.btnFrame, text="Volver", font=cons.FONT_FAMILY1)
        # Skin color frame
        # self.skinColorFrame=tk.Frame(self.rightContentFrame)
        # RadioButtons
        self.radioComponent=frameComp.FrameComponent(self.rightContentFrame)
        self.radioComponent.skinColorLabel.config(font=cons.FONT_FAMILY1,fg=cons.COLOR_AMARILLO)

        # Left Content
        # Instancia personaje
        self.personajeComponent=personaje.imagenPersonaje(self.leftContentFrame,False)
        self.personajeComponent.setXCoords(65)
        self.personajeComponent.construirPersonaje()

        
        self.changeHairColorBtn=tk.Button(self.leftContentFrame,text="Color de pelo", font=cons.FONT_FAMILY0)
        self.changeEyesColorBtn=tk.Button(self.leftContentFrame,text="Color de ojos", font=cons.FONT_FAMILY0)
        # self.changeSkinColorBtn=tk.Button(self.leftContentFrame,text="Color de piel", font=cons.FONT_FAMILY0)


        
        
        # self.rightTopFrame=tk.Frame(self.rightFrame,width=320,height=350,bg="green")
        # self.rightBottomFrame=tk.Frame(self.rightFrame,width=320,height=105,bg="blue")

        
        # self.label=tk.Label(self.leftFrame,text="hola")
    def resetPersonajeComponent(self):
        self.personajeComponent=personaje.imagenPersonaje(self.leftContentFrame)
    def show(self):
        self.reset()
        # Background
        # self.mainCanvas.pack()

        # self.mainCanvas.create_image(0, 0, anchor="nw", image=self.backgroundImage)
        # self.mainCanvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)
        
        # Frames
        self.container.place(relx=0.5, rely=0.5, anchor="center")
        # self.mainFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.mainFrame.pack()
        self.leftFrame.grid(row=0,column=0)
        self.rightFrame.grid(row=0,column=1)
        self.leftContentFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.rightContentFrame.place(relx=0.5, rely=0.5, anchor="center")

        # Widgets
        self.customLabel.pack(**cons.BUTTON_LAYOUT)
        self.nombrePersonajeLabel.pack(**cons.BUTTON_LAYOUT)
   
        self.nombrePersonajeEntry.pack(**cons.BUTTON_LAYOUT)

        self.razaPersonajeLabel.pack()
        self.razaPersonajeCombobox.pack(**cons.BUTTON_LAYOUT)

        self.clasePersonajeLabel.pack()
        self.clasePersonajeCombobox.pack(**cons.BUTTON_LAYOUT)

        

        
        self.radioComponent.show()
        self.personajeComponent.canvas.pack()

        self.changeEyesColorBtn.pack(side="left", **cons.BUTTON_LAYOUT,pady=5)
        self.changeHairColorBtn.pack(side="left", **cons.BUTTON_LAYOUT,padx=2,pady=5)
        # self.changeSkinColorBtn.pack(side="left", **cons.BUTTON_LAYOUT,pady=5)

        self.btnFrame.pack(**cons.BUTTON_LAYOUT,pady=10)
        self.saveBtn.pack(side="top", **cons.BUTTON_LAYOUT,pady=2)
        self.customBackBtn.pack(side="bottom",**cons.BUTTON_LAYOUT,pady=2)

    def hide(self):
        self.mainFrame.pack_forget()

        # self.rightTopFrame.grid(row=0,column=0)
        # self.rightBottomFrame.grid(row=1,column=0)
        # self.marcoFrame.place(relx=0.5, rely=0, anchor="center")
        # self.marcoFrame.grid(column=0,row=0)
#         # self.label.pack()
    def reset(self):
        # Reset
        self.nombrePersonajeEntry.delete(0,tk.END)
        
# root=tk.Tk()
# p1=CustomView(root)
# p1.show()
# root.mainloop()