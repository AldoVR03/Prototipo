import tkinter as tk
import presentacion.constants as cons
import tkinter.ttk as ttk

width=400
height=450

class DescriptionComp():
    def __init__(self,root) -> None:
        # self.clansListFrame=tk.Frame(root,bg="red",width=width,height=height)
        self.clanDescriptionFrame=tk.Frame(root,bg="blue")
        self.topDescriptionFrame=tk.Frame(self.clanDescriptionFrame, width=width,height=2*(height/3),bg="#8f563b")
        self.clanDescription=tk.Text(self.topDescriptionFrame, wrap=tk.WORD, width=20,height=13,bg="#b87556", foreground="#fbce36", font=cons.FONT_FAMILY1)
       

        # List frame

    def show(self):
        
        # self.clansListFrame.pack(side="left")
        self.clanDescriptionFrame.pack()
        self.topDescriptionFrame.pack()
        # self.bottomDescriptionFrame.pack(**cons.BUTTON_LAYOUT)

        self.clanDescription.pack(padx=5, pady=5)
        

        self.mostrar_descripcion("""El clan de los guerreros es conocido por su valentía y coraje en el campo de batalla. 
Sus miembros son expertos espadachines y arqueros, y siempre están dispuestos a defender a su clan 
con sus vidas.""")

    def hide(self):
        pass
    
    def mostrar_descripcion(self,descripcion):
      self.clanDescription.delete(1.0, tk.END)  # Borra el contenido actual del Text widget
      self.clanDescription.insert(tk.END, descripcion)
      self.clanDescription.config(state=tk.DISABLED)
      
    
    
    

# root=tk.Tk()
# oComp=listView(root)
# oComp.show()
# root.mainloop()