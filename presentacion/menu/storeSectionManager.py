import tkinter as tk

import presentacion.constants as cons
import presentacion.menu.storeObjectComponent as SOC
# import scrollframepba as SOC
import random
import time

class SectionManager():
    def __init__(self,root, length, packList) -> None:

        self.tabContainer=tk.Frame(root, bg="#8f563b")
        self.tabFrame=tk.Frame(self.tabContainer, bg="#8f563b")
        self.contentTabFrame=tk.Frame(self.tabContainer, bg="#8f563b")
    
        # Lista de objetos provenientes de la BD. 
        # Ya convertidas en un formato que pueda ser usado. 
        # Diccionario con clave de el tipo de objeto y como valor una lista de objetos.  
        # ej: [{"Armas":[<dictObjects>]},{"Armaduras":[<dictObjects>]},{"Consumibles":[<dictObjects>]}]

        self.packList=packList
        self.length=length
        # Contenedor de pestañas y contenido
        
        # self.notebook = ttk.Notebook(root)
        self.tabText=[ "Todos",'Armas','Consumibles',"Accesorios","Armaduras"]
        self.tabObjects={}    #En este caso son botones
       
        # Objetos de tipo SOC.ObjectFrameComponent
        self.objectCompList={}

        self.tabContentFrames={}

        # Images
        self.imageUnpressed=tk.PhotoImage(file="images/botonTienda.png")
        self.imagePressed=tk.PhotoImage(file="images/botonTiendaOver.png")

        for i in range(len(self.tabText)):
            self.tabObjects[self.tabText[i]]=(tk.Button(self.tabFrame,text=self.tabText[i],image=self.imageUnpressed,bg="#8f563b", activebackground="brown",bd=0,relief=tk.FLAT, highlightthickness=0, compound="center", font=("Unispace",11)))
            self.tabObjects[self.tabText[i]].bind("<ButtonPress>", lambda event: self.on_button_press(event))
            

            # print(self.tabText[i])
            
        # print(self.tabObjects)

        self.length = length
        self.rows=0
        # print(imageList)
        if self.length%2!=0:
            self.rows=(self.length+1)//2
            # print(self.length)
        else:
            self.rows=self.length//2
        self.imageFrame1=None

        self.isSelected=None
        # print(self.tabObjects)
        self.showStart()
    def startObjectComp(self):
        for key,value in self.objectCompList.items():
            print(key)
            self.objectCompList[key].start()
    def showStart(self):

        
        self.tabFrame.pack(pady=5)
        self.contentTabFrame.pack()


        # Muestra los botones con grid 2X3
        buttonLength=0
        for i in range(len(self.tabObjects)//2):
            # print(index)
            for j in range(5):
                if buttonLength==len(self.tabObjects):
                    break

                self.tabObjects[self.tabText[buttonLength]].grid(row=i,column=j)
                # print(i,j)

                # print("HOLA",index)
                # self.objectList.append()
                # print(buttonLength)
                buttonLength+=1

        length=0
        objElem=None
        for tab in self.tabObjects:
            # print(tab)
            for obj in self.packList:  #-> {"Armas":[{},{},{}],"Armadura":[{},{},{}],"Consumibles":[{},{},{}]}
                if(tab in obj):

                    length= len(obj[tab])
                    objElem=obj
            oComponent= SOC.ObjectFrameComponent(self.contentTabFrame, length,self.determineImages(objElem,tab), 2)
                    
            # Guarda referencias a los objetos de contenido de cada tab
            # print(tab)
            self.objectCompList[tab]=oComponent
            
        self.startObjectComp()
        self.objectCompList["Todos"].show()

        # self.objectCompList["Todos"].start()
        self.isSelected=[self.objectCompList["Todos"],self.tabObjects["Todos"]]
        self.tabObjects["Todos"].config(image=self.imagePressed)
        

        

    def determineImages(self, objElem, elem):
        print("hola")
        imageList=[]
        for key,value in objElem.items():
            for obj in value:
                if(obj["NOMBRE_OBJETO"]=="Espada Llameante I"):
                    imageList.append(tk.PhotoImage(file="images/espadawmarco.png"))
                else:
                    imageList.append(tk.PhotoImage(file="images/NF.png"))
        print(imageList)
        return imageList

    def on_button_press(self,evento):
        print(self.isSelected, self.objectCompList[evento.widget["text"]])
        if self.isSelected:
            print("Entrando..")
            self.isSelected[0].hide()
            time.sleep(.1)
            self.objectCompList[evento.widget["text"]].show()
        
            self.isSelected[1].config(image=self.imageUnpressed)
            self.isSelected=[self.objectCompList[evento.widget["text"]],evento.widget]

            evento.widget.config(image=self.imagePressed)
    def show(self):
        self.tabContainer.pack()
    def hide(self):
        self.tabContainer.pack_forget()
        #     evento.widget.config(image=self.imagePressed)
        #     evento.widget.config(font=("Unispace",10))
        #     self.isSelected=(evento.widget)
        
        #     return 
        # self.isSelected.hide()
        # self.objectCompList[self.evento.widget["text"]].show()

        # evento.widget.config(image=self.imagePressed )

        # evento.widget.config(font=("Unispace",10))
        # self.isSelected=(evento.widget)

        # print(evento.widget["text"])
    



# ventana_principal = tk.Tk()
# ventana_principal.title("Tienda de Juego")
# # oComp=o(,10, [{'Armas':[{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'}]},
# #                                                  {'Armaduras':[{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'}]},
# #                                                  {'Accesorios':[{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'}]},
# #                                                  {'Consumibles':[{'NOMBRE_OBJETO':'Espada Llameante I'}]},{'Otros':[{'NOMBRE_OBJETO':""},{"NOMBRE_OBJETO":""},{"NOMBRE_OBJETO":""}]}])

# # oComp.show()
# # Resto de la interfaz de la tienda...
# oComp=SectionManager(ventana_principal,10, [{'Armas':
#                                                 [{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'}]},
#                                            {'Armaduras':
#                                                 [{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'}]},
#                                            {'Accesorios':
#                                                 [{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'},{'NOMBRE_OBJETO':'Espada Llameante I'}]},
#                                            {'Consumibles':
#                                                 [{'NOMBRE_OBJETO':'Espada Llameante I'}]},
#                                             {'Todos':[{'NOMBRE_OBJETO':" "},{"NOMBRE_OBJETO":" "},{"NOMBRE_OBJETO":" "}]}])

# oComp.show()

# # Iniciar el bucle principal de la ventana
# ventana_principal.mainloop()