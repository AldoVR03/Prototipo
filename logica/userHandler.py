from pubsub import pub
class JugadorHandler():
    def __init__(self) -> None:
        pub.subscribe(self.receivePlayer,"PLAYER-OBJECT")
        pub.subscribe(self.receiveCharacters, "CHARACTERS")
        self.jugadorObject=None
    def receivePlayer(self, msg):
        print("JugadorHandler: Jugador recibido", msg)
        self.jugadorObject=msg
        # print(vars(self.jugadorObject))
    def receiveCharacters(self,msg):
        print("Me ha llegado:",msg)
        print((vars(msg[0])))
        self.jugadorObject.addManyCharacters(msg)
        
        
class GameMasterHandler():
    def __init__(self) -> None:
        pass