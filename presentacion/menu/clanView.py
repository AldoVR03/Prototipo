
import tkinter as tk
import presentacion.menu.clanDescriptionView as clan
import presentacion.menu.clanSolicitudView as clanMsg
import presentacion.constants as cons
import time
x=730
y=55
class ClanView():
    def __init__(self,root):  
        self.backgroundImage=tk.PhotoImage(file="images/fondo_login.gif")
        self.bgWidth = self.backgroundImage.width()
        self.bgHeight = self.backgroundImage.height()
        self.canvas=tk.Canvas(root, width=self.bgWidth, height=self.bgHeight,bd=0,borderwidth=0,highlightthickness=0)
        
        # Marco canvas
        self.marcoImage=tk.PhotoImage(file="images/marco-398X231.png")
        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.x = (self.bgWidth - self.ancho_marco) // 2
        self.y = (self.bgHeight - self.alto_marco) // 2
        # Images
        self.clanImage=tk.PhotoImage(file="images/clanBtn.png")
        self.mailImage=tk.PhotoImage(file="images/messageBtn.png")
        self.clanImageOver=tk.PhotoImage(file="images/clanBtnOver.png")
        self.mailImageOver=tk.PhotoImage(file="images/messageBtnOver.png")


        # Frames
        self.mainFrame=tk.Frame(self.canvas,bg="black", width=200, height=100)
        self.clanFrame=tk.Frame(self.mainFrame)
        


    

        self.clanImageOverReference=self.canvas.create_image(x, y, anchor="nw", image=self.clanImageOver)
        self.mailImageOverReference=self.canvas.create_image(x, y, anchor="nw", image=self.mailImageOver)

        self.canvas.create_image(0, 0, anchor="nw", image=self.backgroundImage)
        self.canvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)
        self.mailImageReference=self.canvas.create_image(x, y+60, anchor="nw", image=self.mailImage)
        self.clanImageReference=self.canvas.create_image(x, y, anchor="nw", image=self.clanImage)
        
        
        
        

        self.canvas.tag_bind(self.clanImageReference, "<Enter>", lambda event:self.change_image(event, self.clanImageReference, self.clanImageOver))                                                                                                 
        self.canvas.tag_bind(self.clanImageReference, "<Leave>", lambda event:self.restore_image(event,self.clanImageReference,self.clanImage))
        self.canvas.tag_bind(self.clanImageReference, "<Button-1>", lambda event:self.selectWin(event, self.clanImageReference, self.clanImageOver, self.clanImage))
        
        self.canvas.tag_bind(self.mailImageReference, "<Enter>",lambda event: self.change_image(event, self.mailImageReference, self.mailImageOver))  
        self.canvas.tag_bind(self.mailImageReference, "<Leave>", lambda event:self.restore_image(event, self.mailImageReference, self.mailImage))
        self.canvas.tag_bind(self.mailImageReference, "<Button-1>", lambda event:self.selectWin(event, self.mailImageReference, self.mailImageOver, self.mailImage))

        self.isSelected=[self.canvas,self.clanImageReference,self.clanImage]
        self.viewDict={"Clan":clan.ClanDescriptionView(self.clanFrame),
                       "Mailbox":clanMsg.SolicitudView(self.clanFrame)}
        self.currentViews=None


    def show(self):
        self.canvas.pack()
        
        
        
        

        self.mainFrame.place(relx=0.451, rely=0.5, anchor="center")
        self.clanFrame.pack()
        
        
        

      

        self.viewDict["Clan"].show()
        self.currentViews= [self.viewDict["Clan"].container]
        
        self.selectWin(check=True)
        
        
        
    
    def hide(self):
        pass
    def startComp(self):
        self.clanListComp.start()

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
            self.canvas.itemconfigure(self.clanImageReference,image=self.clanImageOver)
            self.isSelected= (self.canvas, self.clanImageReference,self.clanImage)
            return 
        canvas=event.widget
        canvas.itemconfigure(reference, image=focusImage) 
        self.isSelected=(canvas,reference, defaultImage)
        # Ejecutar metodo para cambiar de vista
        self.changeView(reference)
        print("Hey you!!")
        
    def changeView(self, reference):
        tempDict = {"Clan":self.clanImageReference,
                    "Mailbox":self.mailImageReference,
                    }
        # print(self.currentViews)
        self.currentViews[0].pack_forget()
        
        print(reference)
        for elem in tempDict:
            if tempDict[elem] == reference:
                print(tempDict[elem], reference)   
                self.currentViews[0]=self.viewDict[elem].container
                # print(self.currentViews)
                time.sleep(0.2)
                self.viewDict[elem].show()

# root=tk.Tk()
# oComp=ClanView(root)
# oComp.show()
# root.mainloop()
		
    
    