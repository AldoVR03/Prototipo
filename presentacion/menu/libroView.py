
import tkinter as tk
from presentacion.menu.bookComponents import EnemigoComponent, UserComponent, HabilidadComponent,MisionComponent
import time
class LibroView():
    def __init__(self, root) -> None:
        
        

        # Images
        self.backgroundImage=tk.PhotoImage(file="images/fondo_login.gif")
        self.bookImage=tk.PhotoImage(file="images/bk.png")
        self.pestagnaaEnemigoImage=tk.PhotoImage(file="images/lg1.png")
        self.pestagnaaHabildiadImage=tk.PhotoImage(file="images/lg2.png")
        self.pestagnaaMisionImage=tk.PhotoImage(file="images/lg3.png")
        self.pestagnaaUserImage=tk.PhotoImage(file="images/lg4.png")
        
        self.pestagnaaEnemigoImageFocus=tk.PhotoImage(file="images/lg1Over.png")
        self.pestagnaaHabildiadImageFocus=tk.PhotoImage(file="images/lg2Over.png")
        self.pestagnaaMisionImageFocus=tk.PhotoImage(file="images/lg3Over.png")
        self.pestagnaaUserImageFocus=tk.PhotoImage(file="images/lg4Over.png")

        self.bgWidth = self.backgroundImage.width()
        self.bgHeight = self.backgroundImage.height()
        self.canvas=tk.Canvas(root, width=self.bgWidth, height=self.bgHeight,bd=0,borderwidth=0,highlightthickness=0)
        # Marco canvas
        
        self.ancho_marco = self.bookImage.width()
        self.alto_marco = self.bookImage.height()
        self.x = (self.bgWidth - self.ancho_marco) // 2
        self.y = (self.bgHeight - self.alto_marco) // 2

        # Frames
        self.mainFrame=tk.Frame(self.canvas,bg="#cab9a1", width=270, height=350)
        self.secFrame=tk.Frame(self.canvas,bg="#cab9a1", width=270, height=350)

        # Image references
        self.canvas.create_image(0, 0, anchor="nw", image=self.backgroundImage)
        self.canvas.create_image(self.x-50, self.y, anchor="nw", image=self.bookImage)

        self.pestagnaaEnemigoImageReference=self.canvas.create_image(self.x+630, self.y+20, anchor="nw", image=self.pestagnaaEnemigoImage,tags="image_tag")
        self.pestagnaaHabildiadImageReference=self.canvas.create_image(self.x+630, self.y+100, anchor="nw", image=self.pestagnaaHabildiadImage,tags="image_tag2")
        self.pestagnaaMisionImageReference=self.canvas.create_image(self.x+630, self.y+180, anchor="nw", image=self.pestagnaaMisionImage,tags="image_tag3")
        self.pestagnaaUserImageReference=self.canvas.create_image(self.x+630, self.y+300,anchor="nw",image=self.pestagnaaUserImage, tags="image_tag4")
        # Eventos
        self.canvas.tag_bind(self.pestagnaaEnemigoImageReference, "<Enter>", lambda event:self.change_image(event, self.pestagnaaEnemigoImageReference, self.pestagnaaEnemigoImageFocus                                                                                                     ))  # Cuando el mouse entra en la imagen
        self.canvas.tag_bind(self.pestagnaaEnemigoImageReference, "<Leave>", lambda event:self.restore_image(event,self.pestagnaaEnemigoImageReference,self.pestagnaaEnemigoImage))
        self.canvas.tag_bind(self.pestagnaaEnemigoImageReference, "<Button-1>", lambda event:self.selectWin(event, self.pestagnaaEnemigoImageReference, self.pestagnaaEnemigoImageFocus, self.pestagnaaEnemigoImage))
        
        self.canvas.tag_bind(self.pestagnaaHabildiadImageReference, "<Enter>",lambda event: self.change_image(event, self.pestagnaaHabildiadImageReference, self.pestagnaaHabildiadImageFocus))  # Cuando el mouse entra en la imagen
        self.canvas.tag_bind(self.pestagnaaHabildiadImageReference, "<Leave>", lambda event:self.restore_image(event, self.pestagnaaHabildiadImageReference, self.pestagnaaHabildiadImage))
        self.canvas.tag_bind(self.pestagnaaHabildiadImageReference, "<Button-1>", lambda event:self.selectWin(event, self.pestagnaaHabildiadImageReference, self.pestagnaaHabildiadImageFocus, self.pestagnaaHabildiadImage))
        
        self.canvas.tag_bind(self.pestagnaaMisionImageReference, "<Enter>", lambda event:self.change_image(event, self.pestagnaaMisionImageReference,self.pestagnaaMisionImageFocus))  # Cuando el mouse entra en la imagen
        self.canvas.tag_bind(self.pestagnaaMisionImageReference, "<Leave>", lambda event:self.restore_image(event, self.pestagnaaMisionImageReference,self.pestagnaaMisionImage))
        self.canvas.tag_bind(self.pestagnaaMisionImageReference, "<Button-1>", lambda event:self.selectWin(event, self.pestagnaaMisionImageReference, self.pestagnaaMisionImageFocus, self.pestagnaaMisionImage))
        
        self.canvas.tag_bind(self.pestagnaaUserImageReference, "<Enter>", lambda event:self.change_image(event, self.pestagnaaUserImageReference,self.pestagnaaUserImageFocus))  # Cuando el mouse entra en la imagen
        self.canvas.tag_bind(self.pestagnaaUserImageReference, "<Leave>", lambda event:self.restore_image(event, self.pestagnaaUserImageReference,self.pestagnaaUserImage))
        self.canvas.tag_bind(self.pestagnaaUserImageReference, "<Button-1>", lambda event:self.selectWin(event, self.pestagnaaUserImageReference, self.pestagnaaUserImageFocus, self.pestagnaaUserImage))
        
        # Vars
        self.isSelected=None
        self.viewDict={"Enemigo":EnemigoComponent(self.mainFrame, self.secFrame),
                       "Mision":MisionComponent(self.mainFrame, self.secFrame),
                       "User":UserComponent(self.mainFrame, self.secFrame),
                       "Habilidad":HabilidadComponent(self.mainFrame, self.secFrame)}
        self.currentViews=None
        

    def change_image(self,event, reference, focusImage):
        canvas=event.widget
        if self.isSelected:
            canvas.configure(cursor="hand2")
            return
        
        canvas.itemconfigure(reference, image=focusImage)  # Cambiar a la segunda imagen
        canvas.configure(cursor="hand2")
        # print("Hola")
        # canvas.after(300)

    def restore_image(self,event, reference, defaultImage):
        # print(reference,defaultImage)
        canvas=event.widget
        if self.isSelected:
            canvas.configure(cursor="")
            return

        canvas.itemconfigure(reference, image=defaultImage)
        canvas.configure(cursor="")

    def selectWin(self, event=None, reference=None, focusImage=None, defaultImage=None, check=None):
        if(self.isSelected):
            canvas=self.isSelected[0]
            idImage=self.isSelected[1]
            defaultIm=self.isSelected[2]
            canvas.itemconfigure(idImage,image=defaultIm)
        if(check==True):
            self.canvas.itemconfigure(self.pestagnaaUserImageReference,image=self.pestagnaaUserImageFocus)
            self.isSelected= (self.canvas, self.pestagnaaUserImageReference,self.pestagnaaUserImage)
            return 
        canvas=event.widget
        canvas.itemconfigure(reference, image=focusImage) 
        self.isSelected=(canvas,reference, defaultImage)
        # Ejecutar metodo para cambiar de vista
        self.changeView(reference)
        # print("Hey you!!")

    
    def show(self):
        self.canvas.pack()
        
        self.mainFrame.place(relx=0.25, rely=0.46, anchor="center")
        self.secFrame.place(relx=0.63, rely=0.46, anchor="center")

        self.viewDict["User"].show()
        self.currentViews= [self.viewDict["User"].leftContent,self.viewDict["User"].rightContent]
        
        self.selectWin(check=True)

    def changeView(self, reference):
        tempDict = {"Enemigo":self.pestagnaaEnemigoImageReference,
                    "User":self.pestagnaaUserImageReference,
                    "Habilidad":self.pestagnaaHabildiadImageReference,
                    "Mision":self.pestagnaaMisionImageReference}
        # print(self.currentViews)
        self.currentViews[0].pack_forget()
        self.currentViews[1].pack_forget()
        
        for elem in tempDict:
            if tempDict[elem] == reference:
                # print(tempDict[elem], reference)   
                self.currentViews[0]=self.viewDict[elem].leftContent
                self.currentViews[1]=self.viewDict[elem].rightContent
                time.sleep(0.2)
                self.viewDict[elem].show()
                
        
        

# root= tk.Tk()
# oComp=LibroView(root)
# oComp.show()

# root.mainloop()