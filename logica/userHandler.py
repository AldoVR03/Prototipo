from pubsub import pub
class JugadorHandler():
    def __init__(self) -> None:
        pub.subscribe(self.receivePlayer,"PLAYER-OBJECT")
        pub.subscribe(self.receiveCharacters, "CHARACTERS")
        self.__jugadorObject=None
    def receivePlayer(self, msg):
        print("JugadorHandler: Jugador recibido", msg)
        self.__jugadorObject=msg
        # print(vars(self.jugadorObject))
    def receiveCharacters(self,msg):
        print("Me ha llegado:",msg)
        print((vars(msg[0])))
        self.__jugadorObject.addManyCharacters(msg)
    def getJugadorObject(self):
        return self.__jugadorObject
    def setJugadorObject(self,re):
        self.__jugadorObject=re
        
        
class GameMasterHandler():
    def __init__(self) -> None:
        pub.subscribe(self.receiveGameMaster, "GAMEMASTER-OBJECT")
        self.__gameMasterObject=None
    def receiveGameMaster(self,msg):
        print("GameMasterHandler: GM recibido",msg)
        self.__gameMasterObject=msg
        print(vars(self.gameMasterObject))
    def getGameMasterObject(self):
        return self.__gameMasterObject
