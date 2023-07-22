from datos.jugadorDAO import JugadorDAO
from datos.gameMasterDAO import GameMasterDAO
from logica.jugadorModel import JugadorModel
from datos.userMapper import JugadorMapper 
class JugadorService():
    def __init__(self) -> None:
        self.oJugadorDAO=JugadorDAO()
        self.oJugadorMapper=JugadorMapper()
        
    def checkUser(self, username, password):
        exists=self.oJugadorDAO.existeJugador(username,password)
        jugador=self.oJugadorMapper.getPlayerByUserName(username,JugadorModel(None,None,None,None,None))
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

class GmService():
    def __init__(self) -> None:
        self.oGameMasterDAO=GameMasterDAO()
    def checkUser(self,userName,password):
        print("GM-PATH")
        exists=self.oGameMasterDAO.existeGm(userName,password)
        return exists
    def registerUser(self, username, nickname, password):
        check=self.oGameMasterDAO.registrarGM(username,nickname,password)
        return check
    def changePasswordUser(self, username, newPassword,oldPassword):
        pass

    def checkUserRegister(self,username,nickname):
        return self.oGameMasterDAO.checkUserRegister(username,nickname)