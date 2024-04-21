import character

class Elf(character.Character):
    """represents elf character"""

    def __init__(self,n):
        """initialize a elf character"""
        super().__init__(n+ " the elf")

    def abilities(self):
        """return level of abilities of elf"""
        return [1,0,0,0]

    def constitution(self):
        """return constitution of elf"""
        return 13

    def strength(self):
        """return strength of elf"""
        return 10

    def wisdom(self):
        """return wisdom of elf"""
        return 15