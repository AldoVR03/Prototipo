import tkinter as tk
import constants as consts
import tkinter.ttk as ttk

class SignInView():
    def __init__(self,marcoFrame) -> None:
        self.marcoFrame=marcoFrame
        self.signInFrame=tk.Frame(self.marcoFrame,bg="#8f563b",bd=0)
        self.radioVar=tk.IntVar(value=1)

        self.signInLabel=tk.Label(self.signInFrame,text="Registrarse",font=consts.FONT_FAMILY2, bg="#8f563b")

        self.signInUsernameLabel=tk.Label(self.signInFrame,text="Nombre de usuario",font=consts.FONT_FAMILY1, bg="#8f563b")
        self.signInUsernameEntry=tk.Entry(self.signInFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)

        self.signInNicknameLabel=tk.Label(self.signInFrame,text="Apodo",font=consts.FONT_FAMILY1, bg="#8f563b")
        self.signInNicknameEntry=tk.Entry(self.signInFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)

        self.signInPasswordLabel=tk.Label(self.signInFrame,text="Contraseña",font=consts.FONT_FAMILY1, bg="#8f563b")
        self.signInPasswordEntry=tk.Entry(self.signInFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)
        
        self.jugadorRadioBtn=ttk.Radiobutton(self.signInFrame, text="Jugador", value=1,variable=self.radioVar )
        self.gmRadioBtn=ttk.Radiobutton(self.signInFrame, text="GM", value=2,variable=self.radioVar )

        self.signInBackBtn=tk.Button(self.signInFrame,text="Volver",font=consts.FONT_FAMILY1)
    def showSignInView(self):
        self.signInLabel.pack()

        self.signInUsernameLabel.pack()
        self.signInUsernameEntry.pack()

        self.signInNicknameLabel.pack()
        self.signInNicknameEntry.pack()

        self.signInPasswordLabel.pack()
        self.signInPasswordEntry.pack()

        self.jugadorRadioBtn.pack()
        self.gmRadioBtn.pack()


        self.signInBackBtn.pack(**consts.BUTTON_LAYOUT)