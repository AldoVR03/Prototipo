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
    
    def nuevo_registro(self, usuario, apodo, contraseña):
        sql = "INSERT INTO `jugador` (NOMBRE_USUARIO,APODO,CLAVE) VALUES('{}','{}','{}')".format(usuario, apodo, contraseña)
        self.cursor.execute(sql)
        self.connection.commit()


obj = DB()