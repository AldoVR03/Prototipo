from datos.dbConnection import dbConnection
from datos.characterDAO import CharacterDAO
class CharacterMapper(dbConnection):
    def __init__(self) -> None:
        super().__init__()
        self.oCharacterDAO=CharacterDAO()
        
    def convertToCharacterModel(self, id, characterModels:list):
        queryResult=self.oCharacterDAO.getCharactersById(id)
        characterList=[]
        # print(len(queryResult))
        if((queryResult)):#SI SE HACEN CAMBIOS EN EL ORDEN DE LAS COLUMNAS DE ESTA TABLA EL CDÓIGO DE ABAJO NO FUNCIONA
            for i,characterDictElem in enumerate(queryResult):
                # print(i,characterDictElem)
                characterModels[i].setId(characterDictElem["ID_PERSONAJE"])
                characterModels[i].setIdClan(characterDictElem["ID_CLAN"])
                characterModels[i].setNombrePersonaje(characterDictElem["NOMBRE_PERSONAJE"])
                characterModels[i].setRaza(characterDictElem["RAZA"])
                characterModels[i].setClase(characterDictElem["CLASE"])
                characterModels[i].setNivelPersonaje(characterDictElem["NIVEL_PERSONAJE"])
                characterModels[i].setVida(characterDictElem["VIDA"])
                characterModels[i].setAtaque(characterDictElem["ATAQUE"])
                characterModels[i].setDefensa(characterDictElem["DEFENSA"])
                characterModels[i].setVelocidad(characterDictElem["VELOCIDAD"])
                characterModels[i].setMonedas(characterDictElem["MONEDAS"])
                characterModels[i].setExpPersonaje(characterDictElem["EXPERIENCIA_PERSONAJE"])
                
                characterModels[i].setHairColor(tuple([int(value) for value in characterDictElem["HCOLOR"].split(",")]))
                characterModels[i].setSkinColor(tuple([int(value) for value in characterDictElem["SCOLOR"].split(",")]))
                characterModels[i].setEyeColor(tuple([int(value) for value in characterDictElem["ECOLOR"].split(",")]))
                characterList.append(characterModels[i])

        return characterList
    def convertToDictRow(self,idJugador,nombrePersonaje,raza,clase,hairColor,skinColor,eyesColor,atq,vel,defe,vida):
        row=(idJugador,nombrePersonaje,raza,clase,vida,atq,defe,vel,hairColor,skinColor,eyesColor)
        tableNames=self.oCharacterDAO.getDictTableNames()
        
        result = dict(zip(tableNames,row))
        return result
            # print("query:", queryResult)
            # characterModel.setId(queryResult[0])
            # characterModel.setNombreUsuario(queryResult[1])
            # characterModel.setApodo(queryResult[2])
            # # print(characterModel.getApodo())
            # characterModel.setNivelCuenta(queryResult[3])
            # # jugadorModel.clave(queryResult[4])
            # print(vars(characterModel))
            # return characterModel