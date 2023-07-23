from datos.dbConnection import dbConnection
from datos.jugadorDAO import JugadorDAO
# from dbConnection import dbConnection


class JugadorMapper(dbConnection):
    def __init__(self) -> None:
        super().__init__()
        self.jugadorDao=JugadorDAO()
    def convertToPlayerModel(self, username, jugadorModel):
        queryResult=self.jugadorDao.getPlayerByUserName(username)
        if(queryResult):
            print("query:", queryResult)
            jugadorModel.setId(queryResult[0])
            jugadorModel.setNombreUsuario(queryResult[1])
            jugadorModel.setApodo(queryResult[2])
            print(jugadorModel.getApodo())
            jugadorModel.setNivelCuenta(queryResult[3])
            # jugadorModel.clave(queryResult[4])
            print(vars(jugadorModel))
            return jugadorModel
class GameMasterMapper():
    pass



# oJugadorMapper=JugadorMapper()
# print(oJugadorMapper.getPlayerByUserName("JohnDoe"))