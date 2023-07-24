from dbConnection import dbConnection
class InvetarioDAO(dbConnection):
    def __init__(self):
        super().__init__()
        
    def registrarObjeto(self,username,nickname,password):
        sql = '''INSERT INTO `JUGADOR` (NOMBRE_USUARIO,APODO,CLAVE) 
                VALUES('{}','{}','{}')'''.format(username, nickname, password)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            print("Error : "+str(e.args))
        
        return self.existeJugador(username,password)
            
    