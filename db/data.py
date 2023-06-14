import  pymysql

class DB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='prueba_prototipo'
        )
        self.cursor = self.connection.cursor()
        print("Correcto")
    
    def nuevo_registro(self, user, passw):
        self.user = user
        self.passw = passw

        sql = "INSERT INTO cuanta (usuario, contraseña) VALUES (%s,%s)".format(self.user,self.passw)
        self.cursor.execute(sql)
        self.connection.commit()
        print("ok")

obj = DB()
obj.nuevo_registro("hola","asdasd")