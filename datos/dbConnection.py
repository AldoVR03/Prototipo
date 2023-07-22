import pymysql
# import threading
# from queue import Queue

class dbConnection:
    connection = pymysql.connect(
            host='bgczrsjlm8vr2p0j0thn-mysql.services.clever-cloud.com',
            user='umtuhjnmpqvc2v1d',
            password='wdcnRW5Jlr40SSQH1XN3',
            db='bgczrsjlm8vr2p0j0thn')
    cursor = connection.cursor()
    def __init__(self):
        self.connection =dbConnection.connection
        self.cursor = dbConnection.cursor

    