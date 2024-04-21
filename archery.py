import decorator

class Archery(decorator.Decorator):
    """Archery ability for a character"""

    def abilities(self):
        """add the archery ability to the character"""
        a_list = super().abilities()
        a_list[0] += 1
        return a_list

    def constitution(self):
        """subtracts the constitution for an archer character"""
        return super().constitution() - 2

    def strength(self):
        """adds the strength for an archer character"""
        return super().strength() + 5

    def wisdom(self):
        """subtracts the wisdom for an archer character"""
        return super().wisdom() - 2