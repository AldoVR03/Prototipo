import tkinter as tk
import tkinter.ttk as ttk
import presentacion.constants as consts
class LoginView():
    def __init__(self,marcoFrame) -> None:
        self.marcoFrame=marcoFrame
        self.loginFrame=tk.Frame(self.marcoFrame,bg="#8f563b",bd=0)
        self.radioButtonFrame=tk.Frame(self.loginFrame,bg="#8f563b",bd=0)

        self.radioVar=tk.IntVar(value=1)
        self.style=ttk.Style()
        self.style.configure("TRadiobutton",
                            background="#8f563b",
                            font=consts.FONT_FAMILY1
                            )  
        self.loginLabel=tk.Label(self.loginFrame,text="Iniciar sesión", bg="#8f563b",font=consts.FONT_FAMILY2)

        # Label-Entry section
        self.userNameLabel=tk.Label(self.loginFrame,text="Nombre de usuario", bg="#8f563b",font=consts.FONT_FAMILY1)
        self.usernameEntry=tk.Entry(self.loginFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)

        self.passwordLabel=tk.Label(self.loginFrame,text="Contraseña", bg="#8f563b",font=consts.FONT_FAMILY1)
        self.passwordEntry=tk.Entry(self.loginFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)

        self.jugadorRadioBtn=tk.Radiobutton(self.radioButtonFrame, text="Jugador", value=1,variable=self.radioVar,takefocus=False,background="#8f563b", activebackground="#8f563b" ,font=consts.FONT_FAMILY1)
        self.gmRadioBtn=tk.Radiobutton(self.radioButtonFrame, text="GM", value=2,variable=self.radioVar, takefocus=False ,background="#8f563b",activebackground="#8f563b",font=consts.FONT_FAMILY1)

        self.loginBtn=tk.Button(self.loginFrame,text="Iniciar sesión",font=consts.FONT_FAMILY1)
        self.loginSignInBtn=tk.Button(self.loginFrame,text="Registrase",font=consts.FONT_FAMILY1)
        self.loginPasswordBtn=tk.Button(self.loginFrame,text="Cambiar contraseña",font=consts.FONT_FAMILY1)

        

        

    def show(self):
        self.reset()
        self.usernameEntry.focus_set()
        self.jugadorRadioBtn.focus_set()

        self.loginLabel.pack()

        self.userNameLabel.pack()
        self.usernameEntry.pack(pady=5) 
        self.passwordLabel.pack()
        self.passwordEntry.pack()

        self.radioButtonFrame.pack()
        self.jugadorRadioBtn.pack(side="left")
        self.gmRadioBtn.pack(side="left")
        
        self.loginBtn.pack(pady=5,**consts.BUTTON_LAYOUT)
        self.loginSignInBtn.pack(pady=5,**consts.BUTTON_LAYOUT)
        self.loginPasswordBtn.pack(pady=5,**consts.BUTTON_LAYOUT)

        
    def reset(self):
        # Reset
        self.usernameEntry.delete(0,tk.END)
        self.passwordEntry.delete(0,tk.END)
    def hide(self):
        self.loginFrame.pack_forget()