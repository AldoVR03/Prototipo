import tkinter as tk
from tkinter import ttk
import presentacion.constants as cons

import random
COLORES = ["red", "blue", "green", "yellow", "purple", "orange",'pink',"gray"]
class ObjectFrameComponent():
    def __init__(self, root, length, imageList,numCol,wframe, selectedImage):

        self.frameComp=tk.Frame(root)
      

        self.canvas = tk.Canvas(self.frameComp,bd=0,borderwidth=0,highlightthickness=0, bg="brown")
        self.scrollbar_vertical = tk.Scrollbar(self.frameComp, orient="vertical", command=self.canvas.yview)
        self.frame_interior = tk.Frame(self.canvas, bg="brown")
        # self.containerFrame=tk.Frame(self.frame_interior)
        
        self.canvas.configure(yscrollcommand=self.scrollbar_vertical.set)



        self.frame_interior.bind("<Configure>", self.configure_canvas)
        self.canvas.bind("<Enter>", self.on_enter)
        self.canvas.bind("<Leave>", self.on_leave)

        self.image1=tk.PhotoImage(file="images/espadawmarco.png")
        self.image2=tk.PhotoImage(file="images/marcoitem3.png")
        self.marcoEspadaMini=tk.PhotoImage(file="images/espadawmarcoMini.png")
        self.imageList=imageList
        self.selectedImage=selectedImage

        
        self.canvasList=[]
        self.frames = []
        self.length = length
        self.rows=0
        # print(imageList)
        if self.length%2!=0:
            self.rows=(self.length+1)//2
            # print(self.length)
        else:
            self.rows=self.length//2
        self.imageFrame1=None
        
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        print(self.imageList)

        self.numCol=numCol
        self.leftWidthFrame=201
        self.withFrame=wframe
        self.selectedItem=None

    def start(self):
        self.canvas.pack( side="left")
        
        self.canvas.create_window((0, 0), window=self.frame_interior, anchor="nw")
        


        index=0
        for i in range(self.rows):
            # print(index)
            for j in range(self.numCol):
                if len(self.frames)==self.length:
                    break

                canvas=None
                if self.withFrame:
                    canvas=None
                    print("holaaa")
                    frame = tk.Frame(self.frame_interior, width=1000, height=500, background=cons.BG_MARCO_TIENDA)
                    canvasRect=tk.Canvas(frame, bg=cons.BG_MARCO_TIENDA,bd=0,highlightthickness=0, width=self.image2.width(), height=self.image2.height())
                
                    canvasRect.create_image(0, 0, anchor="nw", image=self.image2)
                    frameMarco=tk.Frame(canvasRect, width=self.image2.width()-50,height=self.image2.height()-50, bg=cons.BG_MARCO_TIENDA)
                    
                    frame.grid(row=i, column=j, padx=2, pady=2)

                    leftFrame=tk.Frame(frameMarco,height=120, bg=cons.BG_MARCO_TIENDA)
                    rightFrame=tk.Frame(frameMarco,width=self.leftWidthFrame-10,height=120, bg=cons.BG_MARCO_TIENDA)

                    frameMarco.place(relx=0.5, rely=0.5, anchor="center")
                    
                    # self.imageFrame1=tk.Frame(leftFrame, width=100,height=100)
                    leftFrame.pack(side="left", padx=10)
                    # leftFrame.place(x=0,y=0)
                    rightFrame.pack(side="left")
                    # rightFrame.place(x=0,y=0)
                    
                    canvas=tk.Canvas(leftFrame, width=self.image1.width(), height=self.image1.height(), bg="brown",bd=0,highlightthickness=0)
                    # print(index)
                    canvasRef=canvas.create_image(0, 0, anchor="nw", image=self.imageList[index]) #image=self.imageList[index]
                    # canvasRef=canvas.create_image(0, 0, anchor="nw", image=self.image1)
                    canvas.pack(fill="both",side="bottom", padx=5)
                    canvas.config()
                    # canvas.bind("<Button-1>", self.on_canvas_click)
                    # canvas.bind("<Enter>", self.on_canvas_enter)
                    # canvas.bind("<Leave>", self.on_canvas_leave)
                    # print(index)
                    index+=1
                    canvasRect.pack(padx=2)
                    self.canvasList.append(canvas)
                    canvas=None
                else:
                    frame = tk.Frame(self.frame_interior, width=0, height=500, background=cons.BG_MARCO_TIENDA)
                    frame.grid(row=i, column=j, padx=1,pady=1)

                    leftFrame=tk.Frame(frame,height=120, bg=cons.BG_MARCO_TIENDA)
                    # rightFrame=tk.Frame(frame,width=0,height=120, bg=cons.BG_MARCO_TIENDA)

                    leftFrame.pack(side="left")
                    # leftFrame.place(x=0,y=0)
                    # rightFrame.pack(side="left")
                    # rightFrame.place(x=0,y=0)
                    
                    canvas=tk.Canvas(leftFrame, width=self.selectedImage.width(), height=self.selectedImage.height(), bg="brown",bd=0,highlightthickness=0)
                    # print(index,"a")
                    # canvasRef=canvas.create_image(0, 0, anchor="nw", image=self.imageList[index]) #image=self.imageList[index]
                    canvasRef=canvas.create_image(0, 0, anchor="nw", image=self.selectedImage)
                    canvas.pack(fill="both",side="bottom", expand=True)
                    canvas.config()
                    # canvas.bind("<Button-1>", self.on_canvas_click)
                    # canvas.bind("<Enter>", self.on_canvas_enter)
                    # canvas.bind("<Leave>", self.on_canvas_leave)
                    # print(index)
                    index+=1
                    self.canvasList.append(canvas)
                    canvas=None
                # print("hola")
                    # canvasRect.pack()
                # print("asdasd")
                # image=tk.PhotoImage("e.png")
                # canvas=tk.Canvas(leftFrame,width=self.imageA.width(),height=self.imageA.height())
                # print(self.imageA)
                # canvas.create_image(0, 0, anchor="nw", image= image)
                # canvas.pack()
                
                # # buyBtn=tk.Button(frame, text="Comprar")
                # buyBtn.pack()
                # self.canvasList[i]=(canvas,canvasRef)
                canvas=None
                self.frames.append(frame)
        # self.frameComp.update()
        print(len(self.frames))
        if self.withFrame:
            
            self.canvas.config(width=(self.image1.width()+self.leftWidthFrame)*self.numCol)
        else:
            
            self.canvas.config(width=(self.selectedImage.width()+2)*self.numCol)
        # self.containerFrame.pack(anchor="center", side="top")
            
    def show(self):
        self.frameComp.pack(padx=10)
    def on_canvas_click(self,event):
        print(f"Clic en el canvas {event.widget}")
        self.selectedItem=event.widget
        

    def on_canvas_enter(self,event):
        event.widget.config(cursor="hand2")

    def on_canvas_leave(self,event):
        event.widget.config(cursor="")
        

       
        

        
    def hide(self):

        # self.frameInterior.pack_forget()
        # self.canvas.pack_forget()
        self.frameComp.pack_forget()
    # def on_enter(self, event):
    #     self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    # def on_leave(self, event):
    #     self.canvas.unbind("<MouseWheel>")

    def configure_canvas(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # def on_mousewheel(self,event):
    #     self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
    def on_enter(self, event):
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_leave(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


# ventana_principal = tk.Tk()
# ventana_principal.title("Ejemplo de Grid con Scrollbar")


# oComp=ObjectFrameComponent(ventana_principal,40,[],3, False, tk.PhotoImage(file="images/espadawmarcoMini.png"))
# # oComp2=ObjectFrameComponent(ventana_principal,4)

# oComp.start()
# oComp.show()

# # oComp2.show()

# ventana_principal.mainloop()