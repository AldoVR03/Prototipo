import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import imageio

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.attributes("-fullscreen", True)
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        #GIF
        gif_path = "./img/fondo_login.gif"
        self.gif_frames = self.load_gif_frames(gif_path)
        self.current_frame = 0

        self.label_animacion = tk.Label(self.ventana)
        self.label_animacion.pack(fill="both", expand=True)

        self.frame_texto = tk.Frame(self.label_animacion, bg="#fcfcfc")
        self.frame_texto.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(self.frame_texto, text="Inicio de sesión", bg="#FFFFFF", font=("Times", 14))
        titulo.pack(padx=5, pady=40)

        etiqueta_usuario = tk.Label(self.frame_texto, text="Usuario", font=("Times", 14), height=3, bd=0, bg="#fcfcfc")
        etiqueta_usuario.pack(pady=5)
        self.usuario = tk.Entry(self.frame_texto, font=("Times", 14))
        self.usuario.pack()

        etiqueta_contraseña = tk.Label(self.frame_texto, text="Contraseña", font=("Times", 14), height=3, bg="#fcfcfc")
        etiqueta_contraseña.pack()

        self.contraseña = tk.Entry(self.frame_texto, font=("Times", 14))
        self.contraseña.pack()
        self.contraseña.config(show="*")

        inicio = tk.Button(self.frame_texto, text="Entrar", font=("Times", 14), fg="#fcfcfc", bg="#8A169E", command=self.verificar)
        inicio.pack(pady=25)

        self.animate_gif()  # Iniciar la animacion del GIF

        self.ventana.mainloop()

    def load_gif_frames(self, gif_path):
        # Cargar el GIF y extraer los fotogramas
        gif = imageio.mimread(gif_path)
        frames = [Image.fromarray(frame) for frame in gif]
        return frames

    def animate_gif(self):
        # Actualizar la imagen mostrada con el siguiente fotograma del GIF
        self.current_frame += 1
        if self.current_frame >= len(self.gif_frames):
            self.current_frame = 0

        self.animacion = ImageTk.PhotoImage(self.gif_frames[self.current_frame])
        self.label_animacion.config(image=self.animacion)

        self.ventana.after(100, self.animate_gif)  # Repetir la animación cada 100 ms

    def verificar(self):
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
        if usuario == "root" and contraseña == "1234":
            self.ventana.destroy()
            # Lógica adicional para abrir la nueva ventana o realizar otras acciones
        else:
            messagebox.showerror(message="Usuario o contraseña incorrecta")


App()
