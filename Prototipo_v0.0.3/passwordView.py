import tkinter as tk
import tkinter.ttk as ttk
import constants as consts
class PasswordView():
    def __init__(self,marcoFrame) -> None:
        self.marcoFrame=marcoFrame
        self.passwordFrame=tk.Frame(self.marcoFrame,bg="#8f563b",bd=0)
        self.passwordLabel=tk.Label(self.passwordFrame,text="Cambiar contraseña",font=consts.FONT_FAMILY2, bg="#8f563b")
        self.radioVar=tk.IntVar(value=1)

        self.passwordUsernameLabel=tk.Label(self.passwordFrame,text="Nombre de usuario",font=consts.FONT_FAMILY1, bg="#8f563b")
        self.passwordUsernameEntry=tk.Entry(self.passwordFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)

        self.passLabel=tk.Label(self.passwordFrame,text="Contraseña",font=consts.FONT_FAMILY1, bg="#8f563b")
        self.passEntry=tk.Entry(self.passwordFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)

        self.passBtn=tk.Button(self.passwordFrame,text="Cambiar contraseña",font=consts.FONT_FAMILY1)

        self.jugadorRadioBtn=ttk.Radiobutton(self.passwordFrame, text="Jugador", value=1,variable=self.radioVar )
        self.gmRadioBtn=ttk.Radiobutton(self.passwordFrame, text="GM", value=2,variable=self.radioVar )

        self.passwordBackBtn=tk.Button(self.passwordFrame,text="Volver",font=consts.FONT_FAMILY1)
    def showPasswordView(self):
        self.passwordLabel.pack()

        self.passwordUsernameLabel.pack()
        self.passwordUsernameEntry.pack()

        self.passLabel.pack()
        self.passEntry.pack(pady=20)
        self.passEntry.config(show="*")
        self.passBtn.pack(pady=20)
        self.passBtn.pack(**consts.BUTTON_LAYOUT)
        self.passwordBackBtn.pack(**consts.BUTTON_LAYOUT)