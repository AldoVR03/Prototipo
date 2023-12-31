import tkinter as tk
import presentacion.menu.levelBar as level
import presentacion.constants as cons

class MenuView():
    def __init__(self,root) -> None:
        self.root=root
        # Main canvas
        self.backgroundImage=tk.PhotoImage(file="images/fondo_login.gif")
        self.bgWidth = self.backgroundImage.width()
        self.bgHeight = self.backgroundImage.height()
        self.canvas=tk.Canvas(self.root, width=self.bgWidth, height=self.bgHeight,bd=0,borderwidth=0,highlightthickness=0, bg="black")
  

        self.marcoImage=tk.PhotoImage(file="images/marcoMenu.png")
        self.btnMenuImage=tk.PhotoImage(file="images/btnMenu.png")
        self.marcoTiendaImage=tk.PhotoImage(file="images/marcoTienda.png")
        self.tiendaImage=tk.PhotoImage(file="images/tiendaImagen.png")
        self.marcoUsuario=tk.PhotoImage(file="images/marcoDatosUsuario.png")
        self.tiendaImageOver=tk.PhotoImage(file="images/tiendaImagenOver.png")
        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.x = (self.bgWidth - self.ancho_marco) // 2
        self.y = (self.bgHeight - self.alto_marco) // 2

        self.canvas.create_image(-150, 0, anchor="nw", image=self.backgroundImage)
        self.canvas.create_image(self.x+250, self.y+30, anchor="nw", image=self.marcoImage)
        self.canvas.create_image(5, self.y+340, anchor="nw", image=self.marcoTiendaImage)
        self.tiendaImageReference=self.canvas.create_image(20, self.y+360, anchor="nw", image=self.tiendaImage,tags="image_tag")
        self.canvas.create_image(0, 20, anchor="nw", image=self.marcoUsuario)
        
        # self.mainCanvas.create_image(self.x+250, self.y, anchor="nw", image=self.btnMenuImage)

        # Frames
        self.mainFrame=tk.Frame(self.canvas, width=280,height=370,bg="#8f563b" )
        self.barFrame=tk.Frame(self.canvas,bg="#8f563b", width=440,height=20)
        self.btnFrame=tk.Frame(self.mainFrame,bg="#8f563b")
        # #8f563b
        # Bar frames
        self.rightBarFrame=tk.Frame(self.barFrame, bg="#8f563b")
        self.leftBarFrame=tk.Frame(self.barFrame, bg="#8f563b")

        
        # Menu section
        self.jugarBtn=tk.Button(self.btnFrame,font=cons.FONT_FAMILY2,text="JUGAR",width=20)
        self.libroBtn=tk.Button(self.btnFrame,font=cons.FONT_FAMILY2,text="LIBRO")
        self.clanBtn=tk.Button(self.mainFrame,font=cons.FONT_FAMILY2,text="CLAN")
        # self.misionBtn=tk.Button(self.mainFrame, font=cons.FONT_FAMILY2,text="MISIONES")
        self.salirBtn=tk.Button(self.mainFrame,font=cons.FONT_FAMILY2,text="SALIR")
        
        
        # Bar section
        self.characterLevelBar=level.characterLevelComponent(self.rightBarFrame )
        self.playerLevelBar=level.characterLevelComponent(self.leftBarFrame)
        
        self.playerLabel=tk.Label(self.leftBarFrame,text="Cuenta", bg="#8f563b", font=cons.FONT_FAMILY1)
        self.characterLabel=tk.Label(self.rightBarFrame,text="Personaje", bg="#8f563b", font=cons.FONT_FAMILY1)

        self.playerQuantityLabel=tk.Label(self.leftBarFrame, text=0, bg="#8f563b", font=cons.FONT_FAMILY1)
        self.characterQuantityLabel=tk.Label(self.rightBarFrame, text=0, bg="#8f563b", font=cons.FONT_FAMILY1)
        # Store section
        # self.btnIniciar=tk.Label(self.canvas,text="hgola")




        # Eventos
        self.canvas.tag_bind(self.tiendaImageReference, "<Enter>", self.change_image)  # Cuando el mouse entra en la imagen
        self.canvas.tag_bind(self.tiendaImageReference, "<Leave>", self.restore_image)
        # self.canvas.tag_bind(self.tiendaImageReference, "<Button-1>", self.changeView)
        

        # Vars
        self.isSelected=None

    def show(self):
        self.canvas.pack()
        self.mainFrame.place(relx=0.79, rely=0.55, anchor="center")
        self.btnFrame.pack(**cons.BUTTON_LAYOUT)
        self.barFrame.place(relx=0.28, rely=0.1, anchor="center")
        # self.btnIniciar.place(x=self.x+250+30, y=self.y)

        # Menu section
        self.jugarBtn.pack(**cons.BUTTON_LAYOUT, pady=10)
        self.libroBtn.pack(**cons.BUTTON_LAYOUT, pady=10)
        self.clanBtn.pack(**cons.BUTTON_LAYOUT, pady=10)
        # self.misionBtn.pack(**cons.BUTTON_LAYOUT, pady=10)
        self.salirBtn.pack(**cons.BUTTON_LAYOUT, pady=10)

        # Bar section
        self.rightBarFrame.pack(side="left", padx=5, anchor="e")
        self.leftBarFrame.pack(side="left", anchor="e")

        self.playerLabel.pack(side="top")
        self.characterLabel.pack(side="top")
        # self.playerQuantityLabel.pack(side="left")
        # self.characterQuantityLabel.pack(side="left")
        
        self.characterLevelBar.show()
        self.playerLevelBar.show()
        # Store section


        
        # self.mainFrame.place(relx=0.5, rely=0.5, anchor="center")
    def change_image(self,event):
        print(self.isSelected)
        if(self.isSelected):
            return
        canvas=event.widget
        canvas.itemconfigure(canvas.find_withtag("image_tag")[0], image=self.tiendaImageOver)  # Cambiar a la segunda imagen
        canvas.configure(cursor="hand2")

    def restore_image(self,event):
        if self.isSelected:
            return
        canvas=event.widget
        canvas.itemconfigure(canvas.find_withtag("image_tag")[0], image=self.tiendaImage)
        self.canvas.configure(cursor="")

    def changeView(self, event):
        canvas=event.widget
        canvas.itemconfigure(canvas.find_withtag("image_tag")[0], image=self.tiendaImageOver) 
        self.isSelected=(canvas,canvas.find_withtag("image_tag")[0])
        print("Hey you!!")
# root=tk.Tk()
# oMenu=MenuView(root)
# oMenu.show()
# root.mainloop()