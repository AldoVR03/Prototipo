from datos.jugadorDAO import JugadorDAO
from datos.gameMasterDAO import GameMasterDAO
from logica.jugadorModel import JugadorModel
from logica.gameMasterModel import GameMasterModel
from datos.userMapper import JugadorMapper 
from datos.userMapper import GameMasterMapper
class JugadorService():
    def __init__(self) -> None:
        self.oJugadorDAO=JugadorDAO()
        self.oJugadorMapper=JugadorMapper()
        
    def checkUser(self, username, password):
        exists=self.oJugadorDAO.existeJugador(username,password)
        if exists:
            jugador=self.oJugadorMapper.convertToPlayerModel(username,JugadorModel(None,None,None,None,None))
        else:
            jugador=None
        return exists, jugador
    def registerUser(self, username, nickname, password):
        check=self.oJugadorDAO.registrarJugador(username,nickname,password)
        return check
    def changePasswordUser(self,username, newPassword,oldPassword):
        check=self.oJugadorDAO.actualizarClave(username,newPassword,oldPassword)

    def checkCharacter(self, id):
        return self.oJugadorDAO.checkCharacter(id)
    def checkUserRegister(self,username,nickname):
        return self.oJugadorDAO.checkUserRegister(username,nickname)

class GameMasterService():
    def __init__(self) -> None:
        self.oGameMasterDAO=GameMasterDAO()
        self.oGameMasterMaper=GameMasterMapper()
    def checkUser(self,username,password):
        exists=self.oGameMasterDAO.existeGm(username,password)
        if exists:
            gameMasterObject=self.oGameMasterMaper.convertToGameMasterModel(username, GameMasterModel(*((None,)*4)))
        else:
            gameMasterObject=None
        return exists, gameMasterObject
    def registerUser(self, username, nickname, password):
        check=self.oGameMasterDAO.registrarGM(username,nickname,password)
        return check
    def changePasswordUser(self, username, newPassword,oldPassword):
        pass

    def checkUserRegister(self,username,nickname):
        return self.oGameMasterDAO.checkUserRegister(username,nickname)