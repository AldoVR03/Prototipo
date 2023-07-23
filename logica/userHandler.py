from pubsub import pub
class JugadorHandler():
    def __init__(self) -> None:
        pub.subscribe(self.receivePlayer,"PLAYER-OBJECT")
        self.jugadorObject=None
    def receivePlayer(self, msg):
        print("JugadorHandler: Jugador recibido", msg)
        self.jugadorObject=msg
        # print(vars(self.jugadorObject))
class GameMasterHandler():
    def __init__(self) -> None:
        pass