from datos.dbConnection import dbConnection

class JugadorDAO(dbConnection):
    def __init__(self):
        super().__init__()
        
    def registrarJugador(self,username,nickname,password):
        sql = '''INSERT INTO `JUGADOR` (NOMBRE_USUARIO,APODO,CLAVE) 
                VALUES('{}','{}','{}')'''.format(username, nickname, password)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            print("Error : "+str(e.args))
        
        return self.existeJugador(username,password)
            
    
    def existeJugador(self,nombreUsuario, clave ):
 
        sql=''' 
            SELECT NOMBRE_USUARIO,CLAVE 
            FROM JUGADOR
            WHERE NOMBRE_USUARIO = '{}' AND CLAVE = '{}'
        '''.format(nombreUsuario,clave)
        try:    
            existe = False
            self.cursor.execute(sql)
            consulta = self.cursor.fetchall()
            
            if (consulta):
                existe = True
            return existe
        except Exception as e:
                print("Error : "+str(e.args))

    def actualizarClave(self, username, newPassword,oldPassword):
        sql=f''' 
            UPDATE JUGADOR
            SET CLAVE = {newPassword}
            WHERE NOMBRE_USUARIO = '{username}' AND CLAVE = '{oldPassword}'
        '''
        try:    
            existe = False
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
                print("Error : "+str(e.args))

    def checkCharacter(self,id):
        sql=''' 
            SELECT * 
            FROM PERSONAJE
            WHERE ID_JUGADOR = '{}' 
        '''.format(id)
        try:    
            existe = False
            self.cursor.execute(sql)
            consulta = self.cursor.fetchall()
            
            if (consulta):
                existe = True
            return existe
        except Exception as e:
                print("Error : "+str(e.args))

    def checkUserRegister(self,nombreUsuario, nickname ):
 
        sql=''' 
            SELECT NOMBRE_USUARIO,CLAVE 
            FROM JUGADOR
            WHERE NOMBRE_USUARIO = '{}' AND APODO = '{}'
        '''.format(nombreUsuario,nickname)
        try:    
            existe = False
            self.cursor.execute(sql)
            consulta = self.cursor.fetchall()
            
            if (consulta):
                existe = True
            return existe
        except Exception as e:
                print("Error : "+str(e.args))

    def getPlayerByUserName(self,username):
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
            return consulta
        except Exception as e:
                print("Error : "+str(e.args))
        print("JUGADOR-PATH")
        # Transformar a objeto