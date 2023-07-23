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

# oComp=CharacterDAO()
# print(oComp.getCharactersById(2))
   
            