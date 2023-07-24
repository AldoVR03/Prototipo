import tkinter as tk

class Window():
    def __init__(self):
        self.marcoImage = tk.PhotoImage(file="images/MARCOTOP.png")

        self.ancho_marco = self.marcoImage.width()
        self.alto_marco = self.marcoImage.height()
        self.topLevel = tk.Toplevel()
        self.mainCanvas = tk.Canvas(self.topLevel, width=self.ancho_marco, height=self.alto_marco, bd=0, borderwidth=0, highlightthickness=0)
        self.mainCanvas.create_image(0, 0, anchor="nw", image=self.marcoImage)

        self.mainFrame=tk.Frame(self.mainCanvas)
        self.mainFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.mainCanvas.pack()

