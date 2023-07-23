import tkinter as tk
import tkinter.ttk as ttk
import presentacion.constants as consts
class PasswordView():
    def __init__(self,marcoFrame) -> None:

        # Fields
        self.passwordFrame=tk.Frame(marcoFrame,bg="#8f563b",bd=0)
        self.buttonFrame=tk.Frame(self.passwordFrame,bg="#8f563b",bd=0)
        self.radioButtonFrame=tk.Frame(self.passwordFrame,bg="#8f563b",bd=0)

        self.passwordLabel=tk.Label(self.passwordFrame,text="Cambiar contraseña",font=consts.FONT_FAMILY2, bg="#8f563b")
        self.radioVar=tk.IntVar(value=1)
        # Username section
        self.passwordUsernameLabel=tk.Label(self.passwordFrame,text="Nombre de usuario",font=consts.FONT_FAMILY1, bg="#8f563b")
        self.passwordUsernameEntry=tk.Entry(self.passwordFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)

        # Label-Entry section
        self.oldPassLabel=tk.Label(self.passwordFrame,text="Contraseña antigua",font=consts.FONT_FAMILY1, bg="#8f563b")
        self.oldPassEntry=tk.Entry(self.passwordFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)
        self.newPassLabel=tk.Label(self.passwordFrame,text="Contraseña nueva",font=consts.FONT_FAMILY1, bg="#8f563b")
        self.newPassEntry=tk.Entry(self.passwordFrame,bg="#d9a066",bd=0,font=consts.FONT_FAMILY1)
 
        # Radio Button
        self.jugadorRadioBtn=tk.Radiobutton(self.radioButtonFrame, text="Jugador", value=1,variable=self.radioVar,background="#8f563b", takefocus=False,activebackground="#8f563b",font=consts.FONT_FAMILY1 )
        self.gmRadioBtn=tk.Radiobutton(self.radioButtonFrame, text="GM", value=2,variable=self.radioVar,background="#8f563b", takefocus=False,activebackground="#8f563b",font=consts.FONT_FAMILY1 )
        # Button
        self.passBtn=tk.Button(self.buttonFrame,text="Cambiar contraseña",font=consts.FONT_FAMILY1)
        self.passwordBackBtn=tk.Button(self.buttonFrame,text="Volver",font=consts.FONT_FAMILY1)

    def show(self):
        # reset
        self.reset()
        self.passwordFrame.pack()
        self.passwordUsernameEntry.focus_set()
        

        self.passwordFrame.pack()
        self.passwordLabel.pack()
        
        # Username section
        self.passwordUsernameLabel.pack()
        self.passwordUsernameEntry.pack()

        # Password section
        self.oldPassLabel.pack()
        self.oldPassEntry.pack()
        self.newPassLabel.pack()
        self.newPassEntry.pack()
        
        # Button section
        self.jugadorRadioBtn.pack(side="left")
        self.gmRadioBtn.pack(side="left")
        self.passBtn.pack(**consts.BUTTON_LAYOUT, pady=5)
        self.passwordBackBtn.pack(**consts.BUTTON_LAYOUT)

        # Frames
        self.radioButtonFrame.pack()
        self.buttonFrame.pack(pady=10)

     
    def reset(self):
        # Reset
        self.passwordUsernameEntry.delete(0,tk.END)
        self.oldPassEntry.delete(0,tk.END)
        self.newPassEntry.delete(0,tk.END)
    def hide(self):
        self.passwordFrame.pack_forget()