from datos.dbConnection import dbConnection
class CharacterDAO(dbConnection):
    def __init__(self):
        super().__init__()
        
    def getCharactersById(self,id):
        sql=f''' 
            SELECT *
            FROM PERSONAJE
            WHERE ID_JUGADOR = {id}
        '''
        try:    
            existe = False
            self.cursor.execute(sql)
            
            columns=[column[0] for column in self.cursor.description]
            
            # print(consulta)
            # if (consulta):
            #     existe = True
            # return existe
            results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]

            return results
        except Exception as e:
                print("Error : "+str(e.args))
        print("JUGADOR-PATH")
    def saveCharacterById(self,rowDict):
        
        sql = '''INSERT INTO `PERSONAJE` (ID_JUGADOR,NOMBRE_PERSONAJE,RAZA,CLASE,VIDA,ATAQUE,DEFENSA,VELOCIDAD,HCOLOR,SCOLOR,ECOLOR) 
                VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(rowDict["ID_JUGADOR"],rowDict["NOMBRE_PERSONAJE"],rowDict["RAZA"], rowDict["CLASE"],rowDict["VIDA"],rowDict["ATAQUE"],rowDict["DEFENSA"],rowDict["VELOCIDAD"],rowDict["HCOLOR"],rowDict["SCOLOR"],rowDict["ECOLOR"])
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            print("Error : "+str(e.args))
        
        return self.existePersonaje(rowDict["ID_JUGADOR"],rowDict["NOMBRE_PERSONAJE"])
    def getDictTableNames(self):
        sql=f''' 
            SELECT ID_JUGADOR,NOMBRE_PERSONAJE,RAZA,CLASE,VIDA,ATAQUE,DEFENSA,VELOCIDAD,HCOLOR,SCOLOR,ECOLOR
            FROM PERSONAJE
            
        '''
        try:    
            existe = False
            self.cursor.execute(sql)
            
            columns=[column[0] for column in self.cursor.description]
            
            # print(consulta)
            # if (consulta):
            #     existe = True
            # return existe
            

            return columns
        except Exception as e:
                print("Error : "+str(e.args))
        print("JUGADOR-PATH")
    def existePersonaje(self,idJugador,nombrePersonaje):
         
        sql=''' 
            SELECT *
            FROM PERSONAJE
            WHERE ID_JUGADOR = '{}' AND NOMBRE_PERSONAJE = '{}'
        '''.format(idJugador,nombrePersonaje)
        try:    
            existe = False
            self.cursor.execute(sql)
            consulta = self.cursor.fetchone()
            
            if (consulta):
                existe = True
            return existe
        except Exception as e:
                print("Error : "+str(e.args))
# oComp=CharacterDAO()
# # print(oComp.getCharactersById(2))
# print(oComp.getDictTableNames())
            