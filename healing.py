import decorator

class Healing(decorator.Decorator):
    """healing ability for a character"""

    def abilities(self):
        """add the healing ability to the character"""
        a_list = super().abilities()
        a_list[1] += 1
        return a_list

    def constitution(self):
        """adds the constitution for an healing character"""
        return super().constitution() + 3

    def strength(self):
        """substracts the strength for an healing character"""
        return super().strength() - 4

    def wisdom(self):
        """adds the wisdom for an healing character"""
        return super().wisdom() + 2