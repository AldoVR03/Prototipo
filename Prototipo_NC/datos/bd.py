import pymysql

class DB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='bgczrsjlm8vr2p0j0thn-mysql.services.clever-cloud.com',
            user='umtuhjnmpqvc2v1d',
            password='wdcnRW5Jlr40SSQH1XN3',
            db='bgczrsjlm8vr2p0j0thn'
        )
        self.cursor = self.connection.cursor()


