from pubsub import pub
class ControllerMenu():
    def __init__(self,root) -> None:
        pub.subscribe(self.receiveNewPlayers, "NEW-PLAYER")
        pub.subscribe(self.receiveNoNewPlayers, "NO-NEW-PLAYER")
        self.jugadorHandler=None
        self.root=root
    def eventSubInicio(self,msg):
        print("CONTROLADOR-MENU: SEÑAL RECIBIDA")
    
    def receiveNewPlayers(self,msg):
        print("CONTROLADOR-MENU: HE RECIBIDO EL MENSAJE PARA NUEVOS JUGADORES")
        self.jugadorHandler=msg
    def receiveNoNewPlayers(self,msg):
        print("CONTROLADOR-MENU: HE RECIBIDO EL MENSAJE PARA NO NUEVOS JUGADORES")
        self.jugadorHandler=msg
        print(vars(self.jugadorHandler.getJugadorObject()))