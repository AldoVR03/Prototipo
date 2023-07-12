import tkinter as tk
from loginView import *
from signInView import *
from passwordView import *
class ControllerInicio():
    def __init__(self,p1) -> None:
        self.marcoFrame=p1.marcoFrame
        self.contentFrame=p1.contentFrame
        self.mainCanvas=p1.mainCanvas
        self.backgroundImage=p1.backgroundImage
        self.marcoImage=p1.marcoImage
        self.x=p1.x
        self.y=p1.y
        self.oLogin=LoginView(self.marcoFrame)
        self.oRegistro=SignInView(self.marcoFrame)
        self.oPassword=PasswordView(self.marcoFrame)

        style=ttk.Style()
        style.configure("TRadiobutton",
                    background="#8f563b")
        self.oLogin.loginSignInBtn.configure(command=lambda:self.changeMainView("R"))
        self.oLogin.loginPasswordBtn.configure(command=lambda:self.changeMainView("P"))
        # SignIn
        self.oRegistro.signInBackBtn.configure(command=lambda:self.changeSecondaryViews("R"))
        # Password
        self.oPassword.passwordBackBtn.configure(command=lambda:self.changeSecondaryViews("P"))
        self.contentFrame=self.oLogin.loginFrame

    def showLoginFrame(self):
        self.hideFrames()
        self.mainCanvas.pack()
        self.mainCanvas.create_image(0, 0, anchor="nw", image=self.backgroundImage)
        self.mainCanvas.create_image(self.x, self.y, anchor="nw", image=self.marcoImage)
        self.marcoFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.contentFrame.pack()
        self.oLogin.show()     
    def showSignInFrame(self):
        self.hideFrames()

        self.contentFrame.pack()
        self.oRegistro.showSignInView()
    def showPasswordFrame(self):
        self.hideFrames()

        self.contentFrame.pack()
        self.oPassword.showPasswordView()
    def hideFrames(self):
        self.oLogin.loginFrame.pack_forget()
        self.oRegistro.signInFrame.pack_forget()
        self.oPassword.passwordFrame.pack_forget()
    def changeMainView(self,view):
        if(view=="R"):
            self.contentFrame.pack_forget()
            self.contentFrame=self.oRegistro.signInFrame
            self.showSignInFrame()
        elif(view=="P"):
            self.contentFrame.pack_forget()
            self.contentFrame=self.oPassword.passwordFrame
            self.showPasswordFrame()
    def changeSecondaryViews(self,view):
        if(view=="R"):
            self.contentFrame.pack_forget()
            self.contentFrame=self.oLogin.loginFrame
            self.showLoginFrame()
        elif(view=="P"):
            self.contentFrame.pack_forget()
            self.contentFrame=self.oLogin.loginFrame
            self.showLoginFrame()