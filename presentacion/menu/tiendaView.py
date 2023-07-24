import tkinter as tk
# import notebook as nt
import presentacion.menu.counterComponent as counter
import presentacion.menu.storeSectionManager as manager
import presentacion.constants as cons
class TiendaView():
     def __init__(self,root) -> None:
        self.root=root
        # Main canvas
        self.backgroundImage=tk.PhotoImage(file="images/fondo_login.gif")
        self.moneyImage=tk.PhotoImage(file="images/COIN.png")
        self.bgWidth = self.backgroundImage.width()
        self.bgHeight = self.backgroundImage.height()
        self.canvas=tk.Canvas(self.root, width=self.bgWidth, height=self.bgHeight,bd=0,borderwidth=0,highlightthickness=0)
        # Marco canvas
        self.marcoImage=tk.PhotoImage(file="images/marcoTiendaPrueba.png")
        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.x = (self.bgWidth - self.ancho_marco) // 2
        self.y = (self.bgHeight - self.alto_marco) // 2

     #    self.container=tk.Frame(self.canvas)
        # Frames
        ## Main frame
        self.mainFrame=tk.Frame(self.canvas,bg="#8f563b", width=100, height=100,bd=0,borderwidth=0,highlightthickness=0)
        ## Left frame
        self.leftFrame=tk.Frame(self.mainFrame,bg="red")
        ### Left content

        ## RightFrame
        self.rightFrame=tk.Frame(self.mainFrame,bg="brown", width=300,height=400)
        ## Right content
        self.topRightFrame=tk.Frame(self.rightFrame,bg="#8f563b", width=200,height=187)
        self.bottomRightFrame=tk.Frame(self.rightFrame,bg="#8f563b", width=200,height=187)
        
        self.imagenObjeto=tk.PhotoImage(file="images/espadawmarco.png")
        self.nombreObjetoLabel=tk.Label(self.topRightFrame, text="Espada Llameante I", bg="#8f563b", font=cons.FONT_FAMILY1)
        self.descripcionObjeto=tk.Label(self.topRightFrame, text="[Descripción obtejo]", bg="#8f563b", font=cons.FONT_FAMILY1)
        self.canvasObject=tk.Canvas(self.topRightFrame, width=self.imagenObjeto.width(), height=self.imagenObjeto.height(),bd=0,borderwidth=0,highlightthickness=0)
        print(self.imagenObjeto)
        self.espadaReference=self.canvasObject.create_image(0,0,anchor="nw", image=self.imagenObjeto)

        self.counterComponent=counter.CounterComponent(self.bottomRightFrame, cons.FONT_FAMILY1, cons.BUTTON_LAYOUT)
        # self.priceLabel=tk.Label(self.bottomRightFrame, text=str(300*self.counterComponent.valor))
        
        # Components
        self.managerFrame=manager.SectionManager(self.leftFrame,10, [{'Armas':
                                                 [{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'}]},
                                            {'Armaduras':
                                                 [{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'}]},
                                            {'Accesorios':
                                                 [{'NOMBRE_OBJETO':''},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':''}]},
                                            {'Consumibles':
                                                 [{'NOMBRE_OBJETO':'Espada Llameante I'}]},
                                             {'Todos':[{'NOMBRE_OBJETO':" "},{"NOMBRE_OBJETO":" "},{"NOMBRE_OBJETO":" "}]}])
        self.moneyLabel=tk.Label(self.canvas, text=f"{10000000000}", bg="#d9a066", font=cons.FONT_FAMILY1, foreground=cons.COLOR_AMARILLO)
        self.canvas.create_image(0, 0, anchor="nw", image=self.backgroundImage)
        self.canvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)
        self.canvas.create_image(630, 40, anchor="nw", image=self.moneyImage)
        self.managerFrame.startObjectComp()
     def show(self):
        # CANVAS
        
        
        
        # FRAMES
        self.mainFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.leftFrame.pack(side="left")
        self.rightFrame.pack( anchor="center")

        # Right content
        self.topRightFrame.pack()
        self.bottomRightFrame.pack(pady=18, padx=10)
        self.canvasObject.pack()

        self.nombreObjetoLabel.pack()
        self.descripcionObjeto.pack()
        
        # self.priceLabel.pack()
        self.counterComponent.show()
        # Component
        self.managerFrame.show()


        self.moneyLabel.place(relx=0.8,rely=0.1)
     def hide(self):
         self.canvas.pack_forget()
         self.managerFrame.hide()
# root=tk.Tk()
# oTienda=TiendaView(root)
# oTienda.show()

# root.mainloop()