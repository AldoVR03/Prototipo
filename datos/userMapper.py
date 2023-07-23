
from datos.jugadorDAO import JugadorDAO
from datos.gameMasterDAO import GameMasterDAO
# from dbConnection import dbConnection


class JugadorMapper():
    def __init__(self) -> None:
        super().__init__()
        self.jugadorDao=JugadorDAO()
    def convertToPlayerModel(self, username, jugadorModel):
        queryResult=self.jugadorDao.getPlayerByUserName(username)
        if(queryResult):
            # print("query:", queryResult)
            jugadorModel.setId(queryResult[0]["ID_JUGADOR"])
            jugadorModel.setNombreUsuario(queryResult[0]["NOMBRE_USUARIO"])
            jugadorModel.setApodo(queryResult[0]["APODO"])
            print(jugadorModel.getApodo())
            jugadorModel.setNivelCuenta(queryResult[0]["NIVEL_CUENTA"])
            # jugadorModel.clave(queryResult[4])
            print(vars(jugadorModel))
            return jugadorModel
class GameMasterMapper():
    def __init__(self) -> None:
        super().__init__()
        self.oGameMasterDAO=GameMasterDAO()
        
    def convertToGameMasterModel(self, username, gameMasterModel):
        queryResult=self.oGameMasterDAO.getGameMasterByUsername(username)
        if(queryResult):
            print("query:", queryResult)
            gameMasterModel.setId(queryResult[0]["ID_GM"])
            gameMasterModel.setNombreUsuario(queryResult[0]["NOMBRE_USUARIO"])
            gameMasterModel.setApodo(queryResult[0]["APODO"])
            # gameMasterModel.setNivelCuenta(queryResult[0])
            # jugadorModel.clave(queryResult[4])
            print(vars(gameMasterModel))
            return gameMasterModel



# oJugadorMapper=JugadorMapper()
# print(oJugadorMapper.getPlayerByUserName("JohnDoe"))