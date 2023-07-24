import tkinter as tk 
import presentacion.menu.tableComp as tableComp
import presentacion.menu.descriptionComp as descriptionComp
import presentacion.constants as cons
import presentacion.menu.windowDialog as window

class ClanDescriptionView():
    def __init__(self,root) -> None:
        self.container=tk.Frame(root,bg="#8f563b")
        self.topDescriptionFrame=tk.Frame(self.container,bg="#8f563b")
        self.bottomDescriptionFrame=tk.Frame(self.container,bg="#8f563b", relief=tk.RAISED)
        self.leftFrame=tk.Frame(self.topDescriptionFrame, bg="#8f563b")
        self.rightFrame=tk.Frame(self.topDescriptionFrame, bg="#8f563b")
        self.descriptionBtnFrame=tk.Frame(self.bottomDescriptionFrame)
        self.tableComp=tableComp.TableComp(self.leftFrame,tableComp.data)
        self.descriptionComp=descriptionComp.DescriptionComp(self.rightFrame)

        self.descriptionLabel=tk.Label(self.rightFrame, text="Descripción del clan",bg="#8f563b",font=cons.FONT_FAMILY1)
        

        self.clanReqBtn=tk.Button(self.descriptionBtnFrame,text="Solicitar unirse", font=cons.FONT_FAMILY1,activeforeground="black", activebackground="#eec39a", bg="#eec39a", foreground="black")
        self.clanCreateBtn=tk.Button(self.descriptionBtnFrame,text="Crear clan", font=cons.FONT_FAMILY1,activeforeground="black", activebackground="#eec39a", bg="#eec39a", foreground="black", command=self.openWindow)
        self.backBtn=tk.Button(self.bottomDescriptionFrame,text="Volver", font=cons.FONT_FAMILY1,activeforeground="black", activebackground="#eec39a", bg="#eec39a", foreground="black")
        self.window=None
        self.tableComp.start()
    def show(self):
        self.container.pack()

        self.topDescriptionFrame.pack()
        self.leftFrame.pack(side="left", padx=10, pady=10)
        self.rightFrame.pack()

        self.descriptionLabel.pack(pady=2)
        
        
        self.tableComp.show()
        self.descriptionComp.show()

        self.clanReqBtn.pack()
        self.clanCreateBtn.pack(fill="both", expand=True)
        self.backBtn.pack(side="left", anchor="sw")

        self.bottomDescriptionFrame.pack(fill="both",expand=True, padx=5, pady=5)
        self.descriptionBtnFrame.pack(side="right")


        
        
    def hide(self):
        pass
    def openWindow(self):
        self.window=window.Window()
        self.window.topLevel.grab_set()
    

# root=tk.Tk()
# oComp=ClanDescriptionView(root)
# oComp.show()
# root.mainloop()