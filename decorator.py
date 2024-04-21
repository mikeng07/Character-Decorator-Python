import abc
import character

class Decorator (character.Character, abc.ABC):
    """Decorator class that adds the abilities to character"""
    #multiple inheritance here. 
    #decorator is abstract
    #inherit from character to ensure that all decorator have same interface
    #as the original one. 

    def __init__(self,char):
        """passes in the character to be decorated"""
        super().__init__(char.name)
        self._character = char

    def abilities(self):
        """gets original abilities on the character attribute"""
        return self._character.abilities()
    
    def constitution(self):
        """gets orginal constitution on the character attribute"""
        return self._character.constitution()

    def strength(self):
        """gets original strength on the character attribute"""
        return self._character.strength()

    def wisdom(self):
        """gets original wisdom on the character attribute"""
        return self._character.wisdom()