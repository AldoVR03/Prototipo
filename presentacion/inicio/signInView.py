import tkinter as tk
import presentacion.constants as cons
import tkinter.ttk as ttk
import presentacion.constants as cons

class SignInView():
    def __init__(self,marcoFrame) -> None:
        self.marcoFrame=marcoFrame
        self.signInFrame=tk.Frame(self.marcoFrame,bg="#8f563b",bd=0)
        self.buttonFrame=tk.Frame(self.signInFrame,bg="#8f563b",bd=0)
        self.radioButtonFrame=tk.Frame(self.signInFrame,bg="#8f563b",bd=0)
        self.radioVar=tk.IntVar(value=1)


        self.signInLabel=tk.Label(self.signInFrame,text="Registrarse",font=cons.FONT_FAMILY2, bg="#8f563b")

        self.signInUsernameLabel=tk.Label(self.signInFrame,text="Nombre de usuario",font=cons.FONT_FAMILY1, bg="#8f563b")
        self.signInUsernameEntry=tk.Entry(self.signInFrame,bg="#d9a066",bd=0,font=cons.FONT_FAMILY1)

        self.signInNicknameLabel=tk.Label(self.signInFrame,text="Apodo",font=cons.FONT_FAMILY1, bg="#8f563b")
        self.signInNicknameEntry=tk.Entry(self.signInFrame,bg="#d9a066",bd=0,font=cons.FONT_FAMILY1)

        self.signInPasswordLabel=tk.Label(self.signInFrame,text="Contraseña",font=cons.FONT_FAMILY1, bg="#8f563b")
        self.signInPasswordEntry=tk.Entry(self.signInFrame,bg="#d9a066",bd=0,font=cons.FONT_FAMILY1)
        
        self.jugadorRadioBtn=tk.Radiobutton(self.radioButtonFrame, text="Jugador", value=1,variable=self.radioVar, takefocus=False,background="#8f563b",activebackground="#8f563b",font=cons.FONT_FAMILY1 )
        self.gmRadioBtn=tk.Radiobutton(self.radioButtonFrame, text="GM", value=2,variable=self.radioVar, takefocus=False,background="#8f563b",activebackground="#8f563b",font=cons.FONT_FAMILY1 )

        self.signInBtn=tk.Button(self.buttonFrame,text="Registrarse",font=cons.FONT_FAMILY1)
        self.signInBackBtn=tk.Button(self.buttonFrame,text="Volver",font=cons.FONT_FAMILY1)
    def show(self):
        # reset
        self.reset()
        self.signInFrame.pack()
        self.signInUsernameEntry.focus_set()
  

        self.signInLabel.pack()

        self.signInUsernameLabel.pack()
        self.signInUsernameEntry.pack()

        self.signInNicknameLabel.pack()
        self.signInNicknameEntry.pack()

        self.signInPasswordLabel.pack()
        self.signInPasswordEntry.pack()

        self.jugadorRadioBtn.pack(side="left")
        self.gmRadioBtn.pack(side="left")
        
        self.signInBtn.pack(**cons.BUTTON_LAYOUT,pady=5)
        self.signInBackBtn.pack(**cons.BUTTON_LAYOUT,pady=5)


        self.radioButtonFrame.pack(pady=5)
        self.buttonFrame.pack(pady=5,**cons.BUTTON_LAYOUT)
    def reset(self):
        # Reset
        self.signInUsernameEntry.delete(0,tk.END)
        self.signInPasswordEntry.delete(0,tk.END)
        self.signInNicknameEntry.delete(0,tk.END)
        


        