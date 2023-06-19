import tkinter as tk
from PIL import ImageTk, Image

class menu_gm:

    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.window.bind("<Escape>", self.quitFullScreen)

        imagen_registro = ImageTk.PhotoImage(Image.open('./img/fondo_registro.png'))
        lable_registro = tk.Label(image=imagen_registro)
        lable_registro.pack()
        
        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)