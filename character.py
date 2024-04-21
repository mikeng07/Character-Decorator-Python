import abc
class Character(abc.ABC):
    """Abstract character"""
    def __init__(self,n):
        """initialized the character with a name"""
        self._name = n

    @property
    def name(self):
        """return character name"""
        return self._name

    def __str__(self):
        """string representation of the character"""
        s = self.name
        s += "\n-Abilities-"
        d = self.abilities()
        if d[0] > 0:
            s += "\nArchery: Level " + str(d[0])
        if d[1] > 0:
            s += "\nFighting: Level " + str(d[1])
        if d[2] > 0:
            s += "\nFire Magic: Level " + str(d[2])
        if d[3] > 0 :
            s += "\nHealing: Level " + str(d[3])
        return s + "\n-Stats-\nCon: " + str(self.constitution()) + "\nStr: " + str(self.strength()) + "\nWis: " + str(self.wisdom()) 

    @abc.abstractmethod
    def abilities(self):
        """abilities of character"""
        pass
    @abc.abstractmethod
    def constitution(self):
        """constitution of character"""
        pass
    @abc.abstractmethod
    def strength(self):
        """strength of character"""
        pass
    @abc.abstractmethod
    def wisdom(self):
        """wisdom of character"""
        pass