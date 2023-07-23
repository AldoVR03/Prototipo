from datos.characterDAO import CharacterDAO
from datos.characterMapper import CharacterMapper
from logica.personajeModel import PersonajeModel
argsDict=(None,)*15
class CharacterService():
    
    def __init__(self) -> None:
        self.oCharacterDAO=CharacterDAO()
        self.oCharacterMapper=CharacterMapper()
        
    def getCharactersById(self, id):
        charactersList=self.oCharacterMapper.convertToCharacterModel(id,[PersonajeModel(*argsDict), PersonajeModel(*argsDict), PersonajeModel(*argsDict),PersonajeModel(*argsDict)])
        
        return charactersList
