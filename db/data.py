import  pymysql

class DB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='bgczrsjlm8vr2p0j0thn-mysql.services.clever-cloud.com',
            user='umtuhjnmpqvc2v1d',
            password='wdcnRW5Jlr40SSQH1XN3',
            db='bgczrsjlm8vr2p0j0thn'
        )
        self.cursor = self.connection.cursor()
    
    def nuevo_registro(self, usuario, apodo, clave):
        sql = "INSERT INTO `JUGADOR` (NOMBRE_USUARIO,APODO,CLAVE) VALUES('{}','{}','{}')".format(usuario, apodo, clave)
        self.cursor.execute(sql)
        self.connection.commit()


    def existeJugador(self, usuario, clave):
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
    
    def existeGm(self, usuario, clave):
        sql=''' 
            SELECT NOMBRE_USUARIO,CLAVE 
            FROM GM
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