import tkinter as tk
from tkinter.ttk import Style, Radiobutton


class FrameComponent():
    def __init__(self,root) -> None:
# Crear la ventana principal

# Cargar las imágenes

        self.selected_image5 = tk.PhotoImage(file="images/selectedColor5.png")
        self.unselected_image5 = tk.PhotoImage(file="images/unselectedColor5.png")

        self.selected_image4 = tk.PhotoImage(file="images/selectedColor4.png")
        self.unselected_image4 = tk.PhotoImage(file="images/unselectedColor4.png")

        self.selected_image3 = tk.PhotoImage(file="images/selectedColor3.png")
        self.unselected_image3 = tk.PhotoImage(file="images/unselectedColor3.png")

        self.selected_image2 = tk.PhotoImage(file="images/selectedColor2.png")
        self.unselected_image2 = tk.PhotoImage(file="images/unselectedColor2.png")

        self.selected_image1 = tk.PhotoImage(file="images/selectedColor1.png")
        self.unselected_image1 = tk.PhotoImage(file="images/unselectedColor1.png")


        # Crear estilo personalizado para reemplazar el círculo por una imagen
        self.style = Style()
        self.style.element_create('Custom.Radiobutton.indicator5', 'image', self.selected_image5, ('selected', self.selected_image5), ('!selected', self.unselected_image5))
        self.style.layout('Custom.TRadiobutton5', [('Radiobutton.padding', {'sticky': 'nswe'}), ('Custom.Radiobutton.indicator5', {'side': 'left', 'sticky': ''})])

        self.style.element_create('Custom.Radiobutton.indicator4', 'image', self.selected_image4, ('selected', self.selected_image4), ('!selected', self.unselected_image4))
        self.style.layout('Custom.TRadiobutton4', [('Radiobutton.padding', {'sticky': 'nswe'}), ('Custom.Radiobutton.indicator4', {'side': 'left', 'sticky': ''})])

        self.style.element_create('Custom.Radiobutton.indicator3', 'image', self.selected_image3, ('selected', self.selected_image3), ('!selected', self.unselected_image3))
        self.style.layout('Custom.TRadiobutton3', [('Radiobutton.padding', {'sticky': 'nswe'}), ('Custom.Radiobutton.indicator3', {'side': 'left', 'sticky': ''})])

        self.style.element_create('Custom.Radiobutton.indicator2', 'image', self.selected_image2, ('selected', self.selected_image2), ('!selected', self.unselected_image2))
        self.style.layout('Custom.TRadiobutton2', [('Radiobutton.padding', {'sticky': 'nswe'}), ('Custom.Radiobutton.indicator2', {'side': 'left', 'sticky': ''})])

        self.style.element_create('Custom.Radiobutton.indicator1', 'image', self.selected_image1, ('selected', self.selected_image1), ('!selected', self.unselected_image1))
        self.style.layout('Custom.TRadiobutton1', [('Radiobutton.padding', {'sticky': 'nswe'}), ('Custom.Radiobutton.indicator1', {'side': 'left', 'sticky': ''})])


        # Variable de control
        self.selection = tk.StringVar()

        # Aplicar estilo personalizado al Radiobutton

        self.style.configure('Custom.TRadiobutton5', background='white')
        self.style.configure('Custom.TRadiobutton5', font=('Arial', 12))

        self.style.configure('Custom.TRadiobutton4', background='white')
        self.style.configure('Custom.TRadiobutton4', font=('Arial', 12))

        self.style.configure('Custom.TRadiobutton3', background='white')
        self.style.configure('Custom.TRadiobutton3', font=('Arial', 12))

        self.style.configure('Custom.TRadiobutton2', background='white')
        self.style.configure('Custom.TRadiobutton2', font=('Arial', 12))

        self.style.configure('Custom.TRadiobutton1', background='white')
        self.style.configure('Custom.TRadiobutton1', font=('Arial', 12))

        self.skinFrame=tk.Frame(root, bg="#8f563b")
        
        self.skinColorLabel=tk.Label(self.skinFrame,text="Color de piel", bg="#8f563b")    
        # Crear los Radiobutton con la imagen personalizada
        self.radiobutton5 = Radiobutton(self.skinFrame, text="Opción 1", variable=self.selection, value="48,27,23,255", command=self.change_selection, style='Custom.TRadiobutton5')
        self.radiobutton4 = Radiobutton(self.skinFrame, text="Opción 2", variable=self.selection, value="143,86,59,255", command=self.change_selection, style='Custom.TRadiobutton4')
        self.radiobutton3 = Radiobutton(self.skinFrame, text="Opción 3", variable=self.selection, value="223,113,38,255", command=self.change_selection, style='Custom.TRadiobutton3')
        self.radiobutton2 = Radiobutton(self.skinFrame, text="Opción 4", variable=self.selection, value="217,160,102,255", command=self.change_selection, style='Custom.TRadiobutton2')
        self.radiobutton1 = Radiobutton(self.skinFrame, text="Opción 5", variable=self.selection, value="238,195,154,255", command=self.change_selection, style='Custom.TRadiobutton1')
        

        

    def change_selection(self):
        selected_option = self.selection.get()

        return tuple([int(value) for value in selected_option.split(",")])
        
    def show(self):
        self.skinFrame.pack()
        self.skinColorLabel.pack(pady=10)
        self.radiobutton5.pack(side="left", padx=1, pady=4)
        self.radiobutton4.pack(side="left", padx=2)
        self.radiobutton3.pack(side="left", padx=2)
        self.radiobutton2.pack(side="left", padx=2)
        self.radiobutton1.pack(side="right", padx=1)
# root=tk.Tk()

# comp=FrameComponent(root)
# comp.show()
# root.mainloop()
# Código adicional...

# Iniciar el bucle principal
