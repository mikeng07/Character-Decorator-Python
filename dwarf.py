import character

class Dwarf(character.Character):
    """represents dwarf character"""

    def __init__(self,n):
        """initialize a dwarf character"""
        super().__init__(n+ " the Dwarf")

    def abilities(self):
        """return level of abilities of dwarf"""
        return [0,1,0,0]

    def constitution(self):
        """return constitution of dwarf"""
        return 13

    def strength(self):
        """return strength of dwarf"""
        return 15

    def wisdom(self):
        """return wisdom of dwarf"""
        return 10