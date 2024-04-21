import character

class Halfling(character.Character):
    """represents halfling character"""

    def __init__(self,n):
        """initialize a halfling character"""
        super().__init__(n+ " the halfling")

    def abilities(self):
        """return level of abilities of halfling"""
        return [0,1,0,0]

    def constitution(self):
        """return constitution of halfling"""
        return 13

    def strength(self):
        """return strength of halfling"""
        return 15

    def wisdom(self):
        """return wisdom of halfling"""
        return 10