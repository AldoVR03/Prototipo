import tkinter as tk

class cambioClave:
    def cambio_clave(self, ventana):
        self.ventana=ventana
        #Destruye la ventana anterior
        self.ventana.destroy()
        #Generar ventana
        self.ventana_registro = tk.Tk()
        self.ventana_registro.title("Cambio de contraseña")
        self.ventana_registro.config(bg="#fcfcfc")

        screen_width = self.ventana_registro.winfo_screenwidth()
        screen_height = self.ventana_registro.winfo_screenheight()

        print(screen_width)
        print(screen_height)
        window_width = 1200
        window_height = 478
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2


        self.ventana_registro.geometry(f"{window_width}x{window_height}+{x}+{y}")

        etiqueta_usuario_recuperar = tk.Label(text="Ingresa el nombre de usuario",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_usuario_recuperar.pack()
        self.usuario_recuperar = tk.Entry(font=("Times",14))
        self.usuario_recuperar.pack()

        etiqueta_clave_actual = tk.Label(text="Ingrese la clave anterior",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_clave_actual.pack()
        self.clave_actual = tk.Entry(font=("Times",14))
        self.clave_actual.pack()

        etiqueta_clavenueva = tk.Label(text="Ingrese la nueva clave",font=("Times",14),height=1,bg="#fcfcfc")
        etiqueta_clavenueva.pack()
        self.clave_nueva = tk.Entry(font=("Times",14))
        self.clave_nueva.pack()

        registrars= tk.Button(text="Cambiar contraseña",
                                font=("Times",14),
                                bg="#FFFFFF")
        registrars.pack()