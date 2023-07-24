import tkinter as tk
import presentacion.menu.tableComp as tableComp
import presentacion.constants as cons
class SolicitudView():
    def __init__(self,root) -> None:
        self.container=tk.Frame(root,bg="#8f563b")
        self.topDescriptionFrame=tk.Frame(self.container,bg="#8f563b")
        self.bottomDescriptionFrame=tk.Frame(self.container,bg="#8f563b", relief=tk.RAISED)
        self.leftFrame=tk.Frame(self.topDescriptionFrame, bg="#8f563b")
        self.rightFrame=tk.Frame(self.topDescriptionFrame, bg="#8f563b")
        self.topSecFrame=tk.Frame(self.rightFrame)
        self.bottomSecFrame=tk.Frame(self.rightFrame)

        self.tableComp=tableComp.TableComp(self.leftFrame,tableComp.data)
     

        self.acceptBtn=tk.Button(self.bottomSecFrame,text="Aceptar", font=cons.FONT_FAMILY1,activeforeground="black", activebackground="#eec39a", bg="#eec39a", foreground="black")
        self.rejectBtn=tk.Button(self.bottomSecFrame,text="Rechazar", font=cons.FONT_FAMILY1,activeforeground="black", activebackground="#eec39a", bg="#eec39a", foreground="black")
        self.backBtn=tk.Button(self.bottomDescriptionFrame,text="Volver", font=cons.FONT_FAMILY1,activeforeground="black", activebackground="#eec39a", bg="#eec39a", foreground="black")

        self.descriptionLabel=tk.Label(self.rightFrame, text="Descripción del clan",bg="#8f563b",font=cons.FONT_FAMILY1)
        self.characterNameLabel=tk.Label(self.topSecFrame, text="Nombre del personaje")

        self.tableComp.start()
    def show(self):
        self.container.pack()
        self.topDescriptionFrame.pack()
        self.leftFrame.pack(side="left",pady=10, padx=10)
        self.rightFrame.pack()
        self.topSecFrame.pack(pady=10, padx=10)
        self.bottomSecFrame.pack(pady=10, padx=10)


        self.acceptBtn.pack()
        self.rejectBtn.pack()
        # self.descriptionLabel.pack()
        self.characterNameLabel.pack()
        self.tableComp.show()

        

    def hide(self):
        pass
    

# root=tk.Tk()
# oComp=SolicitudView(root)
# oComp.show()
# root.mainloop()