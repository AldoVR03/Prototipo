import tkinter as tk


class CounterComponent():
    def __init__(self,root, font, btnLayout) -> None:
        self.valor=1
        self.btnLayout=btnLayout
        self.container=tk.Frame(root,bg="#8f563b")
        self.btnContainer=tk.Frame(root)

        self.btn_decrementar = tk.Button(self.container, text="-", command=self.decrementar, font=font)
        self.btn_incrementar = tk.Button(self.container, text="+", command=self.incrementar,font=font)
        self.label_valor = tk.Label(self.container, text=str(self.valor), font=font, width=10)
        self.priceValue=500
        self.priceLabel=tk.Label(self.btnContainer,text=str(self.valor*self.priceValue), bg="#8f563b", font=font, foreground="Yellow")
        self.purchaseBtn=tk.Button(self.btnContainer, text="Comprar", command=lambda:print("Hola"), font=font)
        self.backBtn=tk.Button(self.btnContainer, text="Volver", command=lambda:print("Hola"), font=font)

    def show(self):
        
        self.priceLabel.pack()
        self.container.pack()
        self.btnContainer.pack()
        self.btn_decrementar.pack(side="left")
        self.label_valor.pack(side="left")
        self.btn_incrementar.pack(side="left")
        self.purchaseBtn.pack(**self.btnLayout)
        self.backBtn.pack(**self.btnLayout)
   
   

    def actualizar_valor(self,nuevo_valor):
        self.label_valor.config(text=str(nuevo_valor))
        self.priceLabel.config(text=str(self.valor*self.priceValue))

# Funciones de incremento y decremento
    def incrementar(self):
        self.valor += 1
        self.actualizar_valor(self.valor)

    def decrementar(self):  
        if self.valor >1:
            self.valor -= 1
            self.actualizar_valor(self.valor)
# ventana_principal = tk.Tk()

# # Valor numérico
# # valor = 10

# # # Función para actualizar el valor
# # def actualizar_valor(nuevo_valor):
# #     label_valor.config(text=str(nuevo_valor))

# # # Funciones de incremento y decremento
# # def incrementar():
# #     global valor
# #     valor += 1
# #     actualizar_valor(valor)

# # def decrementar():
# #     global valor
# #     valor -= 1
# #     actualizar_valor(valor)

# # # Crear el Frame contenedor
# # frame_contenedor = tk.Frame(ventana_principal)
# # frame_contenedor.pack(pady=10)

# # # Botón de decremento a la izquierda del Label
# # btn_decrementar = tk.Button(frame_contenedor, text="-", command=decrementar)
# # btn_decrementar.pack(side="left")

# # # Label para mostrar el valor
# # label_valor = tk.Label(frame_contenedor, text=str(valor), font=("Arial", 12), width=10, relief="solid")
# # label_valor.pack(side="left")

# # # Botón de incremento a la derecha del Label
# # btn_incrementar = tk.Button(frame_contenedor, text="+", command=incrementar)
# # btn_incrementar.pack(side="left")
# oComp=CounterComponent(ventana_principal)
# oComp.show()
# ventana_principal.mainloop()