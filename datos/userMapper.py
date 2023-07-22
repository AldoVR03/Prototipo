from datos.dbConnection import dbConnection
# from dbConnection import dbConnection


class JugadorMapper(dbConnection):
    def __init__(self) -> None:
        super().__init__()
    def getPlayerByUserName(self,username, jugador):
        sql=''' 
            SELECT *
            FROM JUGADOR
            WHERE NOMBRE_USUARIO = '{}' 
        '''.format(username)
        try:    
            existe = False
            self.cursor.execute(sql)
            consulta = self.cursor.fetchone()
            # print(consulta)
            # if (consulta):
            #     existe = True
            # return existe
        except Exception as e:
                print("Error : "+str(e.args))
        print("JUGADOR-PATH")
        # Transformar a objeto
        if(consulta):
            jugador.id=consulta[0]
            jugador.nombreUsuario=consulta[1]
            jugador.apodo=consulta[2]
            jugador.nivelCuenta=consulta[3]
            jugador.clave=consulta[4]
            return jugador
class GameMasterMapper():
    pass



# oJugadorMapper=JugadorMapper()
# print(oJugadorMapper.getPlayerByUserName("JohnDoe"))