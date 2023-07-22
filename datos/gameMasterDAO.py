from datos.dbConnection import dbConnection

class GameMasterDAO(dbConnection):
    def __init__(self) -> None:
        def __init__(self):
            super().__init__()
        
    
    def registrarGM(self,username,nickname,password):
        sql = '''INSERT INTO `GM` (NOMBRE_USUARIO,APODO,CLAVE) 
                VALUES('{}','{}','{}')'''.format(username, nickname, password)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("HOLA PASE POR AQUI")
            return self.existeGm(username,password)
        except Exception as e:
            print("Error : "+str(e.args))
       
        
            
    def solicitarGM(self):
        pass
    
    def actualizarGM(self):
        pass
    
    def eliminarGM(self):
        pass

    def existeGm(self,nombreUsuario,clave):
        print(nombreUsuario,clave)
        sql=''' 
            SELECT NOMBRE_USUARIO,CLAVE 
            FROM GM
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

    