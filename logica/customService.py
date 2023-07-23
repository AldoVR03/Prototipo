from datos.characterDAO import CharacterDAO
from datos.characterMapper import CharacterMapper
from logica.personajeModel import PersonajeModel
argsDict=(None,)*15
class CharacterService():
    
    def __init__(self) -> None:
        self.oCharacterDAO=CharacterDAO()
        self.oCharacterMapper=CharacterMapper()
    def determineStats(self,raza,clase):
        vel=None
        defe=None
        ataq=None
        vida=None
        if raza == "Humanos":
            if clase == "Guerrero":
                vida=100
                ataq=15
                defe=10
                vel=10
            if clase == "Cazador":
                vida=80
                ataq=10
                defe=65
                vel=15
            if clase == "Bárbaro":
                vida=120
                ataq=18
                defe=5
                vel=8
        elif raza == "Elfos":
            if clase == "Guerrero":
                vida=90
                ataq=12
                defe=7
                vel=15
            if clase == "Cazador":
                vida=70
                ataq=8
                defe=5
                vel=18
            if clase == "Bárbaro":
                vida=100
                ataq=15
                defe=5
                vel=12
        elif raza == "Enanos":
            if clase == "Guerrero":
                vida=120
                ataq=10
                defe=15
                vel=5
            if clase == "Cazador":
                vida=100
                ataq=8
                defe=10
                vel=5
            if clase == "Bárbaro":
                vida=140
                ataq=12
                defe=8
                vel=5
        return {"VIDA":vida,"ATQ":ataq,"DEF":defe,"VEL":5}
        
    def getCharactersById(self, id):
        charactersList=self.oCharacterMapper.convertToCharacterModel(id,[PersonajeModel(*argsDict), PersonajeModel(*argsDict), PersonajeModel(*argsDict),PersonajeModel(*argsDict)])
        print()
        print("Estos son los personajes:", charactersList)
        print()
        return charactersList
    
    def saveCharacterById(self,idJugador,nombrePersonaje,raza,clase,hairColor,skinColor,eyesColor):
        hairColor=",".join(str(elem) for elem in hairColor)
        skinColor=",".join(str(elem) for elem in skinColor)
        eyesColor=",".join(str(elem) for elem in eyesColor)
        print(hairColor,skinColor,eyesColor)
        statsDict=self.determineStats(raza,clase)
        if clase=="Bárbaro":
            clase="Barbaro"
        dictRow=self.oCharacterMapper.convertToDictRow(idJugador,nombrePersonaje,raza,clase,hairColor,skinColor,eyesColor,statsDict["ATQ"],statsDict["VEL"],statsDict["DEF"],statsDict["VIDA"])
        
        return self.oCharacterDAO.saveCharacterById(dictRow)
        

