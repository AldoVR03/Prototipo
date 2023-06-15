import  pymysql

class DB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='aaaaaaaa'
        )
        self.cursor = self.connection.cursor()
    
    def nuevo_registro(self, usuario, apodo, clave):
        sql = "INSERT INTO `jugador` (NOMBRE_USUARIO,APODO,CLAVE) VALUES('{}','{}','{}')".format(usuario, apodo, clave)
        self.cursor.execute(sql)
        self.connection.commit()


    def existeUsuario(self, usuario, clave):
        sql=''' 
            SELECT NOMBRE_USUARIO,CLAVE 
            FROM JUGADOR
            WHERE NOMBRE_USUARIO = '{}' AND CLAVE = '{}'
        '''.format(usuario,clave)
        
        existe = False
        self.cursor.execute(sql)
        consulta = self.cursor.fetchall()
        if (consulta):
            existe = True
        return existe
    
    def cambio_contraseña(self, usuario, claveActual, claveNueva):
        sql=''' 
            UPDATE JUGADOR 
            SET CLAVE ='{}'
            WHERE NOMBRE_USUARIO = '{}' AND CLAVE = '{}'
        '''.format(claveNueva,usuario,claveActual)
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()

obj = DB()