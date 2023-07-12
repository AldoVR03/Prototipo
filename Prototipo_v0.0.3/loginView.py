import tkinter as tk
import tkinter.ttk as ttk
import constants as consts
class LoginView():
    def __init__(self,marcoFrame) -> None:
        self.marcoFrame=marcoFrame
        self.loginFrame=tk.Frame(self.marcoFrame,bg="#8f563b",bd=0)

        self.radioVar=tk.IntVar(value=1)
        self.style=ttk.Style()
        self.style.configure("TRadiobutton",
                            background="#8f563b",
                            font=consts.FONT_FAMILY1
                            )  
        self.loginLabel=tk.Label(self.loginFrame,text="Iniciar sesión", bg="#8f563b",font=consts.FONT_FAMILY1)
        self.usernameEntry=tk.Entry(self.loginFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)
        self.passLabel=tk.Label(self.loginFrame,text="Contraseña", bg="#8f563b",font=consts.FONT_FAMILY1)
        self.passwordEntry=tk.Entry(self.loginFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)

        self.jugadorRadioBtn=ttk.Radiobutton(self.loginFrame, text="Jugador", value=1,variable=self.radioVar )
        self.gmRadioBtn=ttk.Radiobutton(self.loginFrame, text="GM", value=2,variable=self.radioVar )

        self.loginBtn=tk.Button(self.loginFrame,text="Iniciar sesión",font=consts.FONT_FAMILY1)
        self.loginSignInBtn=tk.Button(self.loginFrame,text="Registrase",font=consts.FONT_FAMILY1)
        self.loginPasswordBtn=tk.Button(self.loginFrame,text="Cambiar contraseña",font=consts.FONT_FAMILY1)

    def show(self):
        self.loginLabel.pack()
        self.usernameEntry.pack(pady=5) 
        self.passLabel.pack(pady=5)
        self.passwordEntry.pack()
        self.passwordEntry.config(show="*")
        self.gmRadioBtn.pack()
        self.jugadorRadioBtn.pack()
        self.loginBtn.pack(pady=5,**consts.BUTTON_LAYOUT)
        self.loginSignInBtn.pack(pady=5,**consts.BUTTON_LAYOUT)
        self.loginPasswordBtn.pack(pady=5,**consts.BUTTON_LAYOUT)